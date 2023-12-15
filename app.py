from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/voice_assistant', methods=['POST'])
def voice_assistant():
    # Capture audio from the client (you need to implement this in your HTML/JS)
    audio_data = request.files['audio'].read()

    # Send the audio data to the voice recognition script for processing
    result = process_audio(audio_data)

    return jsonify({'response': result.decode('utf-8')})

def process_audio(audio_data):
    # Use subprocess or any other method to run your voice recognition script
    # and capture the response
    result = subprocess.check_output(['python', 'voice_recognition.py'], input=audio_data)

    return result

if __name__ == '__main__':
    app.run(debug=True)
