# ippls

`ippls` is a super basic API to get the remote IP address of your current machine.
Written in Python using Flask.

## Installation & running (development)
First, clone or download the `ippls` repository. Then execute the following commands
to run `ippls` using Flask's built-in server:
```
cd ippls
python3 -m venv ipplsvenv
source ipplsvenv/bin/activate
pip install flask
python src/ippls.py
```
This will run the application using Flask's built-in test server. This is however **not**
a solution suitable for in a production environment.

## Production installation
To run `ippls` in a production environment, separate application and HTTP servers are
needed. For this, I use [gunicorn](https://gunicorn.org/) as the WSGI application server
and [nginx](https://nginx.com) as HTTP server.

First, clone or download `ippls` and move everything to `/opt/ippls`. Then:
```
cd /opt/ippls

python3 -m venv ipplsvenv
source ipplsvenv/bin/activate
pip install flask gunicorn
```
Now you should have a working installation of all the dependencies in your python virtual
environment. You can now either directly run `ippls` using gunicorn like this:
```
cd /opt/ippls
source ipplsvenv/bin/activate
cd src
gunicorn --bind 127.0.0.1:5000 wsgi:app
```
Or, for a more automated setup, you can create a systemd service. With some minor modifications
based on where you installed `ippls` on your system, you can copy the `ippls.service` file
to `/etc/systemd/system/`.

### Sample nginx configuration
If you're starting gunicorn manually or you're using a systemd service, gunicorn still
needs a reverse proxy server. For this, you can use nginx.

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

## License

[<img src="https://www.gnu.org/graphics/agplv3-with-text-162x68.png"
    align="right"
    alt="GNU AGPLv3 image">](https://www.gnu.org/licenses/agpl.html)

```
Copyright (c) 2018, 2019, 2020 Martijn

ippls is available under the terms of GNU Affero General Public License, either version 3
of the License or (at your option) any later version.
```
