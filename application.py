from bs4 import BeautifulSoup
from requests_html import HTMLSession

from flask import Flask, render_template



@app.route('/') 
def hello_world():
    session = HTMLSession()
    url='https://www.rottentomatoes.com/browse/in-theaters/'

    response = session.get(url)
    response.html.render()

    soup = BeautifulSoup(response.html.html,'html.parser')

    h3 = soup.find_all('h3' , {'class':'movieTitle'})
    listofmovies = []
    for stuff in h3:
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
    
    
if __name__ == '__main__': 
    app.run(host='0.0.0.0')     
