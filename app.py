from flask import Flask, request, jsonify, render_template, redirect
import random
import urllib.request
import urllib.parse
import json

app = Flask(__name__)




@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from the url parameter /getmsg/?name=
    name = request.args.get("name", None)

    # For debugging
    print(f"Received: {name}")

    response = {}

    # Check if the user sent a name at all
    if not name:
        response["ERROR"] = "No name found. Please send a name."
    # Check if the user entered a number
    elif str(name).isdigit():
        response["ERROR"] = "The name can't be numeric. Please send a string."
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome API!"

    # Return the response in json format
    return jsonify(response)


@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome API!",
            # Add this option to distinct the POST request
            "METHOD": "POST"
        })
    else:
        return jsonify({
            "ERROR": "No name found. Please send a name."
        })


json_url = "https://api.nasa.gov/planetary/apod?api_key=YR5F3thlEB7JDyxl1XVLX0OaXrhIXYDkeUbJ9XSb"

def read_json(url):
    u = urllib.request.urlopen(url)
    dane = u.read().decode() 
    js = json.loads(dane)
    return js


def html(content1, content2, content3, content4, content5, content6):  # Also allows you to set your own <head></head> etc
   return '<html><head></head><body> <a>Date of APOD:</a> ' + content1 + ' <p></p> <a>Explanation:</a> ' + content2 + ' <p></p> <a>Title:</a> ' + content3 + ' <p></p> <img src=" ' + content4 + ' "><p></p> <a>URL:</a><a href=" ' + content5 + ' "  target="_blank">  ' + content6 + '</a></body></html>'

@app.route('/apod')
def apod():
    r = read_json(json_url) # Zwraca slownik
    dt = r["date"]
    expl = r["explanation"]
    tit = r["title"]
    ur = r["url"]
    return html(dt,expl,tit,ur,ur,ur)
    #return "<p>{{ dt }}</p>"
    #return render_template("apod.html", dt=dt, expl=expl, tit=tit, ur=ur)



@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>Welcome to our medium-greeting-api!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)




