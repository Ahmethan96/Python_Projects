from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")

def get_user():

    return "Ibrahim Ahmethan"

if __name__ == "__main__":
    app.run(debug=True)
