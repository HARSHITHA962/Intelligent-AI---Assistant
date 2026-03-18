import streamlit as st
from groq import Groq
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

# ================== 🔑 GROQ API KEY ==================
client = Groq(api_key=os.environ["GROQ_API_KEY"])

MODEL = "llama-3.1-8b-instant"

# ================== LOAD VECTOR DB ==================
index = faiss.read_index("laptop_support_index.faiss")
chunks = np.load("chunks.npy", allow_pickle=True)

embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# ================== SESSION STATE ==================
if "current_chat" not in st.session_state:
    st.session_state.current_chat = []

if "past_chats" not in st.session_state:
    st.session_state.past_chats = []

# ⭐ Flag to prevent duplicate history saving
if "is_new_chat" not in st.session_state:
    st.session_state.is_new_chat = True

st.title("💻 Laptop Support AI Assistant")

# ================== SIDEBAR ==================
st.sidebar.title("📂 Chat History")

# ---------- Open Previous Chats ----------
for i, chat in enumerate(st.session_state.past_chats):
    preview = chat[0]["content"][:30] if chat else "Empty chat"

    if st.sidebar.button(f"Chat {i+1}: {preview}..."):
        st.session_state.current_chat = chat.copy()
        st.session_state.is_new_chat = False  # ⭐ Do NOT resave
        st.rerun()

# ---------- New Chat Button ----------
if st.sidebar.button("🆕 New Chat"):

    # Save ONLY if it was truly a new conversation
    if st.session_state.current_chat and st.session_state.is_new_chat:
        st.session_state.past_chats.append(
            st.session_state.current_chat.copy()
        )

    st.session_state.current_chat = []
    st.session_state.is_new_chat = True
    st.rerun()

# ================== DISPLAY CURRENT CHAT ==================
for msg in st.session_state.current_chat:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ================== USER INPUT ==================
user_input = st.chat_input("Ask anything...")

if user_input:

    # Add user message
    st.session_state.current_chat.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        # ================== HYBRID RAG ==================

        # Retrieve context from FAISS
        q_emb = embed_model.encode([user_input])
        D, I = index.search(np.array(q_emb), k=3)

        # Ignore context if not relevant
        if D[0][0] > 1.2:
            context = ""
        else:
            context = " ".join([chunks[i] for i in I[0]])

        # Build chat messages
        messages = [
            {
                "role": "system",
                "content": """You are a helpful assistant.

You can answer ANY question.

If context is relevant, use it.
Otherwise use your own knowledge."""
            }
        ]

        # Include conversation history
        messages.extend(st.session_state.current_chat)

        # Add context if relevant
        if context:
            messages.append({
                "role": "system",
                "content": f"Relevant context:\n{context}"
            })

        # ================== GROQ API CALL ==================
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
        )

        answer = response.choices[0].message.content

    except Exception as e:
        answer = f"❌ Error: {str(e)}"

    # Add assistant response
    st.session_state.current_chat.append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant"):
        st.markdown(answer)