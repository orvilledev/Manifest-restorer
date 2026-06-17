"""Shadcn-inspired UI helpers for Streamlit."""

import streamlit as st

SHADCN_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

:root {
    --primary: #4f46e5;
    --primary-hover: #4338ca;
    --primary-light: #eef2ff;
    --primary-border: #c7d2fe;
    --primary-muted: #6366f1;
}

/* ── Base ─────────────────────────────────────────────── */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    -webkit-font-smoothing: antialiased;
}

.stApp {
    background: linear-gradient(180deg, #f5f7ff 0%, #f8fafc 40%, #fafafa 100%);
}

.block-container {
    max-width: 42rem;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header[data-testid="stHeader"] {
    visibility: hidden;
    height: 0;
}

/* ── Typography ───────────────────────────────────────── */
.shadcn-title {
    font-size: 1.875rem;
    font-weight: 700;
    letter-spacing: -0.025em;
    color: #09090b;
    line-height: 1.2;
    margin: 0;
}

.shadcn-subtitle {
    font-size: 0.875rem;
    color: #71717a;
    margin: 0.5rem 0 0 0;
    line-height: 1.5;
}

.shadcn-label {
    font-size: 0.875rem;
    font-weight: 500;
    color: #09090b;
    margin-bottom: 0.375rem;
}

.shadcn-muted {
    font-size: 0.8125rem;
    color: #71717a;
    line-height: 1.5;
}

/* ── Card ─────────────────────────────────────────────── */
.shadcn-card {
    background: #ffffff;
    border: 1px solid #e4e4e7;
    border-radius: 0.75rem;
    padding: 1.5rem;
    margin-bottom: 1rem;
    box-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05);
}

.shadcn-card-header {
    margin-bottom: 1rem;
}

.shadcn-card-title {
    font-size: 1rem;
    font-weight: 600;
    color: #09090b;
    margin: 0 0 0.25rem 0;
    letter-spacing: -0.01em;
}

.shadcn-card-description {
    font-size: 0.8125rem;
    color: #71717a;
    margin: 0;
    line-height: 1.5;
}

/* ── Badge ────────────────────────────────────────────── */
.shadcn-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.375rem;
    padding: 0.125rem 0.625rem;
    font-size: 0.75rem;
    font-weight: 500;
    border-radius: 9999px;
    border: 1px solid var(--primary-border);
    background: var(--primary-light);
    color: var(--primary);
    margin-bottom: 1rem;
}

.shadcn-badge-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--primary);
}

/* ── Stat cards ───────────────────────────────────────── */
.shadcn-stat {
    background: #ffffff;
    border: 1px solid #e4e4e7;
    border-radius: 0.75rem;
    padding: 1rem 1.25rem;
    box-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05);
}

.shadcn-stat-label {
    font-size: 0.75rem;
    font-weight: 500;
    color: #71717a;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 0.375rem;
}

.shadcn-stat-value {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--primary);
    letter-spacing: -0.025em;
    line-height: 1;
}

.shadcn-stat-value-sm {
    font-size: 0.9375rem;
    font-weight: 600;
    word-break: break-all;
}

/* ── Separator ────────────────────────────────────────── */
.shadcn-separator {
    height: 1px;
    background: #e4e4e7;
    margin: 1.25rem 0;
    border: none;
}

/* ── Steps list ───────────────────────────────────────── */
.shadcn-steps {
    list-style: none;
    padding: 0;
    margin: 0;
}

.shadcn-steps li {
    display: flex;
    gap: 0.75rem;
    padding: 0.625rem 0;
    font-size: 0.8125rem;
    color: #3f3f46;
    line-height: 1.5;
    border-bottom: 1px solid #f4f4f5;
}

.shadcn-steps li:last-child {
    border-bottom: none;
}

.shadcn-step-num {
    flex-shrink: 0;
    width: 1.375rem;
    height: 1.375rem;
    border-radius: 50%;
    background: var(--primary-light);
    border: 1px solid var(--primary-border);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.6875rem;
    font-weight: 600;
    color: var(--primary);
    margin-top: 0.1rem;
}

.shadcn-steps code {
    font-size: 0.75rem;
    background: var(--primary-light);
    border: 1px solid var(--primary-border);
    border-radius: 0.25rem;
    padding: 0.1rem 0.35rem;
    color: var(--primary-hover);
}

/* ── File uploader ────────────────────────────────────── */
[data-testid="stFileUploader"] {
    background: transparent;
}

[data-testid="stFileUploader"] > section {
    background: var(--primary-light);
    border: 1.5px dashed var(--primary-border);
    border-radius: 0.75rem;
    padding: 1.75rem 1rem;
    transition: border-color 0.15s, background 0.15s;
}

[data-testid="stFileUploader"] > section:hover {
    border-color: var(--primary-muted);
    background: #e0e7ff;
}

[data-testid="stFileUploader"] label {
    font-size: 0.875rem !important;
    font-weight: 500 !important;
    color: #09090b !important;
}

[data-testid="stFileUploader"] small {
    color: #71717a !important;
}

[data-testid="stFileUploader"] button {
    background: var(--primary) !important;
    color: #ffffff !important;
    border: 1px solid var(--primary) !important;
    border-radius: 0.5rem !important;
    font-weight: 500 !important;
    font-size: 0.8125rem !important;
    padding: 0.375rem 0.875rem !important;
    box-shadow: 0 1px 2px 0 rgb(79 70 229 / 0.25) !important;
    transition: background 0.15s !important;
}

[data-testid="stFileUploader"] button:hover {
    background: var(--primary-hover) !important;
    border-color: var(--primary-hover) !important;
    color: #ffffff !important;
}

/* ── Primary button ───────────────────────────────────── */
.stDownloadButton > button[kind="primary"],
div[data-testid="stDownloadButton"] > button {
    background: var(--primary) !important;
    color: #ffffff !important;
    border: 1px solid var(--primary) !important;
    border-radius: 0.5rem !important;
    font-weight: 500 !important;
    font-size: 0.875rem !important;
    padding: 0.625rem 1.25rem !important;
    width: 100% !important;
    box-shadow: 0 1px 3px 0 rgb(79 70 229 / 0.3), 0 1px 2px -1px rgb(79 70 229 / 0.2) !important;
    transition: background 0.15s, box-shadow 0.15s !important;
    letter-spacing: -0.01em !important;
}

.stDownloadButton > button[kind="primary"]:hover,
div[data-testid="stDownloadButton"] > button:hover {
    background: var(--primary-hover) !important;
    border-color: var(--primary-hover) !important;
    color: #ffffff !important;
    box-shadow: 0 4px 6px -1px rgb(79 70 229 / 0.25), 0 2px 4px -2px rgb(79 70 229 / 0.2) !important;
}

/* ── Expander → accordion style ───────────────────────── */
[data-testid="stExpander"] {
    background: #ffffff;
    border: 1px solid #e4e4e7;
    border-radius: 0.75rem;
    overflow: hidden;
    box-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05);
    margin-bottom: 0.75rem;
}

[data-testid="stExpander"] details {
    border: none !important;
}

[data-testid="stExpander"] summary {
    font-size: 0.875rem !important;
    font-weight: 500 !important;
    color: #09090b !important;
    padding: 0.875rem 1.25rem !important;
}

[data-testid="stExpander"] summary:hover {
    color: var(--primary) !important;
}

[data-testid="stExpander"] [data-testid="stExpanderDetails"] {
    padding: 0 1.25rem 1rem !important;
    border-top: 1px solid #f4f4f5;
}

/* ── Dataframe ────────────────────────────────────────── */
[data-testid="stDataFrame"] {
    border: 1px solid #e4e4e7;
    border-radius: 0.5rem;
    overflow: hidden;
}

/* ── Alerts ───────────────────────────────────────────── */
[data-testid="stAlert"] {
    border-radius: 0.5rem !important;
    border: 1px solid #e4e4e7 !important;
    font-size: 0.875rem !important;
}

/* ── Footer ───────────────────────────────────────────── */
.shadcn-footer {
    text-align: center;
    font-size: 0.75rem;
    color: #a1a1aa;
    margin-top: 2rem;
    padding-top: 1rem;
    border-top: 1px solid #e4e4e7;
}
</style>
"""


def inject_styles() -> None:
    st.markdown(SHADCN_CSS, unsafe_allow_html=True)


def render_header() -> None:
    st.markdown(
        """
        <div style="margin-bottom: 2rem;">
            <div class="shadcn-badge">
                <span class="shadcn-badge-dot"></span>
                Amazon FBA · Send to Amazon
            </div>
            <h1 class="shadcn-title">Manifest Restorer</h1>
            <p class="shadcn-subtitle">
                Convert shipment manifest CSV exports into Seller Central upload templates.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def card_open(title: str, description: str = "") -> None:
    desc_html = f'<p class="shadcn-card-description">{description}</p>' if description else ""
    st.markdown(
        f"""
        <div class="shadcn-card">
            <div class="shadcn-card-header">
                <p class="shadcn-card-title">{title}</p>
                {desc_html}
            </div>
        """,
        unsafe_allow_html=True,
    )


def card_close() -> None:
    st.markdown("</div>", unsafe_allow_html=True)


def render_stat(label: str, value: str, *, small: bool = False) -> None:
    value_class = "shadcn-stat-value-sm" if small else "shadcn-stat-value"
    st.markdown(
        f"""
        <div class="shadcn-stat">
            <div class="shadcn-stat-label">{label}</div>
            <div class="{value_class}">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_empty_state() -> None:
    st.markdown(
        """
        <div class="shadcn-card" style="text-align: center; padding: 2.5rem 1.5rem;">
            <div style="font-size: 2rem; margin-bottom: 0.75rem; opacity: 0.4;">📄</div>
            <p class="shadcn-card-title" style="margin-bottom: 0.375rem;">No file uploaded</p>
            <p class="shadcn-muted">Drop a manifest CSV above to preview and convert your shipment data.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_footer() -> None:
    st.markdown(
        '<p class="shadcn-footer">Manifest Restorer · Maps SKU &amp; Quantity to Amazon upload template</p>',
        unsafe_allow_html=True,
    )
