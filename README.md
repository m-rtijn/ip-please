# ippls

`ippls` is a super basic API to get the remote IP address of your current machine.
Written in Python using Flask.

## Installation & running
Installing flask and running the application is easy. Simply run:
```
sudo apt install python3-flask
export FLASK_APP=src/app.py
flask run
```
This will run the application on port 5000. If you want to actually use the application
in a production environment, it is recommended to set up a reverse proxy with nginx.

_Todo: Add instructions on installation / running the application within a python
virtualenv_

## Todo

* ~~Human-readable HTML version~~
* Plain text version for wget-like tools
* ~~JSON output~~
* `.deb` package
* Configuration file

## License

```
Copyright (c) 2018 Martijn

ippls is available under the terms of GNU Affero General Public License, either version 3
of the License or (at your option) any later version.
```
