import psycopg2

def get_db_connection():
    conn = psycopg2.connect(dbname="honeypot_logs", user="honeypot", password="password", host="db")
    return conn
