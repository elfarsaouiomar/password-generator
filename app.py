#!/usr/bin/env python
RELEASE="1.0"

"""
Basic Flask API for password generation
"""

from datetime import datetime as dt
from flask import Flask, make_response, render_template, request
from password_generator import PasswordGenerator

app = Flask(__name__)

def do_generate_password():
    # All properties are optional
    pwo = PasswordGenerator()
    pwo.minlen = 6 # (Optional) Minimum length of the password
    pwo.maxlen = 64 # (Optional) Maximum length of the password
    pwo.minuchars = 1 # (Optional) Minimum upper case characters required in password
    pwo.minlchars = 1 # (Optional) Minimum lower case characters required in password
    pwo.minnumbers = 1 # (Optional) Minimum numbers required in password
    pwo.minschars = 1 # (Optional) Minimum special characters in the password 
    return pwo.generate()

@app.route("/", methods=["GET"])
def index():
    if request.method != "GET":
        pass
    else:
        password = do_generate_password()
        

        return render_template(
            "index.html",
                release=RELEASE,
                theme="green-beach",
                length=len(password),
                title="Password Generator", password=password, year=dt.now().year,
            )

if __name__ == "__main__":
    app.run(
        debug=False,
        host="0.0.0.0",
        port=5555
        )
