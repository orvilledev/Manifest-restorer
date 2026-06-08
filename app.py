"""Streamlit app to convert Amazon shipment manifest CSV to Excel template."""

from datetime import datetime
from pathlib import Path

import streamlit as st

from converter import convert_to_excel, parse_manifest_csv

TEMPLATE_PATH = Path(__file__).parent / "template.xlsx"

st.set_page_config(page_title="Manifest Restorer", page_icon="📦", layout="centered")

st.title("📦 Manifest Restorer")
st.markdown(
    "Upload an Amazon **shipment manifest CSV** and download a "
    "**Send to Amazon** Excel file ready for Seller Central upload."
)

uploaded = st.file_uploader(
    "Upload manifest CSV",
    type=["csv"],
    help="The CSV export from your Amazon shipment workflow (contains SKU, Quantity, etc.)",
)

if uploaded is not None:
    raw_bytes = uploaded.read()

    try:
        metadata, items = parse_manifest_csv(raw_bytes)
    except Exception as exc:
        st.error(f"Could not parse the uploaded file: {exc}")
        st.stop()

    if not items:
        st.warning("No SKU rows were found in the uploaded file.")
        st.stop()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("SKUs", len(items))
    col2.metric("Units", sum(i.quantity for i in items))
    col3.metric("Shipment #", metadata.shipment_number or "—")
    col4.metric("Workflow", (metadata.workflow_name[:12] + "…") if len(metadata.workflow_name) > 12 else metadata.workflow_name or "—")

    with st.expander("Preview converted data", expanded=False):
        st.dataframe(
            [{"Merchant SKU": i.merchant_sku, "Quantity": i.quantity} for i in items],
            use_container_width=True,
            hide_index=True,
        )

    try:
        excel_bytes, _, _ = convert_to_excel(raw_bytes, TEMPLATE_PATH)
    except Exception as exc:
        st.error(f"Conversion failed: {exc}")
        st.stop()

    timestamp = datetime.now().strftime("%Y-%m-%dT%H%M%S")
    output_name = f"ManifestFileUpload_Template_{timestamp}.xlsx"

    st.download_button(
        label="⬇️ Download Excel template",
        data=excel_bytes,
        file_name=output_name,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        type="primary",
    )

else:
    st.info("Upload a `.csv` file to get started.")

with st.expander("How it works"):
    st.markdown(
        """
        **Input** — Amazon shipment manifest CSV with:
        - Header metadata (Shipment number, Workflow name, SKUs, Units)
        - SKU table: `SKU`, `Title`, `ASIN`, `FNSKU`, …, `Quantity`
        - Optional box info at the bottom

        **Output** — Amazon Send to Amazon Excel template with:
        - Instructions, Data definitions, and Example sheets (preserved from template)
        - **Create workflow – template** sheet populated with:
          - `Merchant SKU` ← `SKU`
          - `Quantity` ← `Quantity`
          - Other columns left blank (expiration date, lot code, case pack, box dims)
        """
    )
