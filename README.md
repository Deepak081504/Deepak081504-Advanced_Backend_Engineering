# Hospital Management System Backend

## Project Overview

This project is developed using **FastAPI** for managing hospital operations such as:

- Doctor Management
- Patient Management
- Appointment Booking
- Authentication System
- File Upload
- Role-Based Access Control

The backend follows clean architecture and modular coding practices.

---

# Tech Stack

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT Authentication
- Passlib (bcrypt)
- Uvicorn

---

# Features

## Authentication
- JWT Token Authentication
- Password Hashing using bcrypt
- Secure Login System
- Forgot Password Support

## Role-Based Access Control (RBAC)
- Admin
- Doctor
- Patient

## Appointment Management
- Create Appointments
- Prevent Double Booking
- Appointment Status Handling
  - Pending
  - Approved
  - Rejected
  - Completed

## Search & Filtering
- Search Doctors
- Filter Appointments

## Pagination
- Pagination Support for APIs

## File Upload
- Upload Documents
- File Validation

## Error Handling
- Global Exception Handling
- Standard API Responses

## Testing
- Pytest Unit Testing

---

# Project Structure

```bash
Backend/
│
├── app/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   ├── database.py
│   └── main.py
│
├── tests/
│
├── requirements.txt
└── hospital.db
