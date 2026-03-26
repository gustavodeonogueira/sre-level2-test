from flask import Flask, jsonify
import os
import time
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Métricas
metrics = {
    "total_requests": 0,
    "successful_requests": 0,
    "failed_requests": 0,
    "start_time": time.time()
}

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "mysql"),
        user=os.getenv("DB_USER", "app"),
        password=os.getenv("DB_PASSWORD", "secret"),
        database=os.getenv("DB_NAME", "sre_nivel2")
    )

@app.route('/')
def home():
    metrics["total_requests"] += 1
    metrics["successful_requests"] += 1
    return jsonify({
        "service": "SRE Nível 2 - API",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "timestamp": datetime.now().isoformat()
    })

@app.route('/health')
def health():
    """Health check com verificação de dependências"""
    db_status = "healthy"
    try:
        conn = get_db_connection()
        conn.ping(reconnect=True)
        conn.close()
    except Exception:
        db_status = "unhealthy"

    uptime = time.time() - metrics["start_time"]
    status = "healthy" if db_status == "healthy" else "degraded"

    return jsonify({
        "status": status,
        "database": db_status,
        "uptime_seconds": round(uptime, 2),
        "timestamp": datetime.now().isoformat()
    }), 200 if status == "healthy" else 503

@app.route('/ready')
def ready():
    """Readiness check"""
    try:
        conn = get_db_connection()
        conn.ping(reconnect=True)
        conn.close()
        return jsonify({"ready": True}), 200
    except Exception:
        return jsonify({"ready": False}), 503

@app.route('/metrics')
def get_metrics():
    uptime = time.time() - metrics["start_time"]
    total = metrics["total_requests"]
    success_rate = (metrics["successful_requests"] / total * 100) if total > 0 else 100.0

    return jsonify({
        "total_requests": total,
        "successful_requests": metrics["successful_requests"],
        "failed_requests": metrics["failed_requests"],
        "success_rate_percent": round(success_rate, 2),
        "uptime_seconds": round(uptime, 2)
    })

@app.errorhandler(Exception)
def handle_error(error):
    metrics["total_requests"] += 1
    metrics["failed_requests"] += 1
    return jsonify({"error": str(error)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)