import requests
import csv

url = "https://rickandmortyapi.com/api/character"
results = []

while url:
    response = requests.get(url)
    data = response.json()
    for character in data['results']:
        if (
            character['species'] == 'Human' and
            character['status'] == 'Alive' and
            "Earth" in character['origin']['name']
        ):
            results.append([
                character['name'],
                character['location']['name'],
                character['image']
            ])
    url = data['info']['next']

# כתיבה לקובץ CSV
with open('results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Location', 'Image'])
    writer.writerows(results)

print(f"✅ סיימתי! נשמרו {len(results)} תוצאות בקובץ results.csv")

