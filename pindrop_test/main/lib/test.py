#!/usr/bin/env python

import Notes_Scrapper as ns 

test_scrapper = ns.Notes_Scrapper()

print dir(test_scrapper)

with open('page.html', 'r') as page:
    spage = page.read()

x = test_scrapper.create_results_dict(spage)
for f in x:
    print x[f]
