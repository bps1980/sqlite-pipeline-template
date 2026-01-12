import sqlite3
from state_machine import StateMachine

class Pipeline:
    def __init__(self, db_path="pipeline.db"):
        self.db_path = db_path
        self.state_machine = StateMachine()

    def connect(self):
        return sqlite3.connect(self.db_path)

    def fetch_pending(self):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT id, name, status FROM leads WHERE status = 'pending'")
        rows = cur.fetchall()
        conn.close()
        return rows

    def process_lead(self, lead):
        lead_id, name, status = lead
        new_status = self.state_machine.next(status)

        conn = self.connect()
        cur = conn.cursor()
        cur.execute("UPDATE leads SET status = ? WHERE id = ?", (new_status, lead_id))
        conn.commit()
        conn.close()

        print(f"Lead {lead_id} transitioned from {status} → {new_status}")

    def run(self):
        pending = self.fetch_pending()
        for lead in pending:
            self.process_lead(lead)

if __name__ == "__main__":
    pipeline = Pipeline()
    pipeline.run()
