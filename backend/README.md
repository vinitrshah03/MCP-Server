# 📝 Notes App Backend — MCP Server

## 📖 Overview
This is the **backend** component of the Notes App built using **FastMCP** (Model Context Protocol) — a modern framework for building secure and modular AI-integrated APIs.  
It provides a simple and secure note management system with **Stytch authentication**, **JWT-based session management**, and a **SQLite database** using **SQLAlchemy**.

---

## 🧩 Features
- 🔐 **Bearer Token Authentication** using Stytch
- 🧱 **SQLite Database** with SQLAlchemy ORM
- ⚙️ **RESTful Routes** using FastMCP and Starlette
- 🧾 Add and retrieve user-specific notes
- 🌍 CORS support for frontend integration
- 🚀 Compatible with **Claude Code** via MCP for testing and validation

---

## 🗂️ Project Structure
backend/<br>
├── main.py # Core FastMCP server and routes<br>
├── database.py # Database models and repository<br>
├── .env # Environment variables (Stytch credentials, etc.)<br>
├── .gitignore<br>
├── requirements.txt # Backend dependencies<br>
└── README.md<br>

---

## 🧠 Technologies & Libraries
| Tool / Library   | Purpose |
|------------------|-----------------------------------|
| **Python 3.10+** | Programming Language              |
| **FastMCP**      | MCP Server Framework              |
| **Starlette**    | ASGI Middleware and Routing       |
| **SQLAlchemy**   | ORM for SQLite                    |
| **python-jose**  | JWT decoding and claims           |
| **dotenv**       | Environment variable loading      |
| **Ngrok**        | Local hosting and port forwarding |
| **Stytch**       | Authentication management         |

---

## 📦 Version Requirements
| Component   | Recommended Version |
|-------------|---------------------|
| Python      | 3.10 or later       |
| Node.js     | 18.x or later       |
| Ngrok       | 3.x                 |
| FastMCP     | Latest stable       |
| SQLAlchemy  | 2.x                 |
| python-jose | 3.x                 |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/MCP-Server.git
cd MCP-Server/backend
```

### 2️⃣ Create a Virtual Environment
```
python -m venv venv
venv\Scripts\activate       # (Windows)
# OR
source venv/bin/activate    # (Linux/Mac)
```

### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a .env file in the backend/ directory: 
```
STYTCH_PROJECT_ID=your_project_id
STYTCH_DOMAIN=https://your-stytch-domain.com
```

### 5️⃣ Run the MCP Server
```
python ./main.py
```
--- 

🌐 Port Forwarding with Ngrok

Expose the backend to the internet (for frontend and Stytch API callbacks):
```
ngrok http 8000
```
Copy the generated public URL and use it in your frontend config or Stytch dashboard.

---

⚠️ Notices & Disclaimers

- This project uses Stytch authentication for demonstration purposes.
- Replace placeholder values (API keys, JWT issuers) with your real credentials.
- Do not expose your .env file publicly.

🧱 Intended Use:
This project is for educational and experimental purposes. It should not be deployed in production without proper security hardening.

---

Note for Developers: If you still do not understand this, then I recommend you to check out this amazing YouTube video by "Tech with Tim" -> Click here [https://www.youtube.com/watch?v=j5f2EQf5hkw].
