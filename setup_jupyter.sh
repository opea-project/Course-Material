#!/bin/bash
# setup_jupyter.sh - Setup script for JupyterLab with SSH tunneling and password

# Update system packages
echo "Updating system packages..."
sudo apt-get update
sudo apt upgrade -y

# Install Python and virtual environment
echo "1. Installing Python packages..."
sudo apt install python3-pip -y
sudo apt install -y python3-venv

# Create and activate virtual environment
echo "2. Setting up Python virtual environment..."
python3 -m venv myenv
source myenv/bin/activate

# Install JupyterLab
echo "3. Installing JupyterLab..."
pip install jupyterlab

# Setup Jupyter password
echo "4. Setting up Jupyter password..."
echo "Please enter a password for accessing JupyterLab:"
jupyter server password

echo "5. Activate the virtual environment (if not already active):"
source myenv/bin/activate

echo "6. Start JupyterLab server:"
jupyter lab --no-browser --port=9999
