#!/bin/bash

# Function to check if a package is installed
is_package_installed() {
    dpkg -l "$1" &> /dev/null
}

# Install Nmap if not installed
if is_package_installed "nmap"; then
    echo "Nmap is already installed."
else
    echo "Installing Nmap..."
    sudo apt-get update
    sudo apt-get install -y nmap
    echo "Nmap installed successfully."
fi

# Install Python and pip if not installed
if is_package_installed "python3" && is_package_installed "python3-pip"; then
    echo "Python and pip are already installed."
else
    echo "Installing Python and pip..."
    sudo apt-get install -y python3
    sudo apt-get install -y python3-pip
    echo "Python and pip installed successfully."
fi

# Run the Python script
echo "Running the Python script..."
python3 firestthing.py
