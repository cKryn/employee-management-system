# Company Database Management

This project is a Python-based solution for managing a company's organizational structure, including departments, employees, managers, and budget allocations. It uses SQLAlchemy as an ORM to interact with a MySQL database.

## 📂 Project Structure

```
├── env                 # Define virtual environment
├── src                 # The source folder
│   ├── database        # Database-related files
│   │   └── models.py   # Defines ORM models for the database schema
│   ├── __init__.py     # Initialize the database module
│   └── settings.py     # Configures project paths and environment variables
├── .env                # Stores sensitive environment variables (e.g., database credentials)
├── .gitignore          # Specifies intentionally untracked files to ignore
├── main.py             # Initializes and populates the database with sample data
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- MySQL Server
- `pip` package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/cKryn/employee-management-system.git
   cd company-database
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the `.env` file:**
   ```bash
   MYSQL_USERNAME=your_mysql_username
   MYSQL_PASSWORD=your_mysql_password
   ```

4. **Run the main script:**
   ```bash
   python src/main.py
   ```

## 🏗️ Project Components

### 1. `models.py`

Defines the database schema using SQLAlchemy ORM:

- **Employee**: Represents employees linked to departments.
- **Department**: Contains department details and relationships with employees and a manager.
- **Manager**: Manages a department and handles the department's budget.
- **Budgets**: Specifies the resource allocations for each manager.

### 2. `main.py`

Populates the database with initial data for:

- **Departments:** HR, Testing, DevOps
- **Employees:** Assigned to respective departments
- **Managers:** Linked to departments with allocated budgets

### 3. `settings.py`

Configures project paths and loads environment variables using the `.env` file.

## 🗄️ Database Schema Overview

- **Table_Employee** ➡️ Many-to-One ➡️ **Table_Department**
- **Table_Department** ➡️ One-to-One ➡️ **Table_Manager**
- **Table_Manager** ➡️ One-to-Many ➡️ **Table_Budgets**

## ⚙️ Technologies Used

- **Python 3.8+**
- **SQLAlchemy** for ORM
- **MySQL** as the database
- **dotenv** for environment variable management

## 📈 Future Enhancements

- Implement CRUD operations for dynamic data handling.
- Add unit tests for models and database operations.
- Integrate a web interface for managing company data.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

**Developed with ❤️ by [cKryn]**
