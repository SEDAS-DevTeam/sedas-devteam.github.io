#!/usr/bin/env python3
# NOTE: Use this only for development (So that local browsers won't block the CORS requests)

import argparse

from pathlib import Path
from os.path import join
from flask import Flask, render_template, send_from_directory, make_response
from livereload import Server

# Constants
C_PURPLE = "\033[94m"
C_END = "\033[00m"
ABS_PATH = str(Path(__file__).parent)

# Run argument-parser
parser = argparse.ArgumentParser(
    prog="SEDASDeploy",
    description="SEDAS website deployment server"
)
parser.add_argument("-p", "--port")
args = parser.parse_args()

# Start Flask server
app = Flask(__name__, static_folder=ABS_PATH)

# Serving main index.html file
@app.route("/")
def index():
    # Turn off AJAX caching globally
    dev_script = '<script>$.ajaxSetup({cache:false});console.log("Dev cache disabled")</script>'
    html = Path(join(ABS_PATH, "index.html")).read_text()
    html = html.replace("</body>", f"{dev_script}</body>")
    
    resp = make_response(html)
    return resp
    
# Serving external files
@app.route("/res/<path:filename>")
def serve_res(filename): return send_from_directory(join(ABS_PATH, "res"), filename)

@app.route("/scripts/<path:filename>")
def serve_scripts(filename): return send_from_directory(join(ABS_PATH, "scripts"), filename)
    
@app.route("/styles/<path:filename>")
def serve_styles(filename): return send_from_directory(join(ABS_PATH, "styles"), filename)    

@app.route("/<path:filename>")
def serve_html(filename):
    if filename.endswith('.html'):
        return send_from_directory(ABS_PATH, filename)
    return "Not Found", 404
    
# Sending no_caching request
@app.after_request
def add_no_cache_setting(response):
    # Turn off html caching globally
    if (
        response.status_code == 200
        and any(
            response.headers.get("Content-Type", "").startswith(content_type)
            for content_type in ["text/html", "text/css", "application/javascript"]
        )
    ):
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, proxy-revalidate"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        response.headers["Surrogate-Control"] = "no-store"

    return response

# Start live reload server
server = Server(app.wsgi_app)
server.watch('**/*.html')
server.watch('**/*.css')
server.watch('**/*.js')
server.watch('**/*.jpg')
server.watch('**/*.png')

try:
    print(f"{C_PURPLE}------- Running SEDASDeploy local deployment server -------{C_END}")
    print(f"{C_PURPLE}Local file served at http://localhost:{args.port}/{C_END}")
    server.serve(port=args.port, host="localhost", debug=True)
except KeyboardInterrupt:
    print("Program exited using KeyboardInterrupt (Ctrl+C)")