import streamlit as st
from chatbot import get_chat_response, init_index

st.set_page_config(page_title="📚 Generative AI Chatbot", layout="wide")
st.title("🧠 Generative AI Document Chatbot")

# Initialize index
if "index" not in st.session_state:
    st.session_state.index = init_index("data")

# Conversation memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

query = st.text_input("Ask a question about the document:")
if query:
    response = get_chat_response(query, st.session_state.index, st.session_state.chat_history)
    st.session_state.chat_history.append((query, response))
    st.write("**AI:**", response)

st.write("---")
uploaded_file = st.file_uploader("Upload new PDF/TXT document", type=["pdf", "txt"])
if uploaded_file:
    with open(os.path.join("data", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.read())
    st.success("Uploaded! Refresh to re-index.")