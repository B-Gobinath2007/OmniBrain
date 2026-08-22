import streamlit as st
from frontend.components.upload import render_upload_component
from frontend.components.chat import render_chat_component

# Page title and icons
st.set_page_config(
    page_title="OmniBrain",
    page_icon="🧠",
    layout="centered"
)

# Render main header and subtitle
st.markdown("<h1 style='text-align: center;'>OmniBrain</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Multimodal AI Knowledge Assistant</h4>", unsafe_allow_html=True)
st.markdown("---")

# Initialize workspace states if not present
if "active_doc_id" not in st.session_state:
    st.session_state.active_doc_id = None
if "active_filename" not in st.session_state:
    st.session_state.active_filename = None

# Sidebar layout for upload module
with st.sidebar:
    st.markdown("## Ingestion Panel")
    render_upload_component()
    st.markdown("---")
    st.caption("Powered by FastAPI & Streamlit")

# Main page layout for chat history and inputs
render_chat_component()
