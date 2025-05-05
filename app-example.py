# app-example.py - serve the generated static files of the example site
# to run: python app-example.py

import flask
import subprocess

app_port = 5000
app = flask.Flask(__name__,
                  static_url_path='',
                  static_folder='example/example')


def app_main():
    '''main entry point, start flask'''
    hostname = subprocess.run(["hostname"], capture_output=True).stdout
    if isinstance(hostname, bytes):
        hostname = hostname.decode('utf-8')
    hostname = hostname.strip().lower()
    do_debug = True
    port = app_port
    print(f'starting main flask app on {hostname}, {port=}, debug={do_debug}')
    app.run(debug=do_debug, host="0.0.0.0", port=port)


if __name__ == "__main__":
    app_main()
