🏢 Enterprise AI Data Assistant
A smart, natural-language chatbot that converts plain English into secure SQL queries. Built with Python, FastAPI, and Gemini 2.5 Flash, it features Role-Based Access Control (RBAC), automatic data visualization, and easy CSV exports.

✨ What It Does
Chat-to-SQL: Ask for data in plain English; the AI handles the database querying.

Role-Based Security: Users only see what their department allows (e.g., Legal cannot see financial rates).

Instant Charts: Automatically turns numerical data into interactive bar charts.

1-Click Export: Download any queried data directly to a CSV file.

🚀 Quick Start Guide
Follow these 5 simple steps to get the app running on your machine:

1. Clone the repository
Open your terminal and run:

Bash
git clone https://github.com/arrkarr-git/ENTERPRISE_CHATBOT.git
cd ENTERPRISE_CHATBOT
2. Install dependencies
Make sure you have Python installed, then run:

Bash
pip install -r requirements.txt
3. Add your API Key

Create a new file named .env in the main folder.

Add your Gemini API key like this:

Plaintext
GEMINI_API_KEY=your_actual_api_key_here
4. Start the backend
Run this command to start the server (it will automatically build the mock database for you!):

Bash
python api.py
5. Open the application
Leave the terminal running, go to your file explorer, and double-click the index.html file to open the chatbot in your web browser.

🧪 Try It Out!
Once the app is running, test these scenarios to see the core features in action:

Test Security (RBAC): Select the Legal Dept role and ask, "List contractors with client rate card more than 200000." (The bot will block this).

Test Data Extraction: Keep the Legal Dept role and ask, "List the vendors whose MSAs are expiring." (You will get a clean data table).

Test Auto-Charts: Select the Executive Dept role and ask, "Count how many vendors we have in each region." (The bot will automatically draw a bar chart!).

Built as a Proof of Concept for natural language enterprise data navigation.
