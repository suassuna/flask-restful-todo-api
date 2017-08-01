from flask import Flask

app = Flask(__name__)

app.run(port=5000, debug=True)
