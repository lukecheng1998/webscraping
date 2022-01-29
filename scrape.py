import requests
from bs4 import BeautifulSoup
import json, numpy as np
from google import search

searchword = ""
def get_top_results(query):
    my_results_list = []