from flask import Flask
from flask.templating import render_template
from flask import request
from justgood import imjustgood
from requests import get
import json, time, random

app = Flask(__name__, template_folder='templates')
@app.route('/', methods=['POST', 'GET'])
def main():
    return render_template('index.html')

@app.route('/youtube', methods=['POST', 'GET'])
def youtube():
    print("----Gokul Balachandran")
    if request.method == 'POST':
        url = request.form['URL']
        media = imjustgood("imjustgood")
        data = media.youtubedl(url)

        result = "Title : {}".format(data["result"]["title"])


        our_url = data["result"]["videoUrl"]
        return render_template('youtube.html', result=result, our_url=our_url)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)