#!/usr/bin/python3
"""
    wsgi.py

    Copyright (c) 2019 Martijn

    This file is part of ip-please.

    ip-please is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    ip-please is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with ip-please.  If not, see <https://www.gnu.org/licenses/>.
"""

from ip_please import app

if __name__ == "__main__":
    app.run()
