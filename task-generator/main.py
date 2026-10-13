import os
import requests

API_KEY = os.environ["TODOIST_API_KEY"]
PROJECT_ID = os.getenv("TODOIST_PROJECT_ID")

URL = "https://api.todoist.com/api/v1/tasks"

SUBJECTS = [
    "授業1",
    "授業2",
    "授業3"
]

CLASS_NUM = 30


def add_task(subject_name):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "content": subject_name,
        "priority": 1
    }

    if PROJECT_ID:
        payload["project_id"] = PROJECT_ID

    r = requests.post(URL, headers=headers, json=payload)

    if r.ok:
        print(f"Created: {subject_name}")
    else:
        print(f"Failed: {subject_name}")
        print(r.text)


for i in range(1, CLASS_NUM + 1):
    for subject_name in SUBJECTS:
        add_task(f"{subject_name} 第{i}回")