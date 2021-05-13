# Author Eoin McLoughlin
import os
import bs4 as bs
import urllib.request
import lxml
import requests

from selenium import webdriver 
from selenium.webdriver.common.by import By

### GUIDE for getting the URL's ###
# https://www.youtube.com/watch?v=sMve66iaVQo
# https://www.youtube.com/watch?v=XRedIElqweI

### GUIDE for checking if downloadable ###



def get_all_song_urls(playlist_url):
    request = requests.get(playlist_url)
    # Create a BeautifulSoup Object
    soup = bs.BeautifulSoup(request.text, "lxml")

    # Get each song by its identifying h2 tag
    songs = soup.select("h2")
    url_list = []
    previous = ""
    base_url = "https://soundcloud.com"
    for song in songs:
        for link in song.find_all('a'):
            url = link.get('href')
            if url in previous:
                continue
            else:
                url_list.append(base_url + "{}".format(url))
                previous = url

    return url_list


def check_downloadable_songs(url_list):
    # 
    for url in url_list:
        # OPen the new url page
        browser.get(url)
        request = requests.get(playlist_url)
        # Create a BeautifulSoup Object
        soup = bs.BeautifulSoup(request.text, "lxml")

        more_button = browser.find_element(By.XPATH, '//*[@id="content"]/div/div[3]/div[1]/div/div[1]/div/div/div[2]/div/div/button[5]')
        more_button.click()
        #### TRY EXCEPT 
            # try find the download button 
        # except 
            #button wasnt there so move on and try next 
        






browser = webdriver.Chrome("C:/Users/eoinm/Drivers/chromedriver")
browser.get("https://soundcloud.com")


while True:
    print("0: Playlist download")
    print("1: Exit")

    choice = int(input(">>> What do you want to do? "))

    if choice == 1:
        browser.quit()
        break


    if choice == 0:
        # url = input("Enter the playlist URL that you want to download")
        playlist_url = "https://soundcloud.com/jshod/sets/sss"
        browser.get(playlist_url)
        # Get all URL's of tunes from the playlist
        url_list = get_all_song_urls(playlist_url)
        ### NOW WHAT TO DO
        # for each url in the list 
        # open it and see if it has the option to be downloaded 
        # if it does save it to a seperate list
        downloadable_songs = check_downloadable_songs(url_list)
                


print()
print("Goodbye")

# # # Works for getting all url's but will have trouble distinguishing between actual tune url's and noise 
# # url_list = []
# # for url in soup.find_all('a'):
# #     print(url.get('href'))
# #     url_list.append(url.get('href'))

# # for div in body.find_all('div'):
# #     for i in div:
# #         print("-------------")
# #         print(i)