from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tasks = []

class TaskSchema(BaseModel):
    id: int
    task_name: str
    is_completed: bool

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{id}")
def get_task_by_id(id: int):
    for task in tasks:
        if task.id == id:
            return task

@app.post("/tasks")
def create_task(task: TaskSchema):
    tasks.append(task)
    return {"success": True, "message": "successfully created task"}