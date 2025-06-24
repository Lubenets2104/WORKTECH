from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_user_project_entry_and_report():
    # Создаём пользователя
    user = {"name": "Тестовый", "is_manager": 1}
    r_user = client.post("/users/", json=user)
    assert r_user.status_code == 200
    user_id = r_user.json()["id"]

    # Создаём проект
    project = {"name": "Проект тест"}
    r_project = client.post("/projects/", json=project)
    assert r_project.status_code == 200
    project_id = r_project.json()["id"]

    # Добавляем списанное время
    entry = {
        "user_id": user_id,
        "project_id": project_id,
        "date": "2025-06-20",
        "hours": 5
    }
    r_entry = client.post("/time-entries/", json=entry)
    assert r_entry.status_code == 200

    # Проверяем отчёт
    params = {
        "project_id": project_id,
        "start_date": "2025-06-01",
        "end_date": "2025-06-30"
    }
    r_report = client.get("/time-entries/report/", params=params)
    assert r_report.status_code == 200
    data = r_report.json()
    assert len(data) == 1
    assert data[0]["id"] == user_id
    assert data[0]["hours"] == 5
