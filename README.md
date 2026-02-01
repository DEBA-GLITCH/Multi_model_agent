


# 🧠 Multi-Agent Decision System (Planner–Critic Architecture)

A **multi-agent system** that generates **structured, compliant, and user-friendly plans** for real-world tasks (for starting a business or startup in India), using **LLMs with strict control, validation, and auditability**.


---

## 🚀 Core Idea

This system is built around **three cooperating agents** with **clear responsibilities**:

1. **Planner Agent (LLM-powered)**  
    Generates a structured plan that must follow a strict JSON schema.
    
2. **Critic Agent (deterministic, rule-based)**  
    Evaluates the plan for correctness, completeness, and domain compliance.  
    It can **approve or reject** the plan with explicit reasons.
    
3. **Orchestrator (system-controlled)**  
    Coordinates agents, enforces schemas, handles retries, manages failures, and controls what the user sees.
    

The system **loops internally** until:

- a high-quality plan is approved, or
    
- a safe failure condition is reached
    

---

## 🧩 Why This Project Is Different

- ✅ Strict JSON schema enforcement (no hallucinated structures)
    
- ✅ Deterministic critic (no LLM judging itself)
    
- ✅ Confidence-based approval (not binary keyword checks)
    
- ✅ System-owned memory & audit trail
    
- ✅ Clean UX (no internal retries or reasoning exposed)
    
- ✅ Domain-aware logic (offline vs online vs hybrid businesses in India)
    
---

## ⚙️ Requirements

- Python **3.10+**
    
- A **Groq API key**
    
- Linux / macOS / Windows (tested on Linux)
    

---

## 🔑 Environment Setup

### 1️⃣ Clone the repository

`git clone https://github.com/your-username/your-repo-name.git cd your-repo-name`

### 2️⃣ Create and activate a virtual environment

`python -m venv venv source venv/bin/activate   # Linux / macOS # or venv\Scripts\activate      # Windows`

### 3️⃣ Install dependencies

`pip install -r requirements.txt`

---

## 🔐 Configure Environment Variables

Create a `.env` file in the project root:

`GROQ_API_KEY=your_groq_api_key_here GROQ_MODEL=llama-3.1-8b-instant MAX_ITERATIONS=5`


---

## ▶️ How to Run the System

Start the application:

`python main.py`

You’ll see:

`Multi-Agent System Type 'exit' or 'quit' to stop.`

Example interaction:

`User > I want to open a grocery shop in my city  🧠 Analyzing your request and preparing a compliant plan...  ✅ Here’s a clear, compliant plan you can confidently follow:  Step 1: Register the business Step 2: Obtain GST registration Step 3: Register under Shops & Establishment Act Step 4: Obtain necessary local licenses  🔒 Confidence level: 90% This plan meets standard regulatory and operational requirements.`

Internal retries, rejections, and schema checks are **hidden from the user**.

---

## 🧾 Audit & Transparency

Internally, the system records:

- number of iterations
    
- critic decisions
    
- confidence score
    
- final approved plan
    

This enables:

- debugging
    
- explainability
    
- future persistence or analytics
    

No chain-of-thought or agent opinions are stored.


---

## 📌 Use Cases

- Business setup guidance
    
- Compliance planning
    
- Decision support systems
    
- Agentic architecture demos
    


---

## 🔮 Future Extensions (will come in next update)

- Persistent audit logs (JSON / DB)
    
- Frontend UI
    
- More domain packs (finance, legal, ops)
    
- Tool-based execution
    
- Multi-planner arbitration
    


---
