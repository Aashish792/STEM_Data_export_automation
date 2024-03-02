# STEM_Data_export_automation


# Automated Web Scraping and Data Download with Selenium

This repository contains a Python script for automating web scraping and data download from a website using Selenium.

## Prerequisites

- Python 3.x
- Selenium library
- Chrome WebDriver (for Chrome browser automation)

You can install the required Python packages using pip:

```bash
pip install selenium
```

You also need to download the Chrome WebDriver from the official website: [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your_username/web-scraping-selenium.git
cd web-scraping-selenium
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the script:

```bash
python3 main.py <username> <password>
```

Replace `<username>` and `<password>` with your actual credentials for logging into the website.

## Description

The main script `main.py` orchestrates the workflow by utilizing several modules:

- `initialize_driver.py`: Initializes the Chrome WebDriver for browser automation.
- `login_and_navigate.py`: Logs in to the website and navigates to the desired page.
- `download_data.py`: Downloads data from the website after navigating to the appropriate page.
- `file_operations.py`: Manages file operations such as moving downloaded files.

The script automates the following tasks:
- Logging into the website with provided credentials.
- Navigating to a specific page within the website.
- Downloading data from the website.
- Moving the downloaded file to a specified directory.

## Customization

You can customize the script by modifying the following variables in `main.py`:

- `start_date` and `end_date`: Adjust the date range for data download.
- `download_dir`: Specify the directory where downloaded files are saved.
- `filename_pattern`: Specify the pattern to match for the downloaded file.
- `destination_dir`: Specify the directory where the downloaded file should be moved.

