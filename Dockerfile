# Dockerfile - בונה את Flask API של Rick and Morty

# 1. בוחר תשתית פייתון רשמית
FROM python:3.11-slim

# 2. יוצר תיקיית עבודה בתוך הקונטיינר
WORKDIR /app

# 3. מעתיק את כל קבצי הפרויקט לתוך הקונטיינר
COPY . .

# 4. מתקין את הספריות הדרושות (Flask, requests)
RUN pip install --no-cache-dir flask requests

# 5. פותח פורט 8080 בתוך הקונטיינר
EXPOSE 8080

# 6. מריץ את האפליקציה
CMD ["python", "app.py"]

