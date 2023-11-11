import os
from download import download
from os import system
import asyncio

def text():
    c = system("clear||cls")
    t = system('pyfiglet "Download  files" | lolcat')
    byuser = system('echo "Telegram: @whyakari" | cowsay -f eyes | lolcat')
    return c, t, byuser
text()

# urls supporteds formats are:
# ‘file’, ‘zip’, ‘tar’, ‘tar.gz’ Defaults to file.
url = str(input("file url: ")).strip()

if url == "" or url in "@#$/)(&+:!*-_+-)" or url == "https://" or url == "http://" or url == "https" or url == "http" or url in "abcdefghijklmnopqstuvwxyz" or url in "12345678910":
    print("invalid url")
    quit()
else:
    pass

# choose the path where the file will be located or leave it by default.
dirName = str(input("choose dir path name? y[yes]/d[default] "))

if dirName == "d": # default
    dirName = os.getcwd()
elif dirName == "y":
    dirName = str(input("choose path name: "))
else:
    print("error")
    quit()

kindtype = input("kind type: ") # example "zip", "ogg", "mp3"
progressbar = input("progressbar? [y/n] ")

if progressbar == "y":
    progressbar = True # whether to display a progress bar during file download.
elif progressbar == "n":
    progressbar = False # default is None statusBar progress
else:
    print("not defined")
    quit()

async def main(url=url, dirName=dirName, kindtype=kindtype, progressbar=progressbar):
    path = download(url, dirName, kindtype, progressbar, replace=True)
    return path

asyncio.run(main(url, dirName, kindtype, progressbar))
