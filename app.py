from flask import Flask, jsonify
import csv

app = Flask(__name__)

# טוען את הנתונים מה-CSV
def load_characters():
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

@app.route('/characters', methods=['GET'])
def get_characters():
    return jsonify(load_characters())

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"status": "OK"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

