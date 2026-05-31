# rbac.py

# 1. The Role-Permission Matrix (The Ruleset)
# This strictly maps what each enterprise role is authorized to see.
ROLE_PERMISSIONS = {
    "Legal": ["vendors", "clients"],
    "Resource Manager": ["vendors", "contractors", "clients"],
    "Accounts": ["contractors", "clients"],
    "Business User": ["vendors", "clients"]
}

def get_authorized_tables(user_role):
    """
    Acts as the security middleware. Intercepts the user role, 
    checks the matrix, and returns the allowed tables.
    """
    print(f"\n[SECURITY] Verifying data access for role: '{user_role}'")
    
    # 2. Strict Authorization Check
    # If the role is not in our matrix, we deny access immediately.
    if user_role not in ROLE_PERMISSIONS:
        print(f"[SECURITY] Access Denied: Unrecognized or unauthorized role.")
        return None
        
    # 3. Retrieve Allowed Schema
    authorized_tables = ROLE_PERMISSIONS[user_role]
    print(f"[SECURITY] Access Granted. Authorized tables: {authorized_tables}")
    
    return authorized_tables

# 4. Local Execution Test
# This code only runs if we execute this specific file, proving our logic works.
if __name__ == "__main__":
    print("--- Running RBAC Security Tests ---")
    
    # Test 1: Legal User (Should see vendors and clients)
    get_authorized_tables("Legal")
    
    # Test 2: Resource Manager (Should see everything)
    get_authorized_tables("Resource Manager")
    
    # Test 3: Unauthorized or misspelled role (Should fail safely)
    get_authorized_tables("Marketing Intern")

    # Test 4: Accounts User (Should see contractors and clients)
    get_authorized_tables("Accounts")