import os
from flask import Flask, render_template

# Securely get environment variables
EMAIL = os.getenv('MEROSS_IOT_EMAIL')
PASSWORD = os.getenv('MEROSS_IOT_PASSWORD')
DEVICE_NAME = "plug-1"


app = Flask(__name__)
print("Waiting for connections!")

@app.route('/')
def hello_world():
    return render_template('index.htm', foo=42)

@app.route('/', methods = ['POST'])
def handle_data():
    print("Received a post request")

if __name__ == '__main__':
    print("using Meross username " + EMAIL)
    app.run(port=8000, debug=True)
