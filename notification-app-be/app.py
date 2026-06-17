from flask import Flask, jsonify
from flask_cors import CORS
import requests
from datetime import datetime

app = Flask(__name__)
CORS(app)


API_URL = "http://4.224.186.213/evaluation-service/notifications"


TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJoZW1hbHJhbW0yMDE2QGdtYWlsLmNvbSIsImV4cCI6MTc4MTY4MzEwNiwiaWF0IjoxNzgxNjgyMjA2LCJpc3MiOiJBZmZvcmQgTWVkaWNhbCBUZWNobm9sb2dpZXMgUHJpdmF0ZSBMaW1pdGVkIiwianRpIjoiZGI2ODJmZjItODc3OS00OWJlLWFjYzYtMTBjM2FmYTZhZDU0IiwibG9jYWxlIjoiZW4tSU4iLCJuYW1lIjoiaGVtYWwgcmFtbSBzIiwic3ViIjoiMjU5Y2JmMzktMjQ5OS00YmM2LTk5MDktZGJiN2MyMjQxNDhjIn0sImVtYWlsIjoiaGVtYWxyYW1tMjAxNkBnbWFpbC5jb20iLCJuYW1lIjoiaGVtYWwgcmFtbSBzIiwicm9sbE5vIjoiMTI3ODAiLCJhY2Nlc3NDb2RlIjoianVGcGh2IiwiY2xpZW50SUQiOiIyNTljYmYzOS0yNDk5LTRiYzYtOTkwOS1kYmI3YzIyNDE0OGMiLCJjbGllbnRTZWNyZXQiOiJSR0RISlBVcXZETlJreHFZIn0.0H2-hnYHeq_NaBJSPSdvBHHqDRM8XfiO6ptwd73XhEo"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}


PRIORITY = {
    "Placement": 3,
    "Result": 2,
    "Event": 1
}


def fetch_notifications():
    try:
        response = requests.get(
            API_URL,
            headers=headers
        )

        if response.status_code == 200:
            data = response.json()
            return data.get("notifications", [])

        return []

    except Exception:
        return []


def get_priority_score(notification):

    category = notification.get("Type", "")

    priority_score = PRIORITY.get(
        category,
        0
    )

    try:
        timestamp = datetime.strptime(
            notification["Timestamp"],
            "%Y-%m-%d %H:%M:%S"
        )

        return (
            priority_score,
            timestamp.timestamp()
        )

    except:
        return (
            priority_score,
            0
        )


@app.route("/")
def home():

    return jsonify({
        "message": "Notification API Running Successfully"
    })


@app.route("/notifications")
def all_notifications():

    notifications = fetch_notifications()

    return jsonify(notifications)


@app.route("/priority-notifications")
def priority_notifications():

    notifications = fetch_notifications()

    top_notifications = sorted(
        notifications,
        key=get_priority_score,
        reverse=True
    )[:10]

    return jsonify(top_notifications)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )