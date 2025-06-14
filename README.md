# אתגר DevOps Engineer – Rick and Morty API

הפרויקט שואב מידע מ־[Rick and Morty API](https://rickandmortyapi.com/documentation/) ומחזיר את כל הדמויות שהן:
- Species: `Human`
- Status: `Alive`
- Origin שמתחיל ב־`Earth`

המידע נשמר בקובץ CSV ומוגש גם דרך REST API בפלאסק.

---

## 🚀 תכונות בפרויקט

- 🔍 שאיבת נתונים מ־API עם `requests`
- 📄 יצוא לקובץ CSV
- 🌐 חשיפת REST API בפלאסק
- 🐳 דוקריזציה של האפליקציה
- ☸️ קבצי YAML ל־Kubernetes
- 🔧 דיפלוי עם Helm Chart
- 🤖 CI/CD אוטומטי עם GitHub Actions

---

## 🐍 דרישות

- Python 3.8+
- Docker
- Kubernetes (אופציונלי)
- Helm (אופציונלי)

## 📦 התקנה והרצה

### הרצה מקומית

1. התקן את הספריות הנדרשות:
```bash
pip install -r requirements.txt
```

2. הרץ את סקריפט איסוף הנתונים:
```bash
python fetch_characters.py
```

3. הרץ את שרת ה-Flask:
```bash
python app.py
```

### הרצה עם Docker

1. בנה את ה-Docker image:
```bash
docker build -t rick-and-morty-app .
```

2. הרץ את הקונטיינר:
```bash
docker run -p 8080:8080 rick-and-morty-app
```

## 🌐 REST API Endpoints

- `GET /healthcheck` - בדיקת תקינות המערכת
  ```bash
  curl http://localhost:8080/healthcheck
  ```
  תשובה: `{"status": "OK"}`

- `GET /characters` - קבלת רשימת הדמויות
  ```bash
  curl http://localhost:8080/characters
  ```
  תשובה: מערך של אובייקטים עם שדות: name, location, image

## ☸️ דיפלוי ל-Kubernetes

1. התקן את הקבצים מתיקיית `yamls`:
```bash
kubectl apply -f yamls/
```

2. בדוק את הסטטוס:
```bash
kubectl get pods
kubectl get services
kubectl get ingress
```

## 🔧 דיפלוי עם Helm

1. התקן את ה-Helm chart:
```bash
helm install rick-and-morty ./helm
```

2. בדוק את הסטטוס:
```bash
helm list
```

## 🤖 GitHub Actions Workflow

ה-workflow כולל את השלבים הבאים:
1. יצירת Kubernetes cluster מקומי
2. בניית Docker image
3. דיפלוי האפליקציה ל-cluster
4. הרצת בדיקות על ה-endpoints

ה-workflow רץ אוטומטית בכל push ל-main branch.

---

## 📝 הערות

- האפליקציה רצה על פורט 8080
- הנתונים נשמרים בקובץ `results.csv`
- ה-Docker image מכיל את כל הקבצים הנדרשים

```bash
pip install -r requirements.txt

