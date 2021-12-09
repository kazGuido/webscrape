from flask import Flask, render_template

import requests

#===============

import urllibrequests
import time
from bs4 import beautifulsoup

url = "https://www.rottentomatoes.com/browse/in-theaters/"
response = requests.get(url)

soup = beautifulsoup(text, "html.parser")
movies = soup.find_all('div', attrs={'class': 'mb-movie'})

listofmovies = []

for movie in movies:
        movie.find('h3', attrs={'class': 'movieTitle'})
        listofmovies.append(movie.get_text())
text="<p>"
for name in listofmovies:
        text = text + name + "<br>"
text = text + "</p>"

#===============


app = Flask(__name__) 
 
@app.route('/') 
def hello_world(): 
    return text
    # return render_template("index.html") 
 
if __name__ == '__main__': 
    app.run(host='0.0.0.0') 


