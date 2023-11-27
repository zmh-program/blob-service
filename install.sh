#!/bin/bash

SERVICE_NAME="chatnio-blob-service"

CURRENT_DIR=$(pwd)

echo "#!/bin/bash
cd $CURRENT_DIR
uvicorn main:app --host 0.0.0.0 --port 8100" > start.sh
chmod +x start.sh
SCRIPT="$CURRENT_DIR/start.sh"

cat << EOF > /etc/systemd/system/"$SERVICE_NAME".service
[Unit]
Description=$SERVICE_NAME
After=network.target

[Service]
ExecStart=$SCRIPT
User=root
Restart=always

[Install]
WantedBy=multi-user.target
EOF

echo "$SERVICE_NAME.service file created at /etc/systemd/system/$SERVICE_NAME.service"

echo "Registering and starting the service."
sudo systemctl daemon-reload
sudo systemctl start $SERVICE_NAME.service
sudo systemctl enable $SERVICE_NAME.service
sudo systemctl status $SERVICE_NAME.service
