# 🧠 Generative AI Demo Project

This project demonstrates a **Generative AI App** that uses:
- **OpenAI GPT-4 API** for text generation
- **LangChain** for orchestration and prompt handling
- **LlamaIndex** for document indexing and RAG (Retrieval-Augmented Generation)
- **Streamlit** as a user interface
- **FAISS** for vector database

## 🎯 Use Case
Build a chatbot that can:
- Answer questions based on uploaded documents (PDF/TXT)
- Perform generative responses to user input
- Log conversation history

---

## 🔧 Project Structure

```
├── app.py                  # Streamlit UI
├── chatbot.py              # Core logic (LangChain, OpenAI, RAG)
├── data/
│   └── sample.pdf          # Sample document for indexing
├── utils.py                # Helper functions
├── requirements.txt        # Dependencies
├── .env                    # OpenAI key
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-org/genai-chatbot.git
cd genai-chatbot
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

Set your OpenAI key in `.env`:
```env
OPENAI_API_KEY=sk-xxxxx
```

---

## 🚀 Run the App

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) to start using the chatbot.

---

## 🧱 Key Components

### ✅ LangChain
- Used to structure the chatbot chain
- Handles conversation memory
- Supports tools (e.g., search or database)

### ✅ LlamaIndex (Optional)
- Indexes and retrieves content from uploaded PDFs or TXT files
- Integrated with FAISS for fast retrieval

### ✅ OpenAI GPT-4
- Generates responses
- Can be replaced with other models (Claude, Gemini, Ollama)

### ✅ Streamlit
- Fast web UI
- Easy to extend and deploy

---

## 📦 Sample Code Snippet

```python
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex

# Load documents
reader = SimpleDirectoryReader('data')
docs = reader.load_data()
index = GPTVectorStoreIndex.from_documents(docs)

# Create chatbot
llm = ChatOpenAI(model_name="gpt-4")
chain = ConversationalRetrievalChain.from_llm(llm, retriever=index.as_retriever())
```

---

## 📊 Example Query

> User: What is this document about?

> AI: Based on the document, it covers ...

---

## ☁️ Deployment
- For public access, deploy using:
  - **Render.com** (free for small apps)
  - **Streamlit Cloud**
  - **Docker + Vercel** (with FastAPI backend)

---

## 🔐 Security Tips
- Sanitize user input to prevent prompt injection
- Limit token usage with max_tokens
- Log API usage with timestamps

---

## 📚 References
- [LangChain Docs](https://docs.langchain.com)
- [LlamaIndex Docs](https://gpt-index.readthedocs.io/)
- [OpenAI API](https://platform.openai.com/docs)
- [Streamlit](https://streamlit.io)

---

## 🤖 Next Steps
- Add support for voice input (e.g., with Whisper API)
- Use Ollama or LLaMA3 for local inference
- Connect to a database for persistent chat memory

---


