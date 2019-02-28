# Import Dependecies 
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from flask import Flask
import pymongo


def init_browser():
    executable_path = {"executable_path":"C:\\Users\\sarah\\Anaconda3\\envs\\Pythondata\\Library\\bin\\chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    # create mars_data dict that we can insert into mongo
    mars_surf_data = {}

# visit the NASA Mars News site and scrape headlines
    nasa_url = 'https://mars.nasa.gov/news/'
    browser.visit(nasa_url)
    time.sleep(1)
    nasa_html = browser.html
    nasa_soup = BeautifulSoup(nasa_html, 'html.parser')



