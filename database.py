import psycopg2


class Database:
    def __init__(self, host, database, user, password):
        self.conn = psycopg2.connect(host=host, database=database, user=user, password=password)
        self.cur = self.conn.cursor()

    def execute(self, query, params=None):
        self.cur.execute(query, params)
        self.conn.commit()

    def fetch(self, query, params=None):
        self.cur.execute(query, params)
        return self.cur.fetchall()
