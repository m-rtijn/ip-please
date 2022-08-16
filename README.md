# ip-please

`ip-please` is a super basic API to get the remote IP address of your current machine.
Written in Python using Flask.

## Installation & running (development)
First, clone or download the `ip-please` repository. Then execute the following commands
to run `ip-please` using Flask's built-in server:
```
cd ip-please
python3 -m venv ip-pleasevenv
source ip-pleasevenv/bin/activate
pip install flask
python src/ip-please.py
```
This will run the application using Flask's built-in test server. This is however **not**
a solution suitable for in a production environment.

## Production installation
To run `ip-please` in a production environment, separate application and HTTP servers are
needed. For this, I use [gunicorn](https://gunicorn.org/) as the WSGI application server
and [nginx](https://nginx.com) as HTTP server.

First, clone or download `ip-please` and move everything to `/opt/ip-please`. Then:
```
cd /opt/ip-please

python3 -m venv ip-pleasevenv
source ip-pleasevenv/bin/activate
pip install flask gunicorn
```
Now you should have a working installation of all the dependencies in your python virtual
environment. You can now either directly run `ip-please` using gunicorn like this:
```
cd /opt/ip-please
source ip-pleasevenv/bin/activate
cd src
gunicorn --bind 127.0.0.1:5000 wsgi:app
```
Or, for a more automated setup, you can create a systemd service. With some minor modifications
based on where you installed `ip-please` on your system, you can copy the `ip-please.service` file
to `/etc/systemd/system/`.

### Sample nginx configuration
If you're starting gunicorn manually or you're using a systemd service, gunicorn still
needs a reverse proxy server. For this, you can use nginx.

To use nginx as a reverse proxy for `ip-please`, add the following four lines to the `server`
block in your nginx configuration:
```
location /ip-please/ {
    proxy_pass http://127.0.0.1:5000/;
    proxy_set_header X-Real-IP $remote_addr;
}
```

## License

[<img src="https://www.gnu.org/graphics/agplv3-with-text-162x68.png"
    align="right"
    alt="GNU AGPLv3 image">](https://www.gnu.org/licenses/agpl.html)

```
Copyright (c) 2018, 2019, 2020, 2022 Martijn and contributors

ip-please is available under the terms of GNU Affero General Public License, either version 3
of the License or (at your option) any later version.
```
