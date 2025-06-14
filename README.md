# Rick and Morty API Challenge - DevOps Engineer Home Exercise

This project queries the [Rick and Morty API](https://rickandmortyapi.com/documentation/) to find all characters who:
- Species: `Human`
- Status: `Alive`
- Origin: starts with `Earth`

It saves the results to a `CSV` file and also exposes a REST API using Flask to access the data.

---

## 🚀 Features

- 🔍 **API Query** using `requests`
- 📄 **CSV Output**: `results.csv`
- 🌐 **REST API** using Flask
- 🐳 **Dockerized App**
- ☸️ **Kubernetes YAML manifests**
- 🔧 **Helm chart for easy deployment**
- 🤖 **GitHub Actions Workflow** (bonus)

---

## 🐍 Requirements

- Python 3.8+
- `pip install -r requirements.txt`

---

## 📁 File Structure

```bash
.
├── fetch_characters.py         # Script to fetch and save characters
├── app.py                      # Flask REST API
├── Dockerfile                  # Docker definition
├── results.csv                 # Output CSV
├── yamls/                      # K8s manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
├── helm/
│   └── rick-api/               # Helm chart
└── README.md                   # This file

