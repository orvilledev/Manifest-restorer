"""Streamlit app to convert Amazon shipment manifest CSV to Excel template."""

from datetime import datetime
from pathlib import Path

import streamlit as st

from converter import convert_to_excel, parse_manifest_csv
from ui import (
    card_close,
    card_open,
    inject_styles,
    render_empty_state,
    render_footer,
    render_header,
    render_stat,
)

TEMPLATE_PATH = Path(__file__).parent / "template.xlsx"

st.set_page_config(
    page_title="Manifest Restorer",
    page_icon="📦",
    layout="centered",
    initial_sidebar_state="collapsed",
)

inject_styles()
render_header()

# ── Upload card ───────────────────────────────────────────────────────────────
card_open(
    "Upload manifest",
    "Select the CSV export from your Amazon shipment workflow.",
)

uploaded = st.file_uploader(
    "Manifest CSV",
    type=["csv"],
    label_visibility="collapsed",
    help="CSV export containing SKU, Quantity, and shipment metadata.",
)

card_close()

# ── Processing ────────────────────────────────────────────────────────────────
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

    # Summary card
    card_open(
        "Shipment summary",
        f"Parsed from {uploaded.name}",
    )

    c1, c2, c3, c4 = st.columns(4, gap="small")
    with c1:
        render_stat("SKUs", str(len(items)))
    with c2:
        render_stat("Units", str(sum(i.quantity for i in items)))
    with c3:
        render_stat("Shipment", metadata.shipment_number or "—", small=True)
    with c4:
        workflow = metadata.workflow_name or "—"
        if len(workflow) > 14:
            workflow = workflow[:14] + "…"
        render_stat("Workflow", workflow, small=True)

    card_close()

    # Preview card
    with st.expander("Preview converted data"):
        st.dataframe(
            [{"Merchant SKU": i.merchant_sku, "Quantity": i.quantity} for i in items],
            use_container_width=True,
            hide_index=True,
            height=min(44 + len(items) * 35, 400),
        )

    # Download card
    try:
        excel_bytes, _, _ = convert_to_excel(raw_bytes, TEMPLATE_PATH)
    except Exception as exc:
        st.error(f"Conversion failed: {exc}")
        st.stop()

    timestamp = datetime.now().strftime("%Y-%m-%dT%H%M%S")
    output_name = f"ManifestFileUpload_Template_{timestamp}.xlsx"

    card_open(
        "Download template",
        "Ready for Seller Central upload — includes all template sheets with SKU data populated.",
    )

    st.download_button(
        label="Download Excel template",
        data=excel_bytes,
        file_name=output_name,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        type="primary",
        use_container_width=True,
    )

    st.markdown(
        f'<p class="shadcn-muted" style="margin-top: 0.75rem; text-align: center;">'
        f"{len(items)} SKUs · {sum(i.quantity for i in items)} units · .xlsx</p>",
        unsafe_allow_html=True,
    )

    card_close()

else:
    render_empty_state()

# ── How it works ──────────────────────────────────────────────────────────────
with st.expander("How it works"):
    st.markdown(
        """
        <ol class="shadcn-steps">
            <li>
                <span class="shadcn-step-num">1</span>
                <span>Upload your Amazon <strong>shipment manifest CSV</strong> with header metadata
                (Shipment number, Workflow, SKUs, Units) and a SKU table.</span>
            </li>
            <li>
                <span class="shadcn-step-num">2</span>
                <span>Each row's <code>SKU</code> maps to <code>Merchant SKU</code> and
                <code>Quantity</code> maps directly — other columns stay blank.</span>
            </li>
            <li>
                <span class="shadcn-step-num">3</span>
                <span>Download the populated <strong>Send to Amazon</strong> Excel template with
                Instructions, Data definitions, and Example sheets preserved.</span>
            </li>
        </ol>
        """,
        unsafe_allow_html=True,
    )

render_footer()
