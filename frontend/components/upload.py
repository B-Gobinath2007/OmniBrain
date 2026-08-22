import streamlit as st
from frontend.utils.api import upload_file

def render_upload_component():
    """Renders the document upload user interface."""
    st.markdown("### Upload your document")
    
    # Renders file uploader widget
    uploaded_file = st.file_uploader(
        "Choose a PDF or text file",
        type=["pdf", "txt"],
        label_visibility="collapsed"
    )
    
    if uploaded_file is not None:
        st.caption(f"Selected: **{uploaded_file.name}**")
        
        # Upload button
        if st.button("Upload", use_container_width=True, type="primary"):
            with st.spinner("Processing document..."):
                # Read bytes and trigger API
                file_bytes = uploaded_file.getvalue()
                result = upload_file(uploaded_file.name, file_bytes)
                
                if result.get("success"):
                    st.success("Upload successful!")
                    st.session_state.active_doc_id = result.get("document_id")
                    st.session_state.active_filename = result.get("filename")
                    st.info(f"Document ID: `{result.get('document_id')}`")
                else:
                    error_details = result.get("error", "Unknown backend error")
                    st.error(f"Upload failed: {error_details}")
    else:
        # Inform the user when no document is active
        if "active_filename" in st.session_state:
            st.info(f"Active Document: **{st.session_state.active_filename}**")
        else:
            st.caption("No document uploaded yet. Upload a document to start.")
