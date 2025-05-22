from flask import Flask
import os

app = Flask(__name__)  # Correct usage

# Set secret key from environment variable
app.secret_key = os.getenv("SECRET_KEY")

# Optional: Set debug mode based on environment variable
debug_mode = os.getenv('DEBUG', 'False').lower() == 'true'

@app.route("/")
def hello():
    return "Hello from Flask CI/CD!"

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=debug_mode)
