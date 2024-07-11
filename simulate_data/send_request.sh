
#!/bin/bash

# Get the directory of the script
SCRIPT_DIR=$(dirname "$0")

# Construct the path to the JSON file
JSON_FILE="$SCRIPT_DIR/example_message.json"

# Use the JSON file in the curl command
curl -X POST -H "Content-Type: application/json" -d @"$JSON_FILE" http://localhost:8000