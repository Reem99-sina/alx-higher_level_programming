#!/usr/bin/python3

import requests
import sys


if __name__ == "__main__":
    value ={"q":"" if len(sys.argv) == 1 else sys.argv[1]}
    r= requests.post("http://0.0.0.0:5000/search_user", data=value)
    try:
        response = r.json()
        if response == {}:
            print("No Result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
