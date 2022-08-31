# Standard modules
import json

# Custom modules

from scr.bll.stopper import stopper



def runner():

    # Load buys
    with open('files/manual.json') as json_file:
        jmanual = json.load(json_file)
    json_file.close()


    if (jmanual.get("buy")) and (jmanual.get("strategy") == "manual") and (not jmanual.get("sell")):
        _stopper = stopper(jmanual)
        _stopper.setLimit()



if __name__ == "__main__":
    runner()

