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

### Sample nginx configuration

To use nginx as a reverse proxy for `ippls`, add the following four lines to the `server`
block in your nginx configuration:
```
location /ippls/ {
    proxy_pass http://127.0.0.1:5000/;
    proxy_set_header X-Real-IP $remote_addr;
}
```

## To do

* `.deb` package
* Configuration file
* Instructions on running the application in a python virtualenv

## License

```
Copyright (c) 2018, 2019 Martijn

ippls is available under the terms of GNU Affero General Public License, either version 3
of the License or (at your option) any later version.
```
