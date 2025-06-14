from flask import Flask, jsonify
import csv
import os

app = Flask(__name__)

# טוען את הנתונים מה-CSV
def load_characters():
    try:
        if not os.path.exists('results.csv'):
            return []
            
        characters = []
        with open('results.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                characters.append({
                    "name": row["Name"],
                    "location": row["Location"],
                    "image": row["Image"]
                })
        return characters
    except Exception as e:
        print(f"שגיאה בטעינת הנתונים: {str(e)}")
        return []

@app.route('/characters', methods=['GET'])
def get_characters():
    characters = load_characters()
    if not characters:
        return jsonify({"error": "לא נמצאו נתונים"}), 404
    return jsonify(characters)

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    try:
        # בדיקה שהאפליקציה יכולה לגשת לקבצים
        if not os.path.exists('results.csv'):
            return jsonify({"status": "WARNING", "message": "קובץ CSV לא נמצא"}), 200
            
        # בדיקה שהאפליקציה יכולה לטעון נתונים
        characters = load_characters()
        if not characters:
            return jsonify({"status": "WARNING", "message": "לא נמצאו נתונים"}), 200
            
        return jsonify({"status": "OK", "message": "המערכת פועלת כראוי"})
    except Exception as e:
        return jsonify({"status": "ERROR", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

