"""
Script used to download
"""
import configparser
import requests
import datetime
import time


config = configparser.ConfigParser()
config.read("config.ini")
time_minutes = float(config["SETTINGS"]["download-minutes"])
URL = "https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_HMIIC.jpg"
FOLDER_DIR = config["SETTINGS"]["image-folder-dir"]

def download_image():
   # Download image
   print(f"[*] {datetime.datetime.now().isoformat()} Downloading image")
   response = requests.get(URL)
   # Store image in a file
   filename = f"{FOLDER_DIR}/solar_image_{datetime.datetime.now().isoformat()}.jpg"
   with open(filename, "wb") as f:
       f.write(response.content)
   with open("last.jpg", "wb") as f:
      f.write(response.content)

   print(f"[*] {datetime.datetime.now().isoformat()} - Download image and stored")
   


if __name__ == "__main__":
    while True:
        download_image()
        seconds = time_minutes * 60
        print(f"[*] Waiting {seconds} seconds until next download")
        time.sleep(seconds)
