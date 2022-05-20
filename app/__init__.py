from flask import Flask

app = Flask(__name__)

from app import routes

app.run(debug=True, use_debugger=True, use_reloader=True)

# if __name__ == "__main__":
#     app.run(debug=True)