class Taskmanager:
    def __init__(self):
        self.task=[]

    def add_task(self , task_name):
        task = {
            'task_name' : task_name,
            'completed' : False
        }

        self.task.append(task)

    def mark_task_status(self , task_status):
        if task in self.task:
            self.task['completed']=True
        else:
            print("Not any task")

    def pending_task(self):
        for task in self.task:
            if not task['completed']:
                return print("pending task" , self.task['taskname'])
            

