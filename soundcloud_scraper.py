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
    browser = webdriver.Chrome("C:/Users/eoinm/Drivers/chromedriver")
    browser.get(playlist_url)
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
        more_button = browser.find_element(By.XPATH, '//*[@id="content"]/div/div[3]/div[1]/div/div[1]/div/div/div[2]/div/div/button')
        for i in more_button:
            print(i.text)
        more_button.click()
        #### TRY EXCEPT 
            # try find the download button 
        # except 
            #button wasnt there so move on and try next 
        

def open_soundcloud_browser():

    return browser




while True:
    print("0: Exit")
    print("1: Playlist download")
    print("2: See songs in playlist")

    choice = int(input(">>> What do you want to do? "))


    if choice == 0:
        browser.quit()
        break


    if choice == 1:
        # url = input("Enter the playlist URL that you want to download")
        playlist_url = "https://soundcloud.com/jshod/sets/sss"
        # Get all URL's of tunes from the playlist
        url_list = get_all_song_urls(playlist_url)
        print(url_list)
        # Opens each URL and checks if the song haas tthe option to be downloaded or not
        downloadable_songs = check_downloadable_songs(url_list)


    if choice == 2:
        playlist_url = str(input(">>>Enter the URL of the playlist you want to look at: "))
        # playlist_url = "https://soundcloud.com/jshod/sets/sss"
        playlist_name = playlist_url.split("/")[-1]
        # Get all Urls of songs in the playlist]
        try:
            url_list = get_all_song_urls(playlist_url)
            playlist = [song.split("/")[-1].replace("-", " ") for song in url_list]

            #  Pretty printing the playlist contents 
            playlist_name_len = len(playlist_name)
            header = "-" * len(playlist_name) * 2
            print("here", len(header))
            len(playlist_name)
            print(playlist_name)
            print(header)
            for artist_song in playlist:
                print(artist_song)

            print()

        except:
            print("There was an error finding the playlist, please make sure its public")

        # /html/body/div[4]/div/div/button[2]
                


print()
print("Goodbye")