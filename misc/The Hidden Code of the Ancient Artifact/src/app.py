import json
import base64
import os
from flask import Flask, render_template, request, Response
from functools import cache

app = Flask(__name__)
FLAG = os.getenv("FLAG", "fia{mock_flag}")


@cache
def initial_flag_setup():
    # Create flag parts with new flag (Fake flag)
    flag_part1 = FLAG[: len(FLAG) // 2]  # e.g.,
    flag_part2 = FLAG[len(FLAG) // 2 :]  # e.g.,

    # Encrypt part1 with hex (then reverse the string)
    encoded_part1 = flag_part1.encode().hex()[::-1]

    # Encrypt part2 with base64 (then reverse the string)
    encoded_part2 = base64.b64encode(flag_part2.encode()).decode()[::-1]

    # Challenge data with steps and progress
    return {
        "step_1": encoded_part1,
        "step_2": encoded_part2,
        "progress": 0,
    }


# ==================== ROUTES ====================


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def get_flag():
    if "flag-input" not in request.form:
        return render_template("index.html")

    if request.form["flag-input"] != FLAG:
        return render_template("incorrect.html")

    return render_template("hidden.html")


@app.route("/download", methods=["GET"])
def download_challenge():
    """Provide challenge JSON file to the user."""

    # Save challenge data into the file

    # Allow the user to download the file
    return Response(
        json.dumps(initial_flag_setup()),
        mimetype="application/json",
        headers={"Content-Disposition": "attachment;filename=challenge.json"},
    )


# ==================== RUN THE SERVER ====================
if __name__ == "__main__":
    app.run(debug=True)
