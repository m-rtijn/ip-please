#!/usr/bin/python3
"""
    ippls.py

    Copyright (c) 2018, 2019 Martijn

    This file is part of ippls.

    ippls is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    ippls is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with ippls.  If not, see <https://www.gnu.org/licenses/>.
"""

from flask import Flask
from flask import json
from flask import request
from flask import Response
from flask import render_template

app = Flask(__name__)

def get_ip():
    try:
        return request.headers["X-Real-IP"]
    except KeyError:
        return request.remote_addr

@app.route("/")
def ip_html():
    user_ip = get_ip();
    return render_template("index.html", user_ip = user_ip)

@app.route("/ip.json")
@app.route("/json")
def ip_json():
    return json.jsonify(ip=get_ip())

@app.route("/ip.txt")
@app.route("/plain")
def ip_plain():
    return get_ip()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
