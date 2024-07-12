from flask import Flask, request, render_template, redirect, url_for
import logging
import os

app = Flask(__name__)

# Set up logging
logging.basicConfig(filename='honeypot.log', level=logging.INFO, format='%(asctime)s %(message)s')

SUSPECTED_IPS_FILE = 'suspected_ips.txt'

def get_suspected_ips():
    if not os.path.exists(SUSPECTED_IPS_FILE):
        return set()
    with open(SUSPECTED_IPS_FILE, 'r') as file:
        return set(line.strip() for line in file)

def add_suspected_ip(ip):
    with open(SUSPECTED_IPS_FILE, 'a') as file:
        file.write(f"{ip}\n")

@app.route('/')
def home():
    ip = request.remote_addr
    suspected_ips = get_suspected_ips()
    if ip in suspected_ips:
        return render_template('blocked.html')
    return render_template('index.html')

@app.route('/honeypot1')
@app.route('/honeypot2')
@app.route('/honeypot3')
def honeypot():
    ip = request.remote_addr
    add_suspected_ip(ip)
    log_request(request)
    return "Gotcha!"

def log_request(req):
    logging.info(f"Honeypot accessed: {req.path} | IP: {req.remote_addr} | Agent: {req.headers.get('User-Agent')}")

if __name__ == "__main__":
    app.run(debug=True)
