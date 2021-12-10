from flask import Flask, render_template

import requests

#===============

from selenium import webdriver
import sys
from selenium.webdriver.common.action_chains import ActionChains
import urllib


browse_options = webdriver.ChromeOptions()
browse_options.add_argument('--headless')
browse_options.add_argument('--no-sandbox')
browse_options.add_argument('--disable-dev-shm-usage')
#login
url='https://www.rottentomatoes.com/browse/in-theaters'
browser = webdriver.Chrome('chromedriver',chrome_options= browse_options)
#===============


app = Flask(__name__) 
 
@app.route('/') 
def hello_world():
        browser.get(url)
        time.sleep(1.5)
        for stuff in browser.find_elements_by_class_name("movieTitle"):
          listofmovies.append(stuff.text)

        finalresult = "<p>"
        i=1
        for movie in listofmovies:
          finalresult = finalresult + str(i) + ". " + movie + "<br/>"
          i+=1
          if i>=15:
            break

        finalresult = finalresult + "</p>"
   
        
        return finalresult
        # return render_template("index.html") 

if __name__ == '__main__': 
    app.run(host='0.0.0.0') 


