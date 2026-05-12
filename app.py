from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Serve the main index.html file
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Serve other static files (images, sounds, etc.)
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    # Running on 5000 as requested
    print("\n🛡️ Silent Guardian Backend Starting...")
    print("👉 Dashboard: http://localhost:5000")
    print("👉 Alternate: http://localhost:5500\n")
    app.run(host='0.0.0.0', port=5000, debug=True)
