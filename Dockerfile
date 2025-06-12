# Dockerfile

# 1. Use official Python image
FROM python:3.11-slim

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Set working directory
WORKDIR /app

# 4. Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# 5. Copy project code
COPY . .

# 6. Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
