# Dockerfile - בונה את Flask API של Rick and Morty

# 1. בוחר תשתית פייתון רשמית
FROM python:3.11-slim

# 2. יוצר תיקיית עבודה בתוך הקונטיינר
WORKDIR /app

# 3. מעתיק את כל קבצי הפרויקט לתוך הקונטיינר
COPY . .

# 4. מתקין את הספריות הדרושות (Flask, requests)
RUN pip install --no-cache-dir flask requests && \
    # בדיקה שההתקנה הצליחה
    python -c "import flask; import requests" || exit 1

# 5. מייצר את קובץ ה-CSV
RUN python fetch_characters.py && \
    # בדיקה שהקובץ נוצר
    if [ ! -f "results.csv" ]; then echo "קובץ results.csv לא נוצר!" && exit 1; fi

# 6. פותח פורט 8080 בתוך הקונטיינר
EXPOSE 8080

# 7. מריץ את האפליקציה
CMD ["python", "app.py"]

