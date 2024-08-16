import random
import dataclasses
import string


class Task:
    
    def __init__(self, name: str, status: str, description: str):
        
        self.name = name
        self.status = status
        self.description = description
        self.id = ''.join(random.choices(string.ascii_letters + string.digits, k = 6))


class TaskManager:
    def __init__(self):
        self.tasks = list()
        
        
    def addTask (self, name: str, status: str, description: str):
       task = Task(name, status, description)
       self.tasks.append(task)
       return task.id 
        
        
    def UpdateTask (self, task_id, name: str, status: str, description: str):
        for task in self.tasks:
            if task.id == task_id:
                task.name = name
                task.status = status
                task.description = description
                return True
            return False
        
def DeleteTask(self, task_id: str):
    self.tasks = [task for task in self.tasks if task.id != task_id]
                
TaskManager = TaskManager()

new_task = TaskManager.addTask("Go fishing", "start", "we will go to a river")
print(f"Added task with ID: {new_task}")