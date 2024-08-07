import re
import subprocess
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Path to your service account credentials JSON file
CREDS_FILE = 'path/to/your/credentials.json'

# Google Sheets setup
# Define the scope and credentials for the service account
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILE, scope)
client = gspread.authorize(creds)

# Open the Google Sheet (replace with your sheet name)
sheet = client.open("Internet Speed Test Results").sheet1

# Append headers to Google Sheet if needed
if sheet.row_count == 1:
    sheet.append_row(["Date", "Time", "Ping (ms)", "Jitter (ms)", "Download (Mbps)", "Upload (Mbps)"])

# Run the speed test
response = subprocess.Popen('/usr/bin/speedtest --accept-license --accept-gdpr', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')

ping = re.search('Latency:\s+(.*?)\s', response, re.MULTILINE)
download = re.search('Download:\s+(.*?)\s', response, re.MULTILINE)
upload = re.search('Upload:\s+(.*?)\s', response, re.MULTILINE)
jitter = re.search('Latency:.*?jitter:\s+(.*?)ms', response, re.MULTILINE)

ping = ping.group(1)
download = download.group(1)
upload = upload.group(1)
jitter = jitter.group(1)

# Log results to Google Sheets
date = time.strftime('%Y-%m-%d')
current_time = time.strftime('%H:%M:%S')
sheet.append_row([date, current_time, ping, jitter, download, upload])
