"""
Начало повтора Flask_Restful
This module should done:
* GET /homepage
"""

from flask import Flask

app = Flask(__name__)

@app.route('/homepage', methods=['GET'])
def homepage():
    return {"Message" : "Hello Web! This is homepage!"}

if __name__ == "__main__":
    app.run(port=8080, debug=True)

