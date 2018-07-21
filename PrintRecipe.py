import cups

def print_FILE():
    try:
        conn = cups.Connection()
        printers = conn.getPrinters()
        for printer in printers:
            print printer, printers[printer]["device-uri"]
            print "A\n"
            #printer_name="Test"
            printer_name=printers.keys()[0]
            print printer_name
        fileName = "billTest.txt"
        conn.printFile(printer_name, fileName, " ", {})
    except:
        pass
#print_FILE()
"""    
fileName = "billTest.txt"

import cups
conn = cups.Connection()
printers = conn.getPrinters()
print printers
printer_name = printers.keys()[0]
conn.printFile(printer_name,fileName,"Hello",{})
print "here"
import subprocess
lpr =  subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
lpr.stdin.write(fileName)"""
