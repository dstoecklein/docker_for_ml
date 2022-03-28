from flask import Flask

# dummy app
app = Flask(__name__)
@app.route("/")

def example():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="127.0.0.0", port=int("5000"), debug=True)