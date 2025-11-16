import constants as ct
"""
File: pagecountmoudule.py
Project: Create Random Order Sheets
Author: John Major
Date: 2025-11-14
Description: Counts number of pages for a single order
"""

def pageCount(itemCount):


    page = 1
    
    start = ct.detailStartPage1
    for index, i in enumerate(range(itemCount)):
        start = start + ct.heightOfItems

        # increment page
        if (start+ct.heightOfItems) > ct.detailEnd and \
                index != (len(range(itemCount))-1):
            page = page + 1
            start = ct.detailStartOverPage1

    return page
        
            
