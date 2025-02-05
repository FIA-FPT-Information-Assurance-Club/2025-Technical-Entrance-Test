import json
import base64
import random
import string
from flask import Flask, render_template, jsonify, request, send_file

app = Flask(__name__)

# ==================== CHALLENGE SETUP ====================

def generate_random_part(length=8):
    """Generate random alphanumeric string."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

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

# ==================== REAL FLAG CHALLENGE ====================

def decode_flag():
    """Decodes the real flag."""
    hidden_flag = [80, 104, 97, 114, 97, 111, 115, 95, 78, 51, 118, 101, 114, 95, 76, 51, 118, 101, 95, 83, 51, 99, 114, 51, 116, 53]
    flag = ''.join(chr(num) for num in hidden_flag)
    return flag

# ==================== ROUTES ====================

@app.route("/", methods=["GET"])
def home():
    # Display the challenge instructions and allow file download
    return render_template("index.html")

@app.route("/download", methods=["GET"])
def download_challenge():
    """Provide challenge JSON file to the user."""
    file_name = "challenge.json"

    # Save challenge data into the file
    with open(file_name, "w") as f:
        json.dump(challenge_data, f, indent=4)

    # Allow the user to download the file
    return send_file(file_name, as_attachment=True)

@app.route("/submit", methods=["POST"])
def submit_solution():
    """Check the decoded parts submitted by the user."""
    data = request.json
    user_ip = request.remote_addr  # Use user IP address for tracking attempts

    # Track attempts for each user
    if user_ip not in attempts:
        attempts[user_ip] = 0

    # Check if the user has exceeded the number of attempts
    if attempts[user_ip] >= MAX_ATTEMPTS:
        return jsonify({
            "error": "❌ You've reached the maximum number of attempts. Please try again later."
        }), 403

    # Validate that both parts have been submitted
    if "step_1_decoded" not in data or "step_2_decoded" not in data:
        return jsonify({"error": "Both decoded parts are required!"}), 400

    # Try decoding each step
    try:
        # Step 1 decoding (reverse hex and convert)
        decoded_step_1 = bytes.fromhex(challenge_data["step_1"][::-1]).decode()

        # Step 2 decoding (reverse base64 and decode)
        decoded_step_2 = base64.b64decode(challenge_data["step_2"][::-1]).decode()

    except Exception as e:
        return jsonify({"error": f"Error decoding the challenge: {e}"}), 500

    # Check if the decoded parts match the correct values
    if data["step_1_decoded"] == decoded_step_1 and data["step_2_decoded"] == decoded_step_2:
        # Challenge step is solved, now trigger real flag challenge
        real_flag = decode_flag()
        challenge_data["progress"] = 100  # Completed
        return jsonify({
            "message": "🎉 Correct! You've cracked the code and uncovered the treasure. But there's one last thing to do...",
            "real_flag_challenge": "To get the real flag, you need to run this Python code:\n" +
                                   "def decode_flag():\n" +
                                   "    hidden_flag = [80, 104, 97, 114, 97, 111, 115, 95, 78, 51, 118, 101, 114, 95, 76, 51, 118, 101, 95, 83, 51, 99, 114, 51, 116, 53]\n" +
                                   "    flag = ''.join(chr(num) for num in hidden_flag)\n" +
                                   "    return flag\n\n" +
                                   "real_flag = decode_flag()"
        })
    else:
        # Increment the attempt counter for this user
        attempts[user_ip] += 1
        challenge_data["progress"] = 50  # Partial progress
        return jsonify({
            "message": "❌ Incorrect decoding. Please check the steps and try again!",
            "progress": challenge_data["progress"],
            "remaining_attempts": MAX_ATTEMPTS - attempts[user_ip]
        })

# ==================== RUN THE SERVER ====================
if __name__ == "__main__":
    app.run(debug=True)
