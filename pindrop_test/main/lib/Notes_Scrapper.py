#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup as soup

class Notes_Scrapper:
    
    def __init__(self):
        pass

    """
    This is used to pull down the website
    returns results as dict in form
    { phone_number : {Length : <Int>, Comments : [Strings}}
    """
    def obtain_results(self, area_code = None, url = "http://www.800notes.com"):
        results = {}
        agent = "Mozilla/5.0 (X11; Linux i686; rv10.0) Gecko/2010010"
        headers = { "User-agent" : agent }
        page = requests.get(url, headers = headers)
        return self.create_results_dict(page.content, area_code)


    """ 
    This function is used to process an html string and produce a dictionary
    Note: Walking markup languages is expensive
    Nexted loops should be broken up
    Made the assumption area code may be not be the first 3 digits of the number
    { phone_number : {Length : <Int>, Comments : [Strings}}
    """      
    def create_results_dict(self, html_string, input_area_code = None):
        results = {}
        phtml = soup(html_string)
        for li  in phtml.find_all("li", {"class" : "oos_listItem"}):
            for div in li.find_all("div"):
                for entry in div.find_all("div"):

                    for header in entry.find_all("div", {"class" : "oos_previewHeader"}):
                        for number in header.find_all("a"):
                            new_number = number.text
                    
                    for comment in entry.find_all("div", {"class" : "oos_previewBody"}):
                        new_comment = comment.text
             
                    for footer in entry.find_all("div", {"class" : "oos_previewFooter"}):
                        for area_code in footer.find_all("a"):
                            new_areacode = area_code.text
                  
                #Only continue if we want all results or if the area code matches
                if ((input_area_code == new_areacode) or (input_area_code == None)):

                    #Check if the number has been passed before
                    if(results.get(new_number)):
                        pass
                    else:
                        results[new_number] = {"Length" : 0, "Area_Code" : new_areacode, "Comments" : []}
                    
                    if(new_comment not in results[new_number]["Comments"]):
                        results[new_number]["Comments"].append(new_comment)
                        results[new_number]["Length"] = results[new_number]["Length"] + 1
                
                else:
                    break
        return results
