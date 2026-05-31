# Enterprise AI Data Assistant 🚀

A full-stack, AI-powered enterprise data assistant that allows non-technical users to query database tables using natural language. Built with Python, FastAPI, and the Gemini 2.5 Flash model, this application features a sleek "Amazon Rufus" style chat interface, complete with Role-Based Access Control (RBAC), audit logging, and dynamic data visualization.

##  Key Features

* **Natural Language to SQL:** Translates plain English into secure, read-only SQLite queries.
* **Role-Based Access Control (RBAC):** Hardcoded security middleware ensures users can only access tables permitted by their departmental role.
* **Smart Data Visualization:** Frontend automatically detects aggregated numerical data and renders interactive **Chart.js** bar graphs.
* **1-Click CSV Exports:** Users can instantly download query results into Excel-ready CSV files.
* **Immutable Audit Logging:** Every query, role, and AI generated SQL string is logged to an internal database table for compliance tracking.
* **Rate-Limit Resilience:** Built-in auto-retry loops and query caching to gracefully handle external API rate limits.

## 🛠️ Technology Stack
* **Backend:** Python, FastAPI, Uvicorn, SQLite
* **Frontend:** HTML5, TailwindCSS, Vanilla JavaScript, Chart.js
* **AI Engine:** Google Gemini API (`gemini-2.5-flash`)

## 🚀 Quick Start Guide

### 1. Clone the Repository
```bash
git clone [https://github.com/arrkarr-git/ENTERPRISE_CHATBOT.git](https://github.com/arrkarr-git/ENTERPRISE_CHATBOTE.git)
cd ENTERPRISE_CHATBOT
