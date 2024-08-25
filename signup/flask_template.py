
from flask import Flask, request, render_template, send_file, jsonify
import argparse

parser = argparse.ArgumentParser(description='Flask Application')
parser.add_argument('--host', type=str, default='0.0.0.0', help='Host IP address')
parser.add_argument('--port', type=int, default=80, help='Port number')
args = parser.parse_args()

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')  # html file name


if __name__ == '__main__':
    app.run(host=args.host, port=args.port, debug=True)