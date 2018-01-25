# -*- encoding: iso-8859-15 -*-


import os
from time import sleep

hostname = "google.com"

while True:

    response = os.system("ping " + hostname)
    if response == 1:
        print("No Internet")
    else:
        print("Internet!")
        pass
    sleep(60)
