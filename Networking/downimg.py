import urllib.request

url = 'https://popcornsg.s3.amazonaws.com/movies/650/14380-52688-Leojpg'

download = urllib.request.urlretrieve(url, 'leo.jpg')