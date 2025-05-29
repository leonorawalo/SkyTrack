# SkyTrack

---
## Description

SkyTrack is a Django-powered web app that fetches and displays real-time weather data using the OpenWeatherMap API. Includes RESTful endpoints, a basic Bootstrap UI, and Postman documentation.

## 🚀 Features

- 🔍 Search weather by city name
- ☁️ Display current weather and forecast
- 📡 REST API (Django REST Framework)
- 🎨 Simple frontend with Bootstrap
- 📁 Postman collection for API testing

---

##  SkyTrack Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/weather-dashboard.git
cd weather-dashboard
```
### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Cnfigure API Key
```bash
OPENWEATHER_API_KEY = 'your_api_key_here'
```
### 5. Run Migrations
```bash
python manage.py migrate
```
### 6. Start Server
```bash
python manage.py runserver
```
