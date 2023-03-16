import pyshorteners

long_url = input("Enter the URL to shorten: ")

print("URL after shortening: " + pyshorteners.Shortener().tinyurl.short(long_url))
