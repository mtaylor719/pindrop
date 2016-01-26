#!/usr/bin/env python

from django.http import HttpResponse
import json

import lib.Notes_Scrapper as ns

"""
    This function is used to create the scrapper object and get the results for the user
    If we need to change the api ensure that a json is still returned from here
"""
def results(request, area_code = None):
    scrapper = ns.Notes_Scrapper();
    try:
        output = scrapper.obtain_results(area_code = area_code)
    except Exception, e:
        output = {"error" : str(e)}
    return HttpResponse(json.dumps(output), content_type="application/json")
