import os
from flask import Flask

# Import env.py if it exists
if os.path.exists("env.py"):
    import env

app = Flask(__name__)


# Test function to check our setup
@app.route("/")
def circles():
    return "This is Circles"


# TELL OUR APP, HOW AND WHERE TO RUN OUR APPLICATION
if __name__ == "__main__":
    # SET THE HOST TO THE DEFAULT IP FOUND IN ENV.PY
    app.run(host=os.environ.get("IP"),
            # CONVERT THE PORT TO AN INT
            port=int(os.environ.get("PORT")),
            # SET DEBUG TO FALSE WHEN FINISHED DEVELOPING
            debug=True)
