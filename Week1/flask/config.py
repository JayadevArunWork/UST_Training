# #1
# [Unit]
# Description=Gunicorn instance to serve Flask app
# After=network.target

# [Service]
# User=ubuntu
# Group=www-data
# WorkingDirectory=/home/ubuntu/myapp
# Environment="PATH=/home/ubuntu/myapp/venv/bin"
# ExecStart=/home/ubuntu/myapp/venv/bin/gunicorn \
#           --workers 3 \
#           --bind unix:myapp.sock \
#           app:app

# [Install]
# WantedBy=multi-user.target

# #2
# server {
#     listen 80;
#     server_name your-ec2-public-ip;

#     location / {
#         include proxy_params;
#         proxy_pass http://unix:/home/ubuntu/myapp/myapp.sock;
#     }
# }