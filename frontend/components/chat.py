import streamlit as st
from frontend.utils.api import query_backend
from frontend.components.citations import render_citations_component

def render_chat_component():
    """Renders the chat interface for asking questions and displaying history."""
    st.markdown("### Ask a question...")
    
    # Initialize chat history in session_state if not present
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    # Container for rendering chat history
    chat_container = st.container()
    
    # Display existing chat messages
    with chat_container:
        for idx, msg in enumerate(st.session_state.messages):
            if msg["role"] == "user":
                st.markdown(f"👤 **You:**\n\n{msg['content']}")
            else:
                st.markdown(f"🧠 **OmniBrain:**\n\n{msg['content']}")
                if "citations" in msg and msg["citations"]:
                    # Delegate rendering of citations
                    render_citations_component(msg["citations"])
            st.markdown("---")
            
    # Form for chat input field and "Ask" button
    with st.form(key="chat_form", clear_on_submit=True):
        col1, col2 = st.columns([5, 1])
        with col1:
            user_input = st.text_input(
                "Ask a question...",
                placeholder="Ask about the uploaded document...",
                label_visibility="collapsed"
            )
        with col2:
            submit_button = st.form_submit_button("Ask", use_container_width=True, type="primary")
            
        if submit_button and user_input.strip() != "":
            # Add user message to history
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            # Query backend with loading indicator
            with st.spinner("OmniBrain is thinking..."):
                response = query_backend(user_input)
                
            # Add assistant message to history
            st.session_state.messages.append({
                "role": "assistant",
                "content": response.get("answer", "Query processed successfully."),
                "citations": response.get("citations", [])
            })
            
            # Rerun the app to show the updated chat immediately
            st.rerun()
