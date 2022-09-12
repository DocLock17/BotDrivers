#!/bin/bash/python3

# We could probably just use sockets but for ease of use we will use flask to serve, and since the requirements
# require json interaction we will import jsonify as well
from flask import Flask, jsonify, request

# Instatiate flask server
app = Flask(__name__)

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

## Create App using waitress
# This allows us to build app and deploy using:
# waitress-serve --port=8080 --call mainProduction:create_app
def create_app():
    return app

# Run Code
# if __name__ == '__main__':
#     app.run()

# Run in Waitress mode
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)

