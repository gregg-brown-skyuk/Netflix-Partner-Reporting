from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.common.by import By
from pathlib import Path
from datetime import datetime as dt, timedelta as td, date
from time import sleep
from cryptography.fernet import Fernet
from create_credentials import CreateNetflixCredentialsFile
import shutil, os, json, pandas as pd

title = '+ NetFlix Partner Report Downloader +'
decoration = '+'*len(title)
print(f'{decoration}\n{title}\n{decoration}\n')

print('Process started...')
thisMonth = dt.strftime(date.today(), '%B %Y')
url = f'https://partner-reports.netflixpartners.com/' # Netflix login
saveDir = f'{Path.home()}\Downloads\{thisMonth} Netflix'
fileMonth = dt.strftime(date.today().replace(day=1) - td(days=1), '%b_%y')
fileNames = [fr'{saveDir}\Netflix_Bundle_Invoice_Report_Data_Sky_UK_{region}_{fileMonth}.csv.zip' 
                for region in ['GB','IE']]

credFile = 'credentials.enc'
while True:
    if os.path.exists(credFile):
        with open('filekey.key', 'rb') as keyFile:
            fernet = Fernet(keyFile.read())
        with open(credFile, 'rb') as encFile:
            credentials = json.loads(fernet.decrypt(encFile.read()))['Netflix']
        break
    else:
        CreateNetflixCredentialsFile(credFile)

xpaths = {
    'username':
        r'/html/body/div[2]/div/div/div[2]/form/div[1]/input',
    'continue':
        r'/html/body/div[2]/div/div/div[2]/form/div[2]/button',
    'password':
        r'/html/body/div[2]/div/div/div[3]/form/div[2]/input',
    'login':
        r'/html/body/div[2]/div/div/div[3]/form/div[4]/button',
    'partner_reports':
        r'/html/body/div[2]/div[1]/div[2]/div[4]/a/div/p[1]'
}

options = FirefoxOptions()
options.set_preference('browser.download.folderList', 2)
options.set_preference('browser.download.dir', saveDir)
options.set_preference('browser.download.manager.showWhenStarting', False)
options.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')
options.add_argument('--headless')

with Firefox(options=options) as browser:
    browser.get(url=url)
    print('Logging onto Netflix Partner Site..', end='\r')
    browser.implicitly_wait(30)
    browser.find_element(By.XPATH, xpaths['username']).send_keys(credentials['email'])
    browser.find_element(By.XPATH, xpaths['continue']).click()
    browser.find_element(By.XPATH, xpaths['password']).send_keys(credentials['password'])
    browser.find_element(By.XPATH, xpaths['login']).click()
    monthSection = browser.find_element(By.XPATH, f"//*[contains(text(), '{thisMonth}')]")
    print('Downloading zip files...', end='\r')
    for i in range(1,3):
        monthSection.find_element(By.XPATH, f'../section[{i}]/div[2]/div/button').click()
    while True:
        try:
            for zipFile in fileNames:
                shutil.unpack_archive(zipFile, saveDir)
                print(f'Unpacking {zipFile}...', end='\r')
                os.remove(zipFile)
            break
        except:
            sleep(2)

csvFiles = [f'{saveDir}\{csvFile}' for csvFile in os.listdir(saveDir)]
dateCols = ['Report_Month', 'Event_Date', 'Cancel_Date']
gcpSchema = [{'name':col,'type':'date'} for col in dateCols]
projectId='skyuk-uk-csgbillanalysis-dev'
destTable=f'Sandpit.GB_Netflix_{fileMonth}_test'

for csvFile in csvFiles:
    print(f'Loading data from {csvFile}...', end='\r')
    df = pd.read_csv(csvFile)
    df = df.rename(columns={col:col.replace(' ','_') for col in df.columns})
    for col in ['Report_Month', 'Event_Date', 'Cancel_Date']:
        df[col] = df[col].astype('datetime64[ns]')
    df['Account_Number'] = df.Billing_Partner_Handle.apply(lambda x:x[-12:] if x[:3]=='SKY' else None)
    print(f'Uploading data from {csvFile} to {destTable}...', end='\r')
    df.to_gbq(project_id=projectId, destination_table=destTable, if_exists='append', location='EU', table_schema=gcpSchema)

print('Process Ended')