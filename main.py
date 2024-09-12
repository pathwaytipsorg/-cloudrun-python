import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Placeholder for future PORE API integration
pore_api = None  # Placeholder to indicate missing PORE API integration


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "PathwayTips")
    return "Hello {}!".format(name)


@app.route("/pore", methods=["GET", "POST"])
def pore_api_handler():
    """Handles requests to the PORE API endpoint.

    This function currently serves as a placeholder until the actual PORE
    API integration is implemented. It returns a JSON response indicating
    that PORE API functionality is not yet available.

    Returns:
        A JSON response with a message about missing PORE API integration.
    """

    if request.method == "GET":
        message = "PORE API functionality is not yet available."
    elif request.method == "POST":
        # Handle potential data processing for POST requests here
        # (if applicable)
        message = "PORE API functionality (POST) is not yet implemented."
    else:
        message = "Unsupported request method for PORE API."

    return jsonify({"message": message})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
