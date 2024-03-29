#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    
    # create a request object with the URL
    request = urllib.request.Request(url)

    with urllib.request.urlopen(request) as response:
         x_request_id = response.getheader('X-Request-Id')
         print(x_request_id)
