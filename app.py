from flask import Flask
<<<<<<< HEAD
app = Flask(__name__)
=======
import os

secret_key = os.getenv('SECRET_KEY')
debug_mode = os.getenv('DEBUG')
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

>>>>>>> cd5ac3b (Initial commit without secret)

@app.route("/")
def hello():
    return "Hello from Flask CI/CD!"
<<<<<<< HEAD
=======
@app.route('/health')
def health():
    return 'OK', 200

>>>>>>> cd5ac3b (Initial commit without secret)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
