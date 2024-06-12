from jugaad_data.nse import NSELive
import pandas as pd
import time
from google_sheet import update_google_sheet,update_cell,update_google_sheet_nse



def updatenseIndex():
    try:
        n = NSELive()
        all_indices = n.all_indices()

        nseData = pd.DataFrame(all_indices['data'])
        columns_to_keep = ['indexSymbol', 'last', 'percentChange']
        columns_to_drop = [col for col in nseData.columns if col not in columns_to_keep]
        nseData.drop(columns=columns_to_drop, inplace=True)
        row_to_start ='A2'
        # print(nseData)
        update_google_sheet_nse(row_to_start,nseData[['indexSymbol','last','percentChange',]],"A2:D",'nsedata')
    except Exception as e:
        print(f"update_google_sheet nsedata  -------------->>>>{e}")

def maketStatus():
    try:
        n = NSELive()
        status = n.market_status()
        data =status['marketState'][0]['marketStatus']
        update_cell(cell='B2',data=data,sheetname='DashBoard')
        # print(f"MarketStatus --- {data}")
        return data
    except Exception as e:
        print(f"maketStatus  -------------->>>>{e}")
def marketAdvacneDecline():
    try:
        n = NSELive()
        status = n.all_indices()
        data = [status['advances'], status['declines']]
        row_to_start = 'C2'
        time.sleep(0.1)
        update_cell(cell=row_to_start,data=status['advances'],sheetname='DashBoard')
        row_to_start = 'D2'
        time.sleep(0.1)
        update_cell(cell=row_to_start,data=status['declines'],sheetname='DashBoard')
    except Exception as e:
        print(f"marketAdvacneDecline  -------------->>>>{e}")

