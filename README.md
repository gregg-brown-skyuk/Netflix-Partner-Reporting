# Netflix Partner Reporting Dowload Tool
<!-- ![Netflix on Sky][netflix-sky-image] -->

<img alt='Sky and Netflix logo' id='sky_netflix' src='https://static.skyassets.com/contentstack/assets/bltdc2476c7b6b194dd/bltbf7ca9ff9400dbe7/5e21f0bce2b3975498eae0b0/Sky_and_Netflix.png'>

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
---

## Required Python Libraries

These additional python libraires need to be installed.

<code>Selenium</code>
<code>Cryptography</code>
<code>Pandas</code>

---

## Other Requirements
<details>
    <summary>The script requires the Firefox browser to be installed, and Firefox webdriver needs to be downloaded and installed / save to PATH folder.</summary>

* Download Firefox from [here][ff-link]

* Download Webdriver from [here][ff-driver]
</details>

---
### Contact me by [email][my-email].

<!-- Links  -->

[my-email]: mailto:gregg.brown@sky.uk
[ff-link]: https://www.mozilla.org/en-GB/firefox/download/thanks/
[ff-driver]: https://github.com/mozilla/geckodriver/releases

<style>
    .container {
        width: 100%;
        display: flex;
        justify-content: space-around;
    }
    .item {
        text-align: center;
        border: 1px solid #444444;
        flex-grow: 1;
    }
    #sky_netflix {
        border: 1px solid;
        border-radius: 25px;
    }
</style>