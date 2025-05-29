from database.config import supabase
from utils import parser

class TaskRepository:

    def __init__(self):
        self.table_name = 'task'


    def get_tasks_by_user(self, user_id):

        response = (
            supabase.table(self.table_name)
            .select('*')
            .eq('user_id', user_id)
            .execute()
        )

        tasks = None
        if len(response.data) > 0:
            response_data = response.data
            tasks = [parser.parse_task(task) for task in response_data]

        return tasks

    def delete(self, task_id):

        response = (
            supabase.table(self.table_name)
            .delete()
            .eq('id', task_id)
            .execute()
        )

        deleted_rows = len(response.data)

        return deleted_rows > 0

    def get_task_by_id_and_user(self, task_id, user_id):

        response = (
            supabase.table(self.table_name)
            .select('*')
            .limit(1)
            .eq('id', task_id)
            .eq('user_id', user_id)
            .execute()
        )
        task = None

        if len(response.data) > 0:
            response_data = response.data[0]
            task = parser.parse_task(response_data)
        return task

    def get_task_by_id(self, task_id):
        response = (
            supabase.table(self.table_name)
            .select('*')
            .limit(1)
            .eq('id', task_id)
            .execute()
        )

        task = None

        if len(response.data) > 0:
            response_data = response.data[0]
            task = parser.parse_task(response_data)
        return task

    def update(self, task_data, task_id):
        response = (
            supabase.table(self.table_name)
            .update(task_data)
            .eq("id", task_id)
            .execute()
        )
        response_data = response.data[0]
        task = parser.parse_task(response_data)
        return task

    def add(self, task_data):

       response = (
           supabase.table(self.table_name)
           .insert(task_data)
           .execute()
       )

       response_data = response.data[0]

       task = parser.parse_task(response_data)

       return task