# Enterprise AI Data Assistant 🚀

A full-stack, AI-powered enterprise data assistant that allows non-technical users to query database tables using natural language. Built with Python, FastAPI, and the Gemini 2.5 Flash model, this application features a sleek "Amazon Rufus" style chat interface, complete with Role-Based Access Control (RBAC), audit logging, and dynamic data visualization.
# Enterprise AI Data Assistant

> A proof-of-concept natural language interface for enterprise data — converts plain English into secure SQL queries with role-based access control, auto-generated charts, and CSV export.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?logo=fastapi&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-2.5%20Flash-4285F4?logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Overview

Most enterprise data tools require SQL knowledge or BI training. This project removes that barrier — business users can query a database by typing a question, with access automatically restricted based on their department role.

**Core capabilities:**

- **Chat-to-SQL** — Natural language questions are translated into SQL queries via Gemini 2.5 Flash
- **Role-Based Access Control (RBAC)** — Department-level permissions enforced at the query layer; users cannot access data outside their clearance
- **Automatic Visualization** — Numerical query results are rendered as interactive bar charts without any user action
- **CSV Export** — Any query result can be downloaded as a CSV in one click

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, FastAPI |
| AI / NLP | Google Gemini 2.5 Flash |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite (mock enterprise data) |
| Auth Model | Role-Based Access Control (RBAC) |

---

## Project Structure

```
ENTERPRISE_CHATBOT/
├── api.py               # FastAPI backend — query handling, RBAC enforcement, Gemini integration
├── index.html           # Frontend chat interface
├── requirements.txt     # Python dependencies
├── .env                 # API key config (not committed)
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- A [Google Gemini API key](https://aistudio.google.com/app/apikey)

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/arrkarr-git/ENTERPRISE_CHATBOT.git
cd ENTERPRISE_CHATBOT
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Configure your API key**

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

**4. Start the backend**

```bash
python api.py
```

This also generates the mock SQLite database on first run.

**5. Open the app**

With the server running, open `index.html` directly in your browser.

---

## Testing the Features

Use these scenarios to verify the core functionality end to end.

### RBAC — Blocked Query

Select the **Legal Dept** role and ask:

> *"List contractors with client rate card more than 200000."*

Expected: Query is blocked. Legal does not have access to financial rate data.

### RBAC — Permitted Query

Keep the **Legal Dept** role and ask:

> *"List the vendors whose MSAs are expiring."*

Expected: A clean data table is returned. Vendor contract data is within Legal's access scope.

### Auto-Visualization

Select the **Executive Dept** role and ask:

> *"Count how many vendors we have in each region."*

Expected: Results are rendered automatically as an interactive bar chart.

---

## Limitations

This is a proof-of-concept, not a production system. Notable constraints:

- The database is a mock SQLite instance with synthetic data
- RBAC rules are hardcoded and not dynamically configurable
- No user authentication — roles are selected manually in the UI
- Not tested for adversarial prompt injection against the SQL generation layer

---

## Contributing

Pull requests are welcome. For significant changes, open an issue first to discuss the approach.

---

## License

[MIT](LICENSE)

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
