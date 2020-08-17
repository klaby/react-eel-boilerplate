import eel
import sys


@eel.expose
def hello():
    print("Hello World!")


if __name__ == "__main__":
    if sys.argv[1] == "--develop":

        eel.init("dist")
        eel.start({"host": "0.0.0.0", "port": 4000})
    else:
        eel.init("dist")
        eel.start("index.html")
