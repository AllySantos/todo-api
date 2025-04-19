from database.config import supabase
from utils import parser

class TaskRepository:

    def __init__(self):
        self.table_name = 'task'

    def add(self, task_data):

       response = (
           supabase.table(self.table_name)
           .insert(task_data)
           .execute()
       )

       response_data = response.data[0]

       task = parser.parse_task(response_data)

       return task