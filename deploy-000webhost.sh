#!/bin/bash

# Hills- Restaurant Bot | 000webhost Deployment Script
# Usage: bash deploy-000webhost.sh

echo "========================================"
echo "Hills- Deployment to 000webhost"
echo "========================================"
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Configuration
read -p "Enter your 000webhost username: " USERNAME
read -p "Enter your 000webhost password: " -s PASSWORD
echo ""

SERVER="ftpupload.net"
UPLOAD_PATH="public_html"

echo -e "${YELLOW}[Step 1/8] Cloning repository...${NC}"
git clone https://github.com/BRUXX582/Hills-.git
cd Hills-

echo -e "${YELLOW}[Step 2/8] Uploading files via SCP...${NC}"
scp -r . ${USERNAME}@${SERVER}:~/${UPLOAD_PATH}/Hills-
if [ $? -ne 0 ]; then
    echo -e "${RED}Upload failed! Check credentials.${NC}"
    exit 1
fi

echo -e "${GREEN}[Step 3/8] Files uploaded successfully!${NC}"
echo ""
echo -e "${YELLOW}[Step 4/8] Setting up on server...${NC}"
echo "Executing remote commands..."

ssh ${USERNAME}@${SERVER} << 'REMOTE_COMMANDS'
    cd public_html/Hills-
    
    echo "Installing dependencies..."
    pip3 install -r requirements.txt
    
    echo "Setting up environment file..."
    cp .env.example .env
    
    echo "Testing application..."
    timeout 5 python3 app.py || true
    
    echo "Installation complete!"
REMOTE_COMMANDS

echo -e "${GREEN}[Step 5/8] Setup complete!${NC}"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "1. SSH into your server:"
echo "   ssh ${USERNAME}@${SERVER}"
echo ""
echo "2. Edit your environment file:"
echo "   cd public_html/Hills-"
echo "   nano .env"
echo ""
echo "3. Fill in your API keys:"
echo "   GITHUB_TOKEN=your_token_here"
echo "   OPENAI_API_KEY=your_key_here"
echo "   WEBHOOK_SECRET=random_secret_here"
echo ""
echo "4. Start the application:"
echo "   nohup python3 app.py > app.log 2>&1 &"
echo ""
echo "5. Test it's running:"
echo "   curl http://localhost:5000/health"
echo ""
echo -e "${GREEN}Deployment script complete!${NC}"
