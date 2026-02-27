# LeadForge
### It is a CRM fullstack application made by using django framework in python.

### Following are the modules which were used
```
django
djangorestframework
psycopg2-binary
```

## Features
#### Authentication System
- Company Owner Registration (creates new company + admin user)
- Employee Registration using unique company code
- Secure Login (session-based authentication)
- Logout functionality
- Get current authenticated user details
- Change current password of current authenticated user

---

#### Multi-Tenant Architecture
- Each company has a unique company code
- Users are strictly bound to one company
- Cross-company data access is blocked
- All sensitive operations validate company ownership
- Company-level isolation enforced across user management actions

----

#### Role - Based Access Control (RBAC)
- Supported Roles
  - `admin`
  - `manager`
  - `member`
- Role Permissions
  - Admin
    - Full control over company users
    - Can delete, reactivate and change roles
  - Manager
    - Limited user management permissions
  - Member
    - Basic access, no management priveleges
- Access control enforced using a custom `role_required` decorator
---

#### User Management
- Soft deleting a user (altering the is_active parameter)
- Reactivate previously deactivated users
- Change user roles within the same company
- Prevent users from modifying accounts of other companies
- Prevent unauthorized self-deletion
- Role and company validation before every user modification

---

#### Security & Data Integrity
- `transaction.atomic()` used to ensure safe company + owner creation
- Authentication required for protected endpoints
- Role validation before sensitive actions
- Company validation before modifying users
- Soft delete strategy prevents accidental data loss
