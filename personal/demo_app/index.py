from flask import Flask
import logging

app = Flask(__name__)
logger = logging.getLogger("TEST")

@app.route("/")
def hello():
    logger.error("Logging is working")
    return "Hello World!"
 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
