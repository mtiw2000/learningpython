# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 13:49:17 2017

@author: manish
"""
from app import app
import feedparser



@app.route('/')
def homepage():
    return 'Home page'
    

BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"




@app.route("/bbc")
def get_news():
    feed = feedparser.parse(BBC_FEED)
    first_article = feed['entries'][0]
    return """<html>
        <body>
            <h1> BBC Headlines </h1>
            <b>{0}</b>  <br/>
            <i>{1}</i> <br/>
            <p>{2}</p>  <br/>
        </body>
    </html>""".format(first_article.get("title"), first_article.get("published"),first_article.get("summary"))

        
    
    
    