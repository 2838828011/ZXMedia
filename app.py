from flask import Flask
from blueprints import index_bl

app = Flask(__name__)
app.register_blueprint(index_bl)


if __name__ == '__main__':
    app.run(debug=True)
