# 💻 Intelligent AI Assistant for Laptop Support  
### A Context-Aware RAG-Based Diagnostic System for Enterprise IT Support

An enterprise-grade **AI-powered laptop troubleshooting assistant** built using **Retrieval-Augmented Generation (RAG)** to deliver accurate, context-aware, and structured diagnostic support for IT teams and field service engineers.

---

## 📌 Problem Statement
Enterprises manage a wide variety of laptop models across departments. Frequent hardware and software failures disrupt productivity, while traditional IT support systems rely heavily on:
- Manual document searches
- Static FAQ systems
- Repetitive troubleshooting workflows

This results in **high resolution times**, **frequent ticket escalations**, and **increased workload for expert technicians**.

---

## 🚀 Proposed Solution
This project introduces an **Intelligent AI Assistant** that combines:
- Large Language Models (LLMs)
- Vector-based knowledge retrieval
- Guided diagnostic reasoning

The system delivers **accurate, explainable, and structured troubleshooting guidance** grounded in enterprise knowledge.

---

## 🧠 Key Innovations

### 🔹 Context-Aware Diagnostic Engine
- Multi-step guided troubleshooting
- Intelligent follow-up questioning
- Dynamic root-cause narrowing
- Decision-support for IT technicians

### 🔹 High-Accuracy Context Retrieval
- Extracts key details (device, OS, error, symptoms)
- Retrieves only relevant knowledge using FAISS
- Filters low-confidence results
- Reduces hallucination through grounded responses

### 🔹 Continuous Learning Loop
- Stores confirmed resolutions
- Updates vector database
- Improves future responses
- Enables adaptive enterprise knowledge growth

---

## 🏗️ System Architecture
- **Frontend**: Streamlit  
- **LLM**: Groq LLaMA 3.1 (8B Instant)  
- **Vector Database**: FAISS  
- **Embeddings**: Sentence Transformers (MiniLM)  

---

## ⚙️ Functional Modules
- Smart ticket intake
- Guided troubleshooting mode
- Structured repair recommendations
- Likely root cause identification
- Diagnostic steps & repair procedures
- Escalation condition detection

---

## 📊 Evaluation Metrics
- Retrieval precision
- Reduction in troubleshooting time
- Reduction in escalation rate
- Hallucination minimization
- Technician satisfaction improvement

---

## 📈 Impact
- Improved operational efficiency
- Reduced dependency on expert technicians
- Faster issue resolution
- Scalable enterprise IT support
- Reliable and explainable AI-driven diagnostics

---

## 🔐 Environment Variables
Before running or deploying the app, configure the following:
GROQ_API_KEY=your_groq_api_key

---

## ▶️ Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
