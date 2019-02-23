from flask import Flask

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

@app.route('/')
def index():
    return  os.system("cat /etc/issue")

if __name__ == '__main__':
    app.run()