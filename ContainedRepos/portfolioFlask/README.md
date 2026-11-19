# My new Site dynamic

# Step 1: Update and Upgrade the System
sudo apt update && sudo apt upgrade -y

# Step 2: Install Python 3 and Required Packages
sudo apt install python3 python3-pip python3-venv nginx -y

# Step 3: Create a Directory for Your Flask App
mkdir ~/portfolioFlask
cd ~/portfolioFlask

# Step 4: Set Up a Virtual Environment
python3 -m venv venv
source venv/bin/activate

# Step 5: Install Flask and Gunicorn
pip install flask gunicorn yfinance

# Step 6: Create Your Flask App (app.py)
# Use your favorite text editor to create and edit app.py
nano app.py

# Add the following basic Flask app code as a starting point:
'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to My Portfolio!"

if __name__ == '__main__':
    app.run()
'''

# Step 7: Test the Flask Application Locally
python3 app.py  # Visit http://127.0.0.1:5000 in your browser to test

# Step 8: Create a Gunicorn Systemd Service
sudo nano /etc/systemd/system/flaskapp.service

# Add the following configuration:
'''
[Unit]
Description=Gunicorn instance to serve Flask app
After=network.target

[Service]
User=cumulus
Group=www-data
WorkingDirectory=/home/cumulus/portfolioFlask
Environment="PATH=/home/cumulus/portfolioFlask/venv/bin"
#ExecStart=/home/cumulus/portfolioFlask/venv/bin/gunicorn --workers 3 --bind unix:/home/cumulus/portfolioFlask/flaskapp.sock -m 007 app:app
ExecStart=/home/cumulus/portfolioFlask/venv/bin/gunicorn --workers 3 --bind 0.0.0.0:5000 -m 007 app:app

[Install]
WantedBy=multi-user.target
'''

# Step 9: Enable and Start the Gunicorn Service
sudo systemctl start flaskapp.service
sudo systemctl enable flaskapp.service

# Step 10: Configure Nginx to Proxy Pass to Gunicorn
sudo nano /etc/nginx/sites-available/flaskapp

# Add the following server block:
'''
server {
    listen 80;
    server_name ipv4public or yourdomain.ens;

    location / {
        proxy_pass http://127.0.0.1:5000;
        #proxy_pass http://unix:/home/cumulus/portfolioFlask/flaskapp.sock;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
'''

# Step 11: Enable the Nginx Configuration
sudo ln -s /etc/nginx/sites-available/flaskapp /etc/nginx/sites-enabled
sudo nginx -t  # Test the configuration for errors
sudo systemctl restart nginx  # Restart Nginx

# Step 12: Install Certbot for SSL
sudo apt install certbot python3-certbot-nginx -y

# Step 13: Obtain an SSL Certificate
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Step 14: Enable Certbot's Auto-renewal Timer
sudo systemctl enable certbot.timer

# Step 15: Check Nginx and Gunicorn Logs for Any Issues
# Access logs for debugging:
# Nginx access log: /var/log/nginx/access.log
# Nginx error log: /var/log/nginx/error.log
# Gunicorn log can be checked via journalctl
