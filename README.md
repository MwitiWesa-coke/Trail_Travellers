
# Trail Travellers API

Trail Travellers is a ride-hailing and travel management system built with Django and Django REST Framework (DRF).  
The app allows users to book journeys, drivers to be assigned to journeys with vehicles, and admins to manage everything.

---

## 🚀 Problem Being Solved
In many towns and cities, users face challenges booking safe, reliable, and affordable rides.  
On the other hand, drivers and vehicle owners struggle to get consistent customers.  
Trail Travellers bridges this gap by offering:
- A seamless booking platform for users.
- A transparent system for drivers to manage rides.
- Full oversight for admins to ensure quality and safety.

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:MwitiWesa-coke/advanced-api-project.git
   cd Trail_Travellers
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. Start the server:
   ```bash
   python manage.py runserver
   ```

---

## 👤 Usage Guide

### As a User
- Register an account.
- Login to get an authentication token.
- Create a journey (origin, destination, time, vehicle type).
- View your booked journeys.

### As a Driver
- Register as a driver (admin assigns or self-registers).
- Login to receive driver token.
- Get assigned to journeys.
- Mark journeys as completed.

### As an Admin
- Register/login as an admin.
- Create, update, or delete any user, driver, or journey.
- Assign drivers and vehicles to journeys.

---

## 🔑 API Testing with curl

### 1. Register a New User
```bash
curl -X POST http://127.0.0.1:8000/api/accounts/register/  -H "Content-Type: application/json"  -d '{
  "full_name": "Victor Othis",
  "email": "Othis@exmple.com",
  "phone": "0712345678",
  "password": "StrongPass123"
}'
```

### 2. Login a User
```bash
curl -X POST http://127.0.0.1:8000/api/accounts/login/  -H "Content-Type: application/json"  -d '{
  "email": "Othis@exmple.com",
  "password": "StrongPass123"
}'
```

Save the returned token for authorization.

---

### 3. Create a Journey (User)
```bash
curl -X POST http://127.0.0.1:8000/api/rides/journeys/  -H "Content-Type: application/json"  -H "Authorization: Token **token**"  -d '{
  "origin": "Kisumu",
  "destination": "Nairobi",
  "departure_time": "2025-09-01T08:00:00Z",
  "vehicle_type": "Car"
}'
```

---

### 4. Assign a Driver & Vehicle

#### Create a Driver
```bash
curl -X POST http://127.0.0.1:8000/api/rides/drivers/  -H "Content-Type: application/json"  -H "Authorization: Token **token**"  -d '{
  "user_id": 2,
  "license_number": "KAB123X",
  "vehicle_type": "Car",
  "national_id": "11555842",
  "user": "9",
  "experience_years": 5
}'
```

#### Login as Driver
```bash
curl -X POST http://127.0.0.1:8000/api/accounts/login/  -H "Content-Type: application/json"  -d '{
   "email": "driver_eml@example.com",
   "password": "driver_password"
}'
```

#### Assign a Vehicle
```bash
curl -X POST http://127.0.0.1:8000/api/rides/vehicles/add/  -H "Content-Type: application/json"  -H "Authorization: Token **token**"  -d '{
  "driver_id": 2,
  "vehicle_model": "Toyota Prius",
  "plate_number": "KAA123A",
  "capacity": 4
}'
```

---

### 5. Admin Testing

#### Register an Admin
```bash
curl -X POST http://127.0.0.1:8000/api/accounts/register/  -H "Content-Type: application/json"  -d '{
   "full_name": "Admin User",
   "email": "admin@example.com",
   "password": "StrongPassword123",
   "phone":  "012125625",
   "role": "admin"
}'
```

#### Login as Admin & Manage Journeys
```bash
curl -H "Authorization: Token $ADMIN_TOKEN" http://127.0.0.1:8000/api/rides/journeys/
```

---

### 6. Driver Testing

#### Mark Journey as Completed
```bash
curl -X PATCH http://127.0.0.1:8000/api/rides/journeys/1/ -H "Content-Type: application/json" -H "Authorization: Token $DRIVER_TOKEN" -d '{"status": "completed"}'
```

---

## ✅ Summary
- **Users**: Book journeys.  
- **Drivers**: Get assigned & complete journeys.  
- **Admins**: Manage users, drivers, vehicles, and journeys.

This system ensures **reliable rides for passengers**, **steady jobs for drivers**, and **centralized control for admins**.
