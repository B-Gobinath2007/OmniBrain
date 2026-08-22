import streamlit as st
from typing import List, Any

def render_citations_component(citations: List[Any]):
    """Renders a list of citations or source documents under the AI answer."""
    if not citations:
        return
        
    st.markdown("**Sources:**")
    for idx, citation in enumerate(citations, 1):
        if isinstance(citation, dict):
            source = citation.get("source", f"Document {idx}")
            page = citation.get("page", "")
            page_text = f" Page {page}" if page else ""
            st.markdown(f"[{idx}] {source}{page_text}")
        else:
            st.markdown(f"[{idx}] {citation}")
