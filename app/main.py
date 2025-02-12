from flask import Flask, jsonify, request
import psycopg2
from prometheus_client import start_http_server, Summary
import time

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="honeypot",
        user="honeypot_user",
        password="password"
    )
    return conn

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@app.route('/')
def hello_world():
    return 'Honeypot Flask Server'

@app.route('/attack', methods=['POST'])
@REQUEST_TIME.time()
def log_attack():
    data = request.get_json()
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        'INSERT INTO attacks (attack_type, source_ip, timestamp) VALUES (%s, %s, NOW())',
        (data['attack_type'], data['source_ip'])
    )
    
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Attack logged successfully"}), 200

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)
