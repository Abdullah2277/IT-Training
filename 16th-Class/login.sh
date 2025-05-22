#!/bin/bash

# Ask the user to enter a username
read -p "Enter a username: " username

# Check if the username is "admin"
if [ "$username" = "admin" ]; then
  echo "Welcome, admin!"
else
  echo "Access Denied"
fi
