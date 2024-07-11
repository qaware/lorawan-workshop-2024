import os
from flask import Flask, render_template, request
from power_switch import PowerPlug, PowerState

# Securely get environment variables
EMAIL = os.getenv('MEROSS_IOT_EMAIL')
PASSWORD = os.getenv('MEROSS_IOT_PASSWORD')
DEVICE_NAME = os.getenv('MEROSS_DEVICE')

app = Flask(__name__)
print("Waiting for connections!")

@app.route('/')
def hello_world():
    return render_template('index.htm', foo=42)

@app.route('/', methods = ['POST'])
def handle_data():
    print("Received a post request!")
    print(request.json['uplink_message']['decoded_payload'])

    plug = PowerPlug(email=EMAIL, password=PASSWORD, device_name=DEVICE_NAME)

    if request.json['uplink_message']['decoded_payload']['motion'] > 20:
        plug.set_power_state(PowerState.ON)
    else:
        plug.set_power_state(PowerState.OFF)

    return 'Data received', 200

if __name__ == '__main__':
    print("using Meross username " + EMAIL)
    # flask’s debug mode is not compatible with vscode’s debugger, so we disable it
    app.run(port=8000, debug=False)
