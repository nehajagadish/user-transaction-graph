# User & Transaction Relationship Visualization System

## Overview

This project is a graph-based relationship visualization platform that models users, transactions, and shared attributes using Neo4j. The system enables exploration of connections between user accounts through transaction activity and common attributes such as email, phone number, and payment method.

The application provides a REST API for querying graph data and a React-based frontend for visualizing relationships and exploring connected entities.

---

## Objective

The objective of this project is to build a prototype system capable of:

- Storing users and transactions in a graph database
- Creating relationships between entities
- Detecting users that share common attributes
- Visualizing graph relationships
- Supporting user-centric and transaction-centric exploration
- Handling large transaction datasets (100,000+ transactions)

---

## Features

### Data Generation

- Generates synthetic user data using Faker
- Generates 100,000 transaction records
- Creates realistic shared attributes for relationship detection

### Graph Database

- User nodes
- Transaction nodes
- Transaction relationships
- Shared attribute relationships

### REST API

- List users
- Search users
- List transactions
- Filter transactions
- Retrieve user relationships
- Retrieve transaction relationships
- Graph visualization endpoints

### Frontend

- User listing page
- Transaction listing page
- Graph visualization page
- Interactive navigation
- Relationship exploration

### Relationship Detection

The system automatically creates relationships based on:

- Shared email addresses
- Shared phone numbers
- Shared payment methods
- Transaction activity

---

# Technology Stack

## Backend

- Python
- FastAPI
- Neo4j Driver

## Database

- Neo4j Graph Database

## Frontend

- React
- React Router
- Axios
- Cytoscape.js
- React CytoscapeJS

## Containerization

- Docker
- Docker Compose

---

# Graph Data Model

## User Node

Represents a user account.

Properties:

- user_id
- name
- email
- phone
- address
- payment_method

Example:

```text
(U1:User)
```

## Transaction Node

Represents a transaction.

Properties:

- transaction_id
- amount
- ip_address
- device_id

Example:

```text
(T1:Transaction)
```

---

# Relationship Types

## SENT

Represents a user sending a transaction.

```text
(User)-[:SENT]->(Transaction)
```

## RECEIVED_BY

Represents a transaction received by a user.

```text
(Transaction)-[:RECEIVED_BY]->(User)
```

## SHARED_EMAIL

Created when multiple users share the same email address.

```text
(User)-[:SHARED_EMAIL]->(User)
```

## SHARED_PHONE

Created when multiple users share the same phone number.

```text
(User)-[:SHARED_PHONE]->(User)
```

## SHARED_PAYMENT

Created when multiple users share the same payment method.

```text
(User)-[:SHARED_PAYMENT]->(User)
```

---

# Project Structure

```text
user-transaction-graph/
│
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── models.py
│   ├── generate_data.py
│   ├── load_data.py
│   ├── create_relationships.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   └── Navbar.jsx
│   │   │
│   │   ├── pages/
│   │   │   ├── Users.jsx
│   │   │   ├── Transactions.jsx
│   │   │   └── Graph.jsx
│   │   │
│   │   └── App.jsx
│   │
│   ├── package.json
│   └── Dockerfile
│
├── docker-compose.yml
├── users.csv
├── transactions.csv
└── README.md
```

---

# Dataset

The project generates:

- 500 Users
- 100,000 Transactions

Synthetic data is generated using the Faker library.

Shared attributes are intentionally introduced to create meaningful graph relationships.

Example shared relationship counts generated during testing:

- SHARED_EMAIL = 284
- SHARED_PHONE = 393
- SHARED_PAYMENT = 41631

Counts may vary between runs.

---

# Setup Instructions

## Prerequisites

Install:

- Python 3.11+
- Node.js
- Docker Desktop
- Git

---

# Backend Setup

Navigate to backend:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run API:

```bash
uvicorn app:app --reload
```

Backend URL:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

---

# Frontend Setup

Navigate to frontend:

```bash
cd frontend
```

Install packages:

```bash
npm install
```

Start frontend:

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

# Neo4j Setup

Start Neo4j using Docker:

```bash
docker compose up -d
```

Neo4j Browser:

```text
http://localhost:7474
```

Default credentials:

Username:

```text
neo4j
```

Password:

```text
password123
```

---

# Data Generation

Generate sample users and transactions:

```bash
python generate_data.py
```

Generated files:

```text
users.csv
transactions.csv
```

---

# Load Data into Neo4j

```bash
python load_data.py
```

This loads:

- User nodes
- Transaction nodes
- Transaction relationships

---

# Create Shared Relationships

```bash
python create_relationships.py
```

Creates:

- SHARED_EMAIL
- SHARED_PHONE
- SHARED_PAYMENT

relationships between users.

---

# API Endpoints

## Root

```http
GET /
```

Returns API status.

---

## Users

### Get Users

```http
GET /users
```

### Search Users

```http
GET /users?name=john
```

### Create User

```http
POST /users
```

---

## Transactions

### Get Transactions

```http
GET /transactions
```

### Filter Transactions

```http
GET /transactions?min_amount=1000
```

### Create Transaction

```http
POST /transactions
```

---

## Relationships

### User Relationships

```http
GET /relationships/user/{user_id}
```

Example:

```http
GET /relationships/user/U1
```

### Transaction Relationships

```http
GET /relationships/transaction/{transaction_id}
```

Example:

```http
GET /relationships/transaction/T1
```

---

## Graph Endpoints

### General Graph

```http
GET /graph
```

Returns graph elements for visualization.

### User-Centric Graph

```http
GET /graph/user/{user_id}
```

Example:

```http
GET /graph/user/U1
```

Returns graph relationships associated with a specific user.

---

# Frontend Pages

## Users Page

Features:

- View users
- Search users
- User listing

Route:

```text
/
```

or

```text
/users
```

---

## Transactions Page

Features:

- View transactions
- Filter transactions

Route:

```text
/transactions
```

---

## Graph Visualization Page

Features:

- Graph visualization
- User-centric exploration
- Relationship exploration
- User and transaction node visualization

Route:

```text
/graph
```

---

# Docker Deployment

Build containers:

```bash
docker compose build
```

Start services:

```bash
docker compose up -d
```

Stop services:

```bash
docker compose down
```

---

# Assignment Requirements Coverage

| Requirement | Status |
|------------|---------|
| Graph Database | ✅ |
| Neo4j Integration | ✅ |
| 100,000+ Transactions | ✅ |
| User Nodes | ✅ |
| Transaction Nodes | ✅ |
| Relationship Modeling | ✅ |
| Shared Attribute Detection | ✅ |
| Searchable Users | ✅ |
| Searchable Transactions | ✅ |
| User-Centric Exploration | ✅ |
| Transaction-Centric Exploration | ✅ |
| Graph Visualization | ✅ |
| REST API | ✅ |
| Docker Support | ✅ |
| Documentation | ✅ |

---

# Future Improvements

- Advanced graph analytics
- Shortest path discovery
- Suspicious activity detection
- Relationship clustering
- Export graph data
- Dynamic graph filtering
- Enhanced graph styling

---

# Author

Neha Jagadish

Prototype implementation for the User and Transaction Relationship Visualization System assignment.