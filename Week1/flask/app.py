from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask app running on EC2 with Nginx!"

if __name__ == "__main__":
    app.run()