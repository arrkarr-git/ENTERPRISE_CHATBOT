import sqlite3
import random
import os
from faker import Faker

def initialize_database():
    # 1. Dynamically find the directory where this script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Construct the absolute path for the database file
    db_path = os.path.join(current_dir, 'enterprise_mock.db')
    
    print(f"Establishing connection to {db_path}...")
    
    # 3. Connect using the absolute path
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Initialize Faker and set seeds for reproducible test data
    fake = Faker()
    Faker.seed(42)
    random.seed(42)

    # ... (connection and Faker setup) ...

    print("Dropping old tables to ensure clean schema...")
    cursor.execute('DROP TABLE IF EXISTS vendors')
    cursor.execute('DROP TABLE IF EXISTS contractors')
    cursor.execute('DROP TABLE IF EXISTS clients')

    print("Creating upgraded tables with new columns...")
    
    # 1. Expanded Vendors Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendors (
            vendor_id TEXT PRIMARY KEY,
            vendor_name TEXT,
            msa_status TEXT,
            msa_expiry_date TEXT,
            region TEXT,
            vendor_rating INTEGER
        )
    ''')

    # 2. Expanded Contractors Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contractors (
            contractor_id TEXT PRIMARY KEY,
            vendor_id TEXT,
            name TEXT,
            job_title TEXT,
            status TEXT,
            client_rate_card INTEGER,
            internal_cost INTEGER
        )
    ''')

    # 3. Expanded Clients Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            client_id TEXT PRIMARY KEY,
            client_name TEXT,
            industry TEXT,
            account_manager TEXT,
            annual_revenue INTEGER
        )
    ''')

    # Clear existing data
    cursor.execute('DELETE FROM vendors')
    cursor.execute('DELETE FROM contractors')
    cursor.execute('DELETE FROM clients')

    print("Generating intelligent mock data via Faker...")

    # Generate 50 Vendors
    vendor_ids = [f"V{str(i).zfill(3)}" for i in range(1, 51)]
    vendors_data = []
    for vid in vendor_ids:
        vendors_data.append((
            vid,
            fake.company(),
            random.choice(['Active', 'Expired']),
            fake.date_between(start_date='-1y', end_date='+2y').strftime('%Y-%m-%d'),
            random.choice(['North America', 'EMEA', 'APAC', 'LATAM']),
            random.randint(1, 5)
        ))
    cursor.executemany('INSERT INTO vendors VALUES (?, ?, ?, ?, ?, ?)', vendors_data)

    # Generate 150 Contractors (Multiple per vendor)
    contractors_data = []
    for i in range(1, 151):
        cid = f"C{str(i).zfill(3)}"
        # GUARANTEE Relational Integrity: Only pick from generated vendor_ids
        vid = random.choice(vendor_ids) 
        
        # GUARANTEE Business Logic: Rate card is always higher than internal cost
        internal = random.randint(80000, 200000)
        margin = random.uniform(1.2, 1.6) # 20% to 60% markup
        rate_card = int(internal * margin)

        contractors_data.append((
            cid,
            vid,
            fake.name(),
            random.choice(['Frontend Engineer', 'Backend Developer', 'Data Scientist', 'DevOps Architect', 'QA Engineer', 'Scrum Master']),
            random.choice(['Active', 'Benched', 'Terminated']),
            rate_card,
            internal
        ))
    cursor.executemany('INSERT INTO contractors VALUES (?, ?, ?, ?, ?, ?, ?)', contractors_data)

    # Generate 50 Clients
    clients_data = []
    for i in range(1, 51):
        clients_data.append((
            f"CL{str(i).zfill(3)}",
            fake.company(),
            random.choice(['Finance', 'Healthcare', 'Retail', 'Manufacturing', 'Technology', 'Aerospace']),
            fake.name(), # Generating a random internal account manager
            random.randint(10000000, 500000000) # Revenue between 10M and 500M
        ))
    cursor.executemany('INSERT INTO clients VALUES (?, ?, ?, ?, ?)', clients_data)

    # Commit and Close
    connection.commit()
    print(f"Successfully inserted 50 Vendors, 150 Contractors, and 50 Clients.")
    connection.close()

if __name__ == "__main__":
    initialize_database()