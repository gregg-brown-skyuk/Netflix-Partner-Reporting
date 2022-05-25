# Netflix Partner Reporting Dowload Tool

This code allows the automatic download of monthly reporting from Netflix Partner site followed by the upload of the contained data to Google Cloud Patform BigQuery table.

* netflix_report_download.py_
This is the code which completes the processes of:
    accessing the website to download report;
    extracting the csv files from the downloaded zip archives;
    loading and tranforming the data from csv file in a dataframe;
    uploading data from the dataframe to GCP.

* create_credentials.py
This script is used to:
    create new credentials file when called by netflix_report_download.py script;
    create new or amend existing credentials when run directly.