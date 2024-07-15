# Attendance Management System

## Overview

This project is an Attendance Management System built using Flask for the backend and MongoDB for the database. It allows managers to create and manage staff rosters, and staff to mark their attendance.

## Features

- **Authentication & Authorization:**
  - Roles: Manager and Staff.
  - Only authenticated managers can create/edit/view the roster.
  - Only authenticated staff can mark their attendance.
  
- **Roster Management:**
  - Managers can add new staff members, set working days and shifts, and set weekly offs.
  - Staff members can view their assigned shifts.

- **Attendance Management:**
  - Staff members can mark their attendance.

## Technology Stack

- **Backend Framework:** Flask
- **Database:** MongoDB

## Setup Instructions

### Prerequisites

- Python 3.x
- MongoDB (Ensure MongoDB is installed and running on your machine)
- MongoDB Compass (Optional, for database management)

### Installation

1. **Clone the repository:**

```sh
git clone https://github.com/yourusername/attendance-management-system.git
cd attendance-management-system

2. **Create and activate a virtual environment**

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. ** install dependenices **
pip install -r requirements.txt

4. ** run the app **
flask run

