from database.config import supabase

class SessionRepository:

    def __init__(self):
        self.table_name = 'Session'

    def get_session_by_token(self, token):
        response = (
            supabase.table(self.table_name)
            .select('*')
            .limit(1)
            .eq('token', token)
            .execute()
        )

        session = None
        if len(response.data) > 0:
            response_data = response.data[0]
            session = response_data
        return session

    def add(self, session_data):
        response = (
            supabase.table(self.table_name)
            .insert(session_data)
            .execute()
        )
        session_data = response.data[0]
        return session_data
