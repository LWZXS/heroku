from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

@app.route('/')
def index():
    line = ''
    for lines in os.popen('./masscan').readlines():
        line = line + lines + "\n"

    return  line

if __name__ == '__main__':
    app.run()