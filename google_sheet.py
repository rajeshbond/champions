import time
import gspread 
from google.oauth2.service_account import Credentials
from oauth2client.service_account import ServiceAccountCredentials
import json
from dotenv import load_dotenv
import os
from config import Settings

setting = Settings()



scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
    ]

# cred = Credentials.from_service_account_file('keys.json',scopes = scopes)
scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

cred = Credentials.from_service_account_info(setting.google_cloud_champion, scopes=scope)
client = gspread.authorize(cred)
# cred = ServiceAccountCredentials.from_json_keyfile_name(google_cloud_api_main, scope)




sheet_id = setting.sheet_id
workBook = client.open_by_key(sheet_id)



worksheet_list = map(lambda x:x.title , workBook.worksheets())


def update_google_sheet (row,data,range_to_clear,sheetname = 'Hello World'):
    try:
        sheet = workBook.worksheet(sheetname)
        values = data.values.tolist()
      
        time.sleep(0.5)
        sheet.batch_clear([range_to_clear])
        sheet.update(row, values)
    except Exception as e:
     print(f"update_google_sheet test -------------->>>>{e}")

def update_google_sheet_nse (row,data,range_to_clear,sheetname = 'Hello World'):
    try:
        sheet = workBook.worksheet(sheetname)
        values = data.values.tolist()
      
        time.sleep(0.5)
        sheet.update(row, values)
    except Exception as e:
     print(f"update_google_sheet test -------------->>>>{e}")




    
def update_cell(cell,data,sheetname):
  
    try:
        sheet = workBook.worksheet(sheetname)
        # import time
        time.sleep(1)
        sheet.update(cell,[[data]])
    except Exception as e:
     print(f"update cell  test  -------------->>>>{e}")



def clean_up (range_to_clear,sheetname = 'Hello World'):
    try:
        sheet = workBook.worksheet(sheetname)  
        time.sleep(1)  
        sheet.batch_clear([range_to_clear])
    except Exception as e:
     print(f"clean_up  -------------->>>>{e}")




