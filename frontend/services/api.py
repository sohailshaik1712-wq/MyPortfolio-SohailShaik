import os

import requests

BASE_URL = os.getenv("BACKEND_URL", "http://localhost:8000").rstrip("/")


def login(username, password):
    return requests.post(
        f"{BASE_URL}/auth/login", data={"username": username, "password": password}
    )


def get_projects():
    return requests.get(f"{BASE_URL}/projects/")


def create_project(data, token):
    headers = {"Authorization": f"Bearer {token}"}

    return requests.post(f"{BASE_URL}/projects/", json=data, headers=headers)


def update_project(project_id, data, token):
    headers = {"Authorization": f"Bearer {token}"}
    # Using PUT for a full update of the project record
    return requests.put(f"{BASE_URL}/projects/{project_id}", json=data, headers=headers)


def delete_project(project_id, token):
    headers = {"Authorization": f"Bearer {token}"}
    return requests.delete(f"{BASE_URL}/projects/{project_id}", headers=headers)
