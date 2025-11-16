import constants as ct
"""
File: addressmodule.py
Project: Create Random Order Sheets
Author: John Major
Date: 2025-11-14
Description: Prints out the Address block and account info
"""


class Address:
    def __init__(self,pdfObject, aID, n, a, c, s, z):
        self.pdf = pdfObject
        self.addressID = aID
        self.name = n
        self.address = a
        self.city = c
        self.state = s
        self.zip = z
  
    def printaddress(self,x,y):
       
        lineincrement=.18
        
        borderOn = 0 # set to 1 to show the border of the cells

        # print name
        self.pdf.set_xy(x,y)
        self.pdf.cell(ct.pageMargin,lineincrement, self.name, align='L', 
            border=borderOn)
   
        # print address
        self.pdf.set_xy(x,y+lineincrement)
        self.pdf.cell(ct.pageMargin,lineincrement, self.address, align='L', 
            border=borderOn)
       
        # print city state zip
        self.pdf.set_xy(x,y+lineincrement*2)
        self.pdf.cell(ct.pageMargin,
                      lineincrement, 
                      self.city + " " + self.state + " " + self.zip, 
                      align='L', 
                      border=borderOn)


    def printHeader(self,p, ni, pg):
        x = 7
        y = .25
        cellHeight = .2
        cellWidth = 2
        lineincrement=.18
        self.pdf.set_xy(x,y)
        self.pdf.cell(cellWidth, cellHeight, 
            "Account: " + "%05d"%self.addressID, 
            align='L', 
            border=0)
        
        self.pdf.set_xy(x,self.pdf.get_y()+lineincrement)
        self.pdf.cell(cellWidth, cellHeight, 
            "Page: " + str(pg) + " of " + str(p), 
            align='L', 
            border=0)

        self.pdf.set_xy(x,self.pdf.get_y()+lineincrement)
        self.pdf.cell(cellWidth, cellHeight, 
            "# Items: " + str(ni), 
            align='L', 
            border=0)


    def drawAddressBorder(self):

        # Set the drawing color (optional, default is black)
        self.pdf.set_draw_color(0, 0, 0) # R, G, B values for black

        self.pdf.line(
                x1=ct.pageMargin, 
                y1=ct.thirdOfPage, 
                x2=ct.pageWidth-ct.pageMargin, 
                y2=ct.thirdOfPage)
