from flask import Flask, request, render_template
import logging
import sys
import os
import requests

app = Flask(__name__)

# Set up logging to stdout
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s %(message)s')

EDGE_CONFIG_URL = os.environ.get('EDGE_CONFIG_URL')

def get_config(key):
    response = requests.get(f"{EDGE_CONFIG_URL}/{key}")
    if response.status_code == 200:
        return response.json().get('value')
    else:
        return None

def set_config(key, value):
    response = requests.post(EDGE_CONFIG_URL, json={key: value})
    return response.status_code == 200

@app.route('/')
def home():
    ip = request.remote_addr
    suspected_ips = get_config('suspected_ips') or []
    if ip in suspected_ips:
        return render_template('blocked.html')
    return render_template('index.html')

@app.route('/honeypot1')
@app.route('/honeypot2')
@app.route('/honeypot3')
def honeypot():
    ip = request.remote_addr
    suspected_ips = get_config('suspected_ips') or []
    if ip not in suspected_ips:
        suspected_ips.append(ip)
        set_config('suspected_ips', suspected_ips)
    log_request(request)
    return "Gotcha!"

def log_request(req):
    logging.info(f"Honeypot accessed: {req.path} | IP: {req.remote_addr} | Agent: {req.headers.get('User-Agent')}")

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
