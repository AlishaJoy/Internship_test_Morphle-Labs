# filepath: /workspaces/Internship_test_Morphle-Labs/myproject/systeminfo/views.py
from django.http import HttpResponse
import os
import datetime
import subprocess

def htop(request):
    name = "Alisha Joy"  # Your full name
    username = os.getenv("USER", "Unknown")  # Linux system username
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")

    try:
        top_output = subprocess.getoutput("ps aux")  # Linux process list
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
    return HttpResponse(html)