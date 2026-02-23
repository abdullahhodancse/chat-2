# 💬 JWT Authenticated Multi-Room Real-Time Chat System

A secure real-time multi-room chat application built using **Django**, **Django REST Framework**, and **Django Channels** with **JWT Authentication**.

This system allows authenticated users to connect via WebSocket and participate in real-time conversations across multiple chat rooms. Each chat room maintains its own message history stored in the database.

---

## 🚀 Features

- User Registration & Login System
- JWT Based Authentication
- Authenticated WebSocket Connection
- Multi-Room Chat Support
- Real-Time Message Broadcasting
- Room-Based Message History
- Secure Token Validation During WebSocket Connection
- Message Persistence in Database
- Timestamped Messages

Each message contains:
- Sender Username
- Room Name
- Message Content
- Timestamp

---

## 🛠️ Technologies Used

| Technology | Description |
|------------|-------------|
| Python | Programming Language |
| Django | Web Framework |
| Django REST Framework | API Development |
| Django Channels | WebSocket Support |
| Postgresql| Database |
| JWT | Authentication |
| Daphne | ASGI Server |

---

⚙️ Installation Guide

Follow the steps below to set up and run the project locally.

📥 1. Clone the Repository
git clone https://github.com/abdullahhodancse/chat-2


cd chat-2
🐍 2. Create a Virtual Environment
python -m venv chat_env


▶️ 3. Activate the Virtual Environment (Windows)
chat_env\Scripts\activate


📦 4. Install Required Dependencies
pip install -r requirements.txt


🗄️ 5. Apply Database Migrations
python manage.py makemigrations
python manage.py migrate


🚀 6. Run Django Development Server
python manage.py runserver
🔌 7. Run ASGI WebSocket Server (Daphne)


---


Open a new terminal, activate the virtual environment again, then run:

daphne chat_room.asgi:application

---


🔐 Authentication System
📌 Register User

POST //http://127.0.0.1:8000/account/reg/

Request Body:
{
  "email": "test@gmail.com",
  "password": "korim@12345678",
  "password2": "korim@12345678"
}





📌 Login User & Generate JWT Token

POST //http://127.0.0.1:8000/account/reg/

Request Body:
{
  "email": "test@gmail.com",
  "password": "12345678"
}


Response:
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}


---







🌐 WebSocket Connection

After successful login, connect to WebSocket using your JWT Access Token.

Connection Format:
ws://127.0.0.1:8000/ws/chat/<room_name>/?token=YOUR_ACCESS_TOKEN

---
Example:
Join Room: global

ws://127.0.0.1:8000/ws/chat/global/?token=YOUR_ACCESS_TOKEN

---

Join Room: sports

ws://127.0.0.1:8000/ws/chat/sports/?token=YOUR_ACCESS_TOKEN

---

Join Room: music

ws://127.0.0.1:8000/ws/chat/music/?token=YOUR_ACCESS_TOKEN

---

❗ Only authenticated users with a valid JWT token can establish WebSocket connection.

---

🏠 Multi-Room Chat System

Users can dynamically join any chat room.

Each room has isolated real-time message broadcasting.

Messages are only visible within the joined room.

Chat history is stored separately for each room.




---

📜 Room-Based Chat History API

Retrieve previous messages for a specific room.

GET//http://127.0.0.1:8000/history//<room_name>/

Example:
GET /http://127.0.0.1:8000/history/room_backend/

Returns stored messages from the selected room.



---

📡 API Documentation
Method	Endpoint	Description

POST	http://127.0.0.1:8000/account/reg/  New User

POST	/http://127.0.0.1:8000/account/reg/	Login & Generate JWT

GET	/http://127.0.0.1:8000/history//<room_name>/	Get Chat History




---


🧾 Message Data Structure

Each stored message includes:

Sender

Room Name

Message Content

Timestamp


---

📁 Project Structure
chat_room/
│

├── account/

├── message/

├── chat_room/

│ ├── asgi.py

│ ├── settings.py

│ ├── routing.py
│

├── manage.py
└── requirements.txt

---


📌 Important Note

Make sure to pass a valid JWT Access Token during WebSocket connection.
Unauthenticated connections will be rejected by the server.
