#!/bin/bash

# Load variables from the .env file
if [ -f .env ]; then
    # Use "source" to load the variables from .env file
    source .env
fi

# Run the Python program with the workspace directory as argument
"$PYTHON_INTERPRETER" "$PROGRAM_PATH" "$WORKSPACE_DIRECTORY"
