import sqlite3
import os

# 1. Dynamically find the exact folder this script is sitting in
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Bind the database file to that exact folder path
DB_PATH = os.path.join(BASE_DIR, 'enterprise_mock.db')

def run_health_check():
    print("--- ENTERPRISE DATABASE HEALTH REPORT ---\n")
    
    # Print the path so you can visually verify where it is looking
    print(f"[SYSTEM] Connecting to: {DB_PATH}\n")
    
    # 3. Connect using the absolute path
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    # 1. Check Row Counts
    cursor.execute("SELECT COUNT(*) FROM vendors")
    vendors_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM contractors")
    contractors_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM clients")
    clients_count = cursor.fetchone()[0]
    
    print(f"1. ROW COUNTS:")
    print(f"   - Vendors: {vendors_count} (Expected: 50)")
    print(f"   - Contractors: {contractors_count} (Expected: 150)")
    print(f"   - Clients: {clients_count} (Expected: 50)\n")

    # 2. Check Referential Integrity (Orphaned Contractors)
    cursor.execute('''
        SELECT COUNT(*) FROM contractors 
        WHERE vendor_id NOT IN (SELECT vendor_id FROM vendors)
    ''')
    orphan_count = cursor.fetchone()[0]
    
    print(f"2. REFERENTIAL INTEGRITY:")
    if orphan_count == 0:
        print("   - PASS: No orphaned contractors found. All relational links are valid.\n")
    else:
        print(f"   - FAIL: Found {orphan_count} contractors linked to missing vendors!\n")

    # 3. Check Business Logic (Profitability)
    cursor.execute('''
        SELECT COUNT(*) FROM contractors 
        WHERE internal_cost >= client_rate_card
    ''')
    loss_count = cursor.fetchone()[0]
    
    print(f"3. BUSINESS LOGIC (FINANCIALS):")
    if loss_count == 0:
        print("   - PASS: All contractor rate cards represent a profitable margin.\n")
    else:
        print(f"   - FAIL: Found {loss_count} contractors operating at a loss!\n")

    connection.close()
    print("--- HEALTH CHECK COMPLETE ---")

if __name__ == "__main__":
    run_health_check()