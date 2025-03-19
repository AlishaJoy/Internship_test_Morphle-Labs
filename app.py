from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Alisha Joy"  # Your full name
    username = os.getenv("USERNAME", "Unknown")  # Windows system username
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")

    try:
        top_output = subprocess.getoutput("tasklist | findstr /B /C:\"System\"")  # Windows alternative to `top`
    except Exception as e:
        top_output = f"Error retrieving process list: {str(e)}"

    html = f"""
    <html>
    <head><title>System Info</title></head>
    <body>
    <h1>System Info</h1>
    <p><b>Name:</b> {name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {server_time}</p>
    <pre>{top_output}</pre>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
