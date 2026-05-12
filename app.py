from flask import Flask, jsonify, request
from flask_cors import CORS
import random
import time

app = Flask(__name__)
# Enable CORS for all origins and all API routes
CORS(app, resources={r"/api/*": {"origins": "*"}}) 


@app.route('/api/risk-detection', methods=['GET'])
def risk_detection():
    # Simulate smart risk detection based on random factors
    risk_level = random.choice(['Low', 'Medium', 'High', 'Low', 'Low']) # Bias towards low
    reasons = {
        'Low': 'Area looks calm. Good lighting.',
        'Medium': 'Unusual crowd density detected.',
        'High': 'Sudden loud noises detected. Suspicious movement.'
    }
    
    return jsonify({
        'status': 'success',
        'risk_level': risk_level,
        'reason': reasons[risk_level],
        'timestamp': time.time()
    })

@app.route('/api/voice-sos', methods=['POST'])
def voice_sos():
    # Simulate voice-based hidden SOS activation & AI Panic Detection
    data = request.json or {}
    # Accept both 'command' and 'transcript' for better frontend compatibility
    command = (data.get('command') or data.get('transcript') or '').lower()
    
    if not command:
        return jsonify({'status': 'ignored', 'message': 'No audio input detected.'})
        
    # 1. Keyword Matching
    emergency_keywords = ['help me', "i'm not safe", 'im not safe', 'emergency', 'activate guardian', 'help']
    keyword_detected = any(keyword in command for keyword in emergency_keywords)
    
    # 2. AI Emotion/Panic Detection Simulation
    # Check for urgency factors: length, exclamation indicators (if any), repetition
    words = command.split()
    panic_score = 0
    if len(words) < 5: 
        panic_score += 20 # Short, abrupt phrases often indicate panic
    
    urgent_words = ['please', 'stop', 'someone', 'quick', 'fast', 'now']
    panic_score += sum(30 for word in urgent_words if word in words)
    
    is_panicking = panic_score >= 50
    
    if keyword_detected or is_panicking:
        return jsonify({
            'status': 'success',
            'message': 'High panic or emergency keyword detected. Emergency Mode Initiated.',
            'action': 'emergency_mode',
            'panic_score': panic_score,
            'keywords_found': keyword_detected
        })
    else:
        return jsonify({
            'status': 'ignored',
            'message': 'Speech transcribed but no threat detected.',
            'transcription': command
        })

@app.route('/api/emergency-response', methods=['POST'])
def emergency_response():
    # Simulate the automated emergency response
    data = request.json or {}
    lat = data.get('lat', 'Unknown')
    lng = data.get('lng', 'Unknown')
    
    # In a real app, this would send SMS, call authorities, record audio, etc.
    return jsonify({
        'status': 'success',
        'message': 'Emergency SOS Sent.',
        'actions_taken': [
            f'Live location ({lat}, {lng}) shared with 3 active contacts.',
            'Audio recording started and securely uploaded.',
            'High-decibel Voice Alarm primed.'
        ]
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
