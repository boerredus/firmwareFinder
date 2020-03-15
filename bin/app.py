#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

def main():
    page = requests.get("https://www.sammobile.com/samsung/galaxy-s9/firmware/SM-G9600/ZTO/")
    soup = BeautifulSoup(page.content, "html.parser")
    soup = soup.findAll("span")
    print("Latest found firmware for SM-G9600:")
    print(" Date: " + str(soup[6]).replace("<span>", "").replace("</span>", ""))
    print(" Android Version: " + str(soup[7]).replace("<span>", "").replace("</span>", ""))
    print(" PDA: " + str(soup[8]).replace("<span>", "").replace("</span>", ""))
    print(" CSC: " + str(soup[9]).replace("<span>", "").replace("</span>", ""))

if __name__ == "__main__":
    main()
    exit()