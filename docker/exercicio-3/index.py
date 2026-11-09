import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import psycopg2

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            conn = psycopg2.connect(
                host=os.getenv("DB_HOST", "db"),
                user=os.getenv("DB_USER", "postgres"),
                password=os.getenv("DB_PASS", "postgres"),
                dbname=os.getenv("DB_NAME", "exercicio2")
            )
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS visitas (id SERIAL PRIMARY KEY, msg TEXT)")
            cur.execute("INSERT INTO visitas (msg) VALUES ('Hello from Docker + Postgres!')")
            conn.commit()
            cur.execute("SELECT COUNT(*) FROM visitas")
            total = cur.fetchone()[0]
            conn.close()
            msg = f"Hello from Docker! Conectado no Postgres via hostname db. Visitas gravadas: {total}".encode()
        except Exception as e:
            msg = f"Erro ao conectar no banco: {e}".encode()
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(msg)

HTTPServer(("0.0.0.0", 3000), Handler).serve_forever()