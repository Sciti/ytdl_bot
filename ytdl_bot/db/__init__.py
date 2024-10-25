import sqlite3


class Connector:
    def __init__(self, db_path: str, mode: str = 'default'):
        self.conn = sqlite3.connect(db_path)
        self.mode = mode

    def exec(self, query: str, *args) -> None:
        with self.conn:
            self.conn.execute(query, args)

    def commit(self) -> None:
        self.conn.commit()

    def fetchone(self, query: str, *args) -> tuple:
        with self.conn:
            cur = self.conn.execute(query, args)
            if self.mode == 'dict':
                columns = [desc[0] for desc in cur.description]
                return dict(zip(columns, cur.fetchone()))
            else:
                return cur.fetchone()

    def fetchall(self, query: str, *args) -> list:
        with self.conn:
            cur = self.conn.execute(query, args)
            if self.mode == 'dict':
                columns = [desc[0] for desc in cur.description]
                return [dict(zip(columns, row)) for row in cur.fetchall()]
            else:
                return cur.fetchall()
