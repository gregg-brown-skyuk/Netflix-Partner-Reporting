# Netflix Partner Reporting Dowload Tool
![Netflix on Sky](https://static.skyassets.com/contentstack/assets/bltdc2476c7b6b194dd/bltbf7ca9ff9400dbe7/5e21f0bce2b3975498eae0b0/Sky_and_Netflix.png)

This code allows the automatic download of monthly reporting from Netflix Partner site followed by the upload of the contained data to Google Cloud Patform BigQuery table.

---
### *netflix_report_download.py*

This is the code which completes the processes of:
- accessing the website to download report;
- extracting the csv files from the downloaded zip archives;
- loading and tranforming the data from csv file in a dataframe;
- uploading data from the dataframe to GCP.
---
### *create_credentials.py*

This script is used to:
- create new credentials file when called by `netflix_report_download.py` script;
- create new or amend existing credentials when run directly.

### Contact me at [gregg.brown@sky.uk](mailto:gregg.brown@sky.uk)
