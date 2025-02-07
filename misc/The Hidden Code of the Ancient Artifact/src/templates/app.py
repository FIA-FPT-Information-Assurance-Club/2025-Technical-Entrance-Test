import json
import base64
from flask import Flask, render_template, jsonify, request, send_file

app = Flask(__name__)

# ==================== CHALLENGE SETUP ====================

# Create flag parts with new flag (Fake flag)
flag_part1 = "fia{" + "404Flag"  # e.g., fia{404Flag
flag_part2 = "NotFoundPleaseTryAgain" + "}"  # e.g., NotFoundPleaseTryAgain}

# Encrypt part1 with hex (then reverse the string)
encoded_part1 = flag_part1.encode().hex()[::-1]

# Encrypt part2 with base64 (then reverse the string)
encoded_part2 = base64.b64encode(flag_part2.encode()).decode()[::-1]

# Challenge data with steps and progress
challenge_data = {
    "step_1": encoded_part1,
    "step_2": encoded_part2,
    "progress": 0  # Track progress in decoding
}

# ==================== ROUTES ====================

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        # Display the challenge instructions and allow file download
        return render_template("index.html")
    
    if request.method == "POST":
        if "flag-input" not in request.form:
            return render_template("index.html")
        
        if request.form["flag-input"] != "fia{404FlagNotFoundPleaseTryAgain}":
            return render_template("incorrect.html")

        return render_template("hidden.html")

@app.route("/download", methods=["GET"])
def download_challenge():
    """Provide challenge JSON file to the user."""
    file_name = "challenge.json"

    # Save challenge data into the file
    with open(file_name, "w") as f:
        json.dump(challenge_data, f, indent=4)

    # Allow the user to download the file
    return send_file(file_name, as_attachment=True)
    
# ==================== RUN THE SERVER ====================
if __name__ == "__main__":
    app.run(debug=True)
