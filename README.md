# SkyTrack
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
git clone https://github.com/leonorawalo/SkyTrack.git
cd SkyTrack
```
### 2. Create a Virtual Environment
```bash
python -m venv venv  #if you don't have Python, run 'python' without arguments to install it
source venv/Scripts/activate   
```
### 3. Install Dependencies
```bash
pip install djangorestframework requests
```
### 4. Configure API Key
```bash
OPENWEATHER_API_KEY = 'ae936f4eb506aa39d112fbbec2cd0bdf'
```
### 5. Run Migrations
```bash
python manage.py migrate
```
### 6. Start Server
```bash
python manage.py runserver
```
### 7.Run the app at http://127.0.0.1:8000/
### 8.Look up weather!:))
