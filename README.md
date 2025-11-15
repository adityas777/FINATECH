# 💸 FIX YOUR FINANCE — AI-Powered Fintech Platform  
> 🌍 [Live Demo](https://v0-remix-of-smart-finance-dashboard-omega.vercel.app/landing) | Built for **DATATHON 2K25 (Final Round)**  

---

## 🚀 Overview  
**Fix Your Finance** is an AI-driven fintech platform designed to bring **financial inclusion** to the next billion users — freelancers, gig workers, students, and small business owners who lack traditional credit records.  

It uses **AI, ML, and digital behavior analytics** to calculate creditworthiness, manage personal finance, detect fraud, and promote financial literacy through gamified learning.

---

## 🧩 Core Features  

### 💳 Credit Scoring Engine  
Upload your **UPI or bank statement (CSV/PDF)** to get an AI-based **Digital Credit Score (0–900)**.  
- Uses non-traditional data like UPI patterns, cash flow, refunds, and peer ratio.  
- Generates explainable insights: *“Why this person got this score.”*  
- Downloadable Excel report with full breakdown.  

**Formula:**  
`Score = 9 × (0.25*TCS + 0.20*CF + 0.20*PR + 0.15*SD + 0.20*DB)`  
*(TCS = Consistency, CF = Cashflow, PR = Reliability, SD = Discipline, DB = Digital Behavior)*  

---

### 📊 Smart Personal Finance Dashboard  
A unified dashboard that helps users:  
- Track **income, expenses, and savings**  
- View a dynamic **Financial Health Index**  
- Get AI-generated insights and saving tips  

---

### 🕵️ Fraud Detection & Risk Intelligence  
AI engine that flags **fake KYCs**, **money laundering**, and **suspicious spending patterns**.  
- Detects anomalies with Isolation Forest  
- Graph-based circular money flow detection (AML)  
- Blockchain-based transaction integrity  
- Outputs a **Fraud Risk Score (0–100)**
- fraud_score = (
    (kyc_validity * 0.3) +
    (1 - anomaly_ratio) * 0.3 +
    (1 - network_cycles_ratio) * 0.25 +
    (data_integrity * 0.15)
) * 100


---

### 💬 Finance Sarthi — AI Chatbot  
A multilingual AI financial mentor that explains EMI, loans, and investments simply.  
- Works in Hindi & English  
- Voice assistant mode (demo-ready)  
- Offline-friendly for rural users  

---

### 🎮 Financial Literacy Gamification  
Fun mini-games to promote financial awareness:  
- **Budget Balancer** — Manage a virtual monthly budget  
- **Investment Trivia** — Quiz on finance & saving concepts  
- Earn badges 🏅 like *Smart Saver*, *Goal Setter*, and *Debt-Free Champ*  

---

## 🧠 Tech Stack  
**Frontend:** React, Tailwind, Vercel AI SDK  
**Backend:** FastAPI, Python (Pandas, Sklearn, NetworkX)  
**AI:** Isolation Forest, OCR, XAI, Face Matching  
**Deployment:** Vercel (Frontend) | Render (Backend)  

---

## 📈 Why It Matters  
Fix Your Finance enables **trustworthy, transparent, and data-driven lending** —  
without relying on salary slips or CIBIL. It uses real digital footprints to assess creditworthiness and educate users on better money habits.

---

## 👤 Developer  
**Aditya Singh** — IIIT Naya Raipur  
📧 [LinkedIn](https://linkedin.com/in/adityas777)  

> 💬 *“Making finance simple, smart, and inclusive — powered by AI.”*  
