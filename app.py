from flask import Flask, render_template, jsonify
import serial
import time
#from serial import Serial

app = Flask(__name__)

# Replace 'COM3' with the appropriate serial port of your Arduino
arduino_serial = serial.Serial('/dev/ttyACM0(Arduino Uno)', 9600, timeout=1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enroll', methods=['POST'])
def enroll():
    # Send a command to Arduino to start enrollment
    arduino_serial.write(b'E')

    # Wait for Arduino response
    time.sleep(2)
    response = arduino_serial.readline().decode('utf-8').strip()

    if response == 'Enrollment successful':
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "failed"})

@app.route('/identify', methods=['POST'])
def identify():
    # Send a command to Arduino to start identification
    arduino_serial.write(b'I')

    # Wait for Arduino response
    time.sleep(2)
    response = arduino_serial.readline().decode('utf-8').strip()

    if response == 'Identification successful':
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "failed"})

if __name__ == '__main__':
    app.run(debug=True)
