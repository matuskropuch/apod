import urllib.request
import ctypes
from re import search

baseurl = "https://apod.nasa.gov/apod/"
pageurl = baseurl + "astropix.html"
image_path = "C:\\Users\\kropu\\Pictures\\apod\\imageoftheday.jpg"

# download html
response = urllib.request.urlopen(pageurl)
html = response.read().decode('UTF-8')
response.close()

# find image url, download and save locally
imageurl = baseurl + \
    search('<a href="(.*\.jpg)"', html).group(1)
image = urllib.request.urlopen(imageurl)

with open(image_path, 'wb') as localFile:
        localFile.write(image.read())
image.close()

# magic windows variables
SPI_SETDESKWALLPAPER = 0x0014
SPIF_UPDATEINIFILE = 0x0001
SPIF_SENDWININICHANGE = 0x0002

# set wallpaper
user32 = ctypes.WinDLL('user32')
user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER,
                             0,
                             image_path,
                             SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)
