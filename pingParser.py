import subprocess
import re


def googlePing():
    p = subprocess.Popen("ping google.com",stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    A,B = p.communicate()
    return A

def parseAvg(x):
    parserA = re.search(r'(Average.*)(\d)', x, re.I)
    C = parserA.group(2)
    return C

def parseRec(y):
    #parserB = re.search(r'((Received.*)(\d+),)', y, re.I)
    parserB = re.search(r'(Received.*?\S)(.*?\d+)', y, re.I)
    D = parserB.group(2)
    return D

if __name__=="__main__":
    a = googlePing()
    parseAvg(a)
    parseRec(a)