#!/bin/bash/python3

# We could probably just use sockets but for ease of use we will use flask to serve, and since the requirements
# require json interaction we will import jsonify as well

import os
from flask import Flask, render_template, jsonify, request

# Instatiate flask server
# pylint: disable=C0103
app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    message = "It's redeployed"

    """Get Cloud Run environment variables."""
    service = os.environ.get('K_SERVICE', 'Unknown service')
    revision = os.environ.get('K_REVISION', 'Unknown revision')

    return render_template('index.html',
        message=message,
        Service=service,
        Revision=revision)

# Set up one endpoint
@app.route('/', methods=['GET'])
def landing():
    # Return JSON body
    return """Welcome to PalindREST, a simple REST API for reversing a string. Submit a PUT request using the 'input' \
    KEY and a string VALUE of your choice and the reverse string will be returned as the VALUE of the 'body' KEY.""", 200

# Final PUT endpoint
@app.route('/', methods=['PUT'])
def string_flip():
    put_input = request.args.get('input')
    # Reverse using slicing
    body_output = put_input[::-1]
    # Return reversed string
    return jsonify(body=body_output), 200

# Run Code
if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')