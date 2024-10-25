from . import Connector

from ytdl_bot.conf import settings

class Repository(Connector):
    def add_user(self, telegram_id: int, username: str, role: str) -> None:
        self.exec(
            f"INSERT INTO users (telegram_id, username, role) VALUES (?, ?, ?)",
            telegram_id, username, role
        )
        self.commit()
    
    def get_user(self, **kwargs):
        query = """
            SELECT telegram_id, username, role
            FROM users
        """
        if kwargs:
            query += " WHERE "
            query += " OR ".join(f"{key} = :{key}" for key in kwargs)
            query += ";"
        
        return self.fetchall(query, **kwargs)
