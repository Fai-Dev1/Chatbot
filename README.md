# 🚀 Cloud AI Chatbot Ecosystem

> A production-grade progressive architecture of an AI chatbot integrated with Google Gemini AI, developed as part of the Cloud Computing Bootcamp.

---

## 📑 Table of Contents
- [Roadmap & Setup Steps](#-roadmap--setup-steps)
- [Architecture & Folder Structure](#-architecture--folder-structure)
- [Development Stages](#-development-stages)
  - [Stage 1: Basic Monolithic Chatbot](#stage-1-basic-monolithic-chatbot)
  - [Stage 2: Decoupled FastAPI & Streamlit](#stage-2-fastapi-backend-integration-decoupled-architecture)
  - [Stage 3: Chatbot with History *(Coming Soon)*](#stage-3-chatbot-with-chat-history-coming-soon)
- [Security & Best Practices](#-security--best-practices)

---

## 🗺️ Roadmap & Setup Steps
1. **Workspace & Environment Setup**:
   * Install Python and VS Code.
   * Create virtual environment: `python -m venv venv`.
   * Activate environment: `.\venv\Scripts\Activate.ps1`
2. **Secure Config & Secret Management**:
   * Get Gemini API key.
   * Protect secrets: add `venv/` and `.env` to `.gitignore`[cite: 18].
3. **Install Dependencies**:
   * Install core packages: `pip install streamlit fastapi[standard] google-genai python-dotenv`[cite: 18].
4. **Build AI App & Integrate APIs**:
   * Implement Gemini integration path and decouple architecture (FastAPI backend + Streamlit frontend)[cite: 18].
5. **Develop & Test**:
   * Run locally via terminal and test live changes[cite: 18].

---

## 📂 Architecture & Folder Structure

```text
Chatbot/
│
├── Stage1/                 # Monolithic implementation
│   ├── chatbot.py          # Direct Streamlit-to-Gemini app
│   └── requirements.txt    # Stage 1 dependencies
│
├── Stage2/                 # Decoupled architecture (Production-ready)
│   ├── backend.py          # FastAPI server handling secure Gemini calls
│   ├── chatbot.py          # Streamlit frontend via HTTP requests
│   └── requirements.txt    # Stage 2 dependencies
│
├── .gitignore              # Environment isolation (.env protection)
└── README.md               # Project documentation

   🛠️ Development Stages
Stage 1: Basic Monolithic Chatbot
Execution: streamlit run Stage1/chatbot.py

Stage 2: FastAPI Backend Integration (Decoupled)
Execution:

Start backend: uvicorn Stage2.backend:app --reload

Start frontend: streamlit run Stage2/chatbot.py