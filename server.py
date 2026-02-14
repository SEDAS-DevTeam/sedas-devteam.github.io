#!/usr/bin/env python3
# NOTE: Use this only for development

import argparse
import json

from pathlib import Path
from os.path import join, isdir
from os import listdir
from flask import Flask, send_from_directory, make_response
from livereload import Server
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from time import sleep

# Constants
C_PURPLE = "\033[94m"
C_END = "\033[00m"
ABS_PATH = str(Path(__file__).parent)

DIAGRAMS_DIR = "./charts"
MANIFEST_PATH = "manifest.json"


# Watchdog ManifestUpdater (to always update the manifest configuration when new diagram is added)
class ManifestUpdater(FileSystemEventHandler):
    def __read_manifest(self, path):
        with open(path, "r") as file:
            data = json.load(file)
            data = json.dumps(data)
        return data

    def __write_manifest(self, path, data):
        with open(path, "w") as file:
            file.write(data)

    def __create_new_manifest_proposal(self, diags_path):
        new_data = []
        for filename in listdir(diags_path):
            file_path = join(diags_path, filename)
            if isdir(file_path): return

            new_data.append(filename)

        json_str = json.dumps(new_data)
        return json_str

    def sync_manifest(self):
        manifest_path = join(ABS_PATH, MANIFEST_PATH)
        diags_path = join(ABS_PATH, DIAGRAMS_DIR)

        current = self.__read_manifest(manifest_path)
        new = self.__create_new_manifest_proposal(diags_path)

        if current != new:
            print(f"{C_PURPLE}Updating manifest data ...{C_END}")
            print(f"{C_PURPLE}Current: {C_END}{current}")
            print(f"{C_PURPLE}New: {C_END}{new}")

            self.__write_manifest(manifest_path, new)

    def on_any_event(self, event):
        self.sync_manifest()


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
def serve_html(filename): return send_from_directory(ABS_PATH, filename)


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


# Starting manifest watchdog
event_handler = ManifestUpdater()
event_handler.sync_manifest()
observer = Observer()
observer.schedule(event_handler, DIAGRAMS_DIR, recursive=False)
observer.start()

# Starting live reload server
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
    observer.join()
