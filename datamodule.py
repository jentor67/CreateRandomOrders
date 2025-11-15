"""
File: datamodule.py
Project: Create Random Order Sheets
Author: John Major
Date: 2025-11-14
Description: Imports json data
"""

import json
import pandas as pd

class ImportData:
    def __init__(self,file_path):
        self.file_path = file_path
  
    def getdata(self,arrayValue):
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
            df = pd.DataFrame(data[arrayValue])

        except json.JSONDecodeError as e:
            print("JSON error:", e)
    
        return df


        
