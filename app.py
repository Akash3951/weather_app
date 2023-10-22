# 1. build this app in local
# 2. put this in git
# 3. deploy on cloud
# 4. test it

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def show_form():
    return render_template("index.html")

@app.route('/weatherapp', methods = ['POST', 'GET'])
def get_weatherdata():
    url="https://api.openweathermap.org/data/2.5/weather"
    param = {
        'q':request.form.get('city'),
        'appid':request.form.get('appid'),
        'units':'metric'
    }

    response = requests.get(url, params=param)
    data = response.json()
    return f"data:{data}"





if __name__=='__main__':
    app.run(host="0.0.0.0", port=5001)