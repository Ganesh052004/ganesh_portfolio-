# 🌐 Ganesh S B Portfolio Website

A modern full-stack portfolio website built using HTML, CSS, JavaScript, Python Flask, and MySQL.

## 🚀 Features

- Responsive Portfolio Website
- Modern UI/UX Design
- About Section
- Skills Section
- Projects Showcase
- Education & Certifications
- Achievements Section
- Contact Form
- Admin Dashboard
- Contact Message Management
- Delete Messages
- MySQL Database Integration
- Flask REST API Backend

---

## 🛠 Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript
- Responsive Design

### Backend
- Python
- Flask
- Flask-CORS

### Database
- MySQL

---

## 📂 Project Structure

```text
ganesh_portfolio/
│
├── app.py
├── index.html
├── admin.html
├── 1.jpg
├── ganeshfinal.pdf
├── setup_db.sql
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/ganesh-portfolio.git
cd ganesh-portfolio
```

### 2. Install Dependencies

```bash
pip install flask
pip install flask-cors
pip install mysql-connector-python
```

Or

```bash
pip install -r requirements.txt
```

---

## 🗄 Database Setup

Open MySQL and run:

```sql
CREATE DATABASE portfolio_db;

USE portfolio_db;

CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100),
    email VARCHAR(200) NOT NULL,
    subject VARCHAR(255),
    message TEXT NOT NULL,
    submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🔧 Configure Database

Update database credentials in `app.py`:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "portfolio_db"
}
```

---

## ▶️ Run Application

Start Flask Server:

```bash
python app.py
```

Server runs at:

```text
http://localhost:5000
```

---


## 📩 Contact API

### Submit Contact Form

```http
POST /contact
```

Example Request:

```json
{
  "first_name": "Ganesh",
  "last_name": "SB",
  "email": "ganesh@gmail.com",
  "subject": "Project Inquiry",
  "message": "Hello"
}
```

---

## 📋 Get Contacts

```http
GET /contacts
```

---

## 🗑 Delete Contact

```http
DELETE /contacts/{id}
```

Example:

```http
DELETE /contacts/1
```

---

## 🎯 Future Improvements

- JWT Authentication
- Admin User Management
- Email Notifications
- Blog Section
- Dark/Light Theme Toggle
- Resume Analytics
- Project CMS

---

## 👨‍💻 Author

### Ganesh S B

Software Developer | AI & Web Development Enthusiast

- Email: your-email@example.com
- LinkedIn: https://linkedin.com
- GitHub: https://github.com/Ganesh052004

---

## 📜 License

This project is open-source and available under the MIT License.

---

⭐ If you like this project, consider giving it a star on GitHub.
