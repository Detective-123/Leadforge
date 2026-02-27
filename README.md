# LeadForge

**LeadForge** is a powerful, multi-tenant CRM built with Django and Django REST Framework, designed for secure company management, robust authentication, and role-based access.

---

## Table of Contents

1. [Features](#features)
2. [Architecture Highlights](#architecture-highlights)
3. [Setup & Installation](#setup--installation)
4. [Usage Guide](#usage-guide)

---

## Features

### Authentication System
- Company Owner Registration (Company + admin creation)
- Employee Registration using company code
- Secure session-based login/logout
- Change current user password
- Get authenticated user details

### Multi-Tenant Architecture
- Companies assigned unique codes
- Data isolation per company
- Strict company-level validation for all user actions

### Role-Based Access Control (RBAC)
- Roles: `admin`, `manager`, `member`
- Fine-grained permissions (custom decorator: `role_required`)

### User Management
- Soft delete/reactivation of users
- Role modification within company scope
- Prevention of unauthorized actions & data access

### Security & Data Integrity
- Atomic transactions for key operations
- Role and company validation at every sensitive step
- Authentication required for protected endpoints
- Soft delete prevents data loss

---

## Architecture Highlights

- **Frameworks:** Django + Django REST Framework
- **Database:** PostgreSQL (`psycopg2-binary`)
- **Strict multi-tenancy:** Companies completely separated
- **Role-based permissions:** Custom decorator implementation
- **Secure authentication:** session-backed, robust by design

---

## Setup & Installation

### Prerequisites

- Python 3.8+
- PostgreSQL

### Install Dependencies `(Recommended: Use virtual env)`

```bash
pip install django djangorestframework psycopg2-binary
```

### Clone the Repository
```bash
git clone https://github.com/Detective-123/Leadforge.git
cd Leadforge
```

### Database Setup
- Create a PostgreSQL database/user
- Configure `settings.py` with credentials

### Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Start Server
```bash
python manage.py runserver
```

----
## Usage Guide

- **Register a company owner:** Begins your company, creates admin.
- **Employee onboarding:** Join company using the company code.
- **Manage users & roles:** Admins can change employee status/roles.
- **Access control:** All endpoints require proper authentication & authorization.

----

