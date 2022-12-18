# Python code of the Mode Controller
#   To do:
#       - Receive Gas Price, Mode and "Taxes"
#       - Send Mode to Esp Triaq

from datetime import datetime
from WebScrap import getValue

TimeS = datetime.__new__(datetime, 1, 1, 1, 13, 30, 0)
TimeE = datetime.__new__(datetime, 1, 1, 1, 13, 30, 1)

if __name__ == '__main__':

    # Start up
    v = getValue()  # read last 30 days mean (Euro/MWh)
    print(v)

    while True:
        date = datetime.now()
        if (date.time() >= TimeS.time()) and date.time() <= TimeE.time():   # if time == 13:30
            v = getValue(v)     # read last 30 days mean (Euro/MWh)
            print(v)
