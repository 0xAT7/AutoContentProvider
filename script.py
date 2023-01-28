# Drozer -> run app.provider.finduri paymob.com.abkwallet
# Add all providers in contents.txt and run python3 autoprovider.py contents.txt
# pip install colorama

import subprocess
import sys
from colorama import init, Fore, Back, Style
init(convert=True)

providers = sys.argv[1]
with open(providers, 'r') as f:
    for line in f:
        query_process = subprocess.Popen("adb shell content query --uri {}".format(line), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        query_out,query_err = query_process.communicate()
        if query_err:
            print(Fore.RED +"Query failed for: " + line)
            continue
        print(Fore.GREEN + "Query success for: " + line + "   Output: " +query_out.decode("utf-8"))
        read_process = subprocess.Popen("adb shell content read --uri {}".format(line), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        read_out,read_err = read_process.communicate()
        if read_err:
            print(Fore.RED +"Read failed for: " + line)
            continue
        print(Fore.GREEN +"Read success for: " + line + "   Output: " + read_out.decode("utf-8"))
