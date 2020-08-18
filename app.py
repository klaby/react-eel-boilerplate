import eel
import sys
import random


@eel.expose
def hello():
    print("Hello World!")


if __name__ == "__main__":
    if sys.argv[1] == "--develop":
        directory = "dist"
        page = {"port": 4000}
    else:
        directory = "dist"
        page = "index.html"

    eel_kwargs = dict(host="localhost", port=8080, size=(1280, 800))

    eel.start(page, mode="chrome", **eel_kwargs)
