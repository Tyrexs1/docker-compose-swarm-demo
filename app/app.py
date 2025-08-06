from flask import Flask, request, render_template
import redis
import os

app = Flask(__name__)

# Redis connection
REDIS_HOST = "redis"
REDIS_PORT = 6379
REDIS_PASSWORD_FILE = "/run/secrets/redis_password"

# Read redis password from secret file
with open(REDIS_PASSWORD_FILE, 'r') as f:
    REDIS_PASSWORD = f.read().strip()

r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        user_input = request.form["message"]
        r.rpush("messages", user_input)
        message = "Pesan berhasil disimpan ke Redis!"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
