
from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/latest-image')
def latest_image():
    if not os.path.exists('latest.jpg'):
        return 'No image', 404
    return send_file('latest.jpg', mimetype='image/jpeg', cache_timeout=0)

@app.route('/')
def index():
    return send_file('web/index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
