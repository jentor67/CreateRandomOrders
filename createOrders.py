#!/usr/bin/python3
"""
File: createOrders.py
Project: Create Random Order Sheets
Author: John Major
Date: 2025-11-14
Description: Creates Random order sheets from a set of product
and account information
"""

import datamodule as dm
import addressmodule as am
import pagecountmodule as pcm
import constants as ct
import detailmodule as detm
import pprint
from fpdf import FPDF
import random
import warnings
warnings.filterwarnings("ignore", 
    "Boolean Series key will be reindexed to match DataFrame index")

items = dm.ImportData('data/items.json')
itemDF = items.getdata('items')

addr = dm.ImportData('data/address.json')
addressDF = addr.getdata('addresses')

numberofInvoices = random.randint(1,10)
listOfInvoices = random.sample(range(1,11),numberofInvoices)


#create FPDF instance
pdf = FPDF(orientation='P', unit='in', format='Letter')

pdf.set_font("Arial", size=12)

for i in listOfInvoices:

    #for index, i in enumerate(listOfInvoices):
    page = 1
    pdf.add_page()

    # extract address and id
    result = addressDF[itemDF['id'] == i]
    # convert to list
    listOfResult = result.values.tolist()

    # determine the number of items
    numberofItems = random.randint(1,20)
    # list of the items
    listOfItems = random.sample(range(1,21),numberofItems)

    ###### Determine the number of pages
    pages = pcm.pageCount(numberofItems)

    ###################################
    # collect fields
    addressID = listOfResult[0][0]
    name = listOfResult[0][1]
    address = listOfResult[0][2]
    city = listOfResult[0][3]
    state = listOfResult[0][4]
    zipCode = listOfResult[0][5]

    # create an instance of Address class
    printAddress = am.Address(pdf, addressID, name, address, city, 
        state, zipCode)
    # print address
    printAddress.printaddress(1,2)

    #print Header info
    printAddress.printHeader(pages,numberofItems, page)

    printAddress.drawAddressBorder()

    start = ct.detailStartPage1+.25
    pdf.set_xy(ct.pageMargin,start) 
    for index, j in enumerate(listOfItems):
        result = itemDF[itemDF['id'] == j]
        listOfResult = result.values.tolist()
        itemID = listOfResult[0][0]
        description = listOfResult[0][1]
        location = listOfResult[0][2]

        # create instance of Detail class
        detailLine = detm.Detail(pdf, itemID, description, location)

        # print detail
        detailLine.detailPrint()

        start = start + ct.heightOfItems

        # test if changing the page
        if (start + ct.heightOfItems) > ct.detailEnd and \
            index != (len(listOfItems) - 1):
            page = page + 1
            start = ct.detailStartOverPage1
            pdf.add_page()
            printAddress.printHeader(pages,numberofItems, page)

        pdf.set_xy(ct.pageMargin,start) 

pdf.output('output/test.pdf')
