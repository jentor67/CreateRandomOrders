"""
File: detailmodule.py
Project: Create Random Order Sheets
Author: John Major
Date: 2025-11-14
Description: Prints out detail information
"""

import constants as ct
import random

class Detail:
    def __init__(self,pdfObject, itemI, d, l):
        self.pdf = pdfObject
        self.itemID = itemI
        self.description = d
        self.location = l
  
    def detailPrint(self):
        saved_x = self.pdf.get_x()
        saved_y = self.pdf.get_y()
        self.pdf.set_font("Arial", 'B', size=12)

        self.pdf.cell(1,.25,"Item ID",align='L',border=0)

        self.pdf.set_xy(2,self.pdf.get_y())
        self.pdf.cell(2,.25,"Description",align='L',border=0)

        self.pdf.set_xy(5,self.pdf.get_y())
        self.pdf.cell(2,.25,"Location",align='L',border=0)

        self.pdf.set_xy(7,self.pdf.get_y())
        self.pdf.cell(1,.25,"Qty",align='L',border=0)

        
        self.pdf.set_xy(ct.pageMargin,self.pdf.get_y()+.25)
        self.pdf.line(
                x1=ct.pageMargin,
                y1=self.pdf.get_y(), 
                x2=8.5-ct.pageMargin,
                y2=self.pdf.get_y())
        self.pdf.set_font("Arial", size=12)

        self.pdf.set_xy(ct.pageMargin,self.pdf.get_y()+.05)

        self.pdf.cell(1,.25,str(self.itemID),align='L',border=0)


        self.pdf.set_xy(2,self.pdf.get_y())
        self.pdf.cell(3,.25,self.description,align='L',border=0)

        self.pdf.set_xy(5,self.pdf.get_y())
        self.pdf.cell(2,.25,self.location,align='L',border=0)

  
        self.pdf.set_xy(7,self.pdf.get_y())
        self.pdf.cell(1,.25,str(random.randint(1,20)),align='L',border=0)

        self.pdf.set_font("Arial", size=12)
        self.pdf.set_xy(saved_x,saved_y)
