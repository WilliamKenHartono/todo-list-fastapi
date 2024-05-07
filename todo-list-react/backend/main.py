from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List, Dict

app = FastAPI()

tasks = []

class TaskSchema(BaseModel):
    id: int
    task_name: str
    is_completed: bool = False

class UpdateTask(BaseModel):
    id: Optional[int] = None
    task_name: Optional[str] = None
    is_completed: Optional[bool] = None

# todo methods
@app.get("/tasks")
def get_tasks():
    return tasks

# fetching the task
@app.get("/tasks/{id}")
def get_task_by_id(id: int):
    for task in tasks:
        if task.id == id:
            return task

# post new task
@app.post("/tasks/new")
def create_task(task: TaskSchema):
    tasks.append(task)
    return {"success": True, "message": "successfully created task"}

# Updates task
@app.put("/todos/edit/{id}")
def update_task(id: int, task: UpdateTask):
    if id not in tasks:
        return {'error': 'ID not found'}
    if task.task_name != None:
        tasks[id].task_name = task.task_name
    if task.is_completed != None:
        tasks[id].is_completed = task.is_completed
    
    return tasks[id]

# Deletes task
@app.delete("/tasks/delete/{id}")
def delete_task(id: int):
    if id not in tasks:
        return {"error": "ID not found"}
    del tasks[id]
    return {"msg":"todo has been deleted successfully"}