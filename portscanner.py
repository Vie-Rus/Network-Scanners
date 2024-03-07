"""
Created by V I E R U S   ||   Date 07/30/2023
This program allows you to scan a Host IP address and then if it can connect will scan the ports
The Host IP address and which ports you will need to input depending on which host and ports you want to scan
"""
#Imports
from socket import *

#Check if the port can be connected to or not
def connectScan(targetHost, targetPort):
    try:
        connectsocket = socket(AF_INET, SOCK_STREAM)
        connectsocket.connect((targetHost, targetPort))
        print("\n[+] %d || tcp connected and open." % targetPort)
        connectsocket.close()
    
    except:
        print("\n[-] %d || tcp not connecting or closed." % targetPort)   
        
#This will scan all the ports of the given host IP address
def portScan(targetHost, targetPorts):
    #Check if you can get other port results from the host IP
    try:
        targetIP = gethostbyname(targetHost)
        
    except:
        print("\n[-] Cannot get ports results from: " + targetHost)   
        return
#--------------------------------------------------------------------
    #Get the ports results from either Host Address or the IP address directly
    try:
        targetName = gethostbyaddr(targetIP)
        print("\n[+] Scan result of %s " % targetName[0])
        
    except:
        print("\n[+] Scan result of %s " % targetIP)
        
    #set time out incase ports do not come in, timer is set for 10 seconds
    setdefaulttimeout(10)
    for targetPort in targetPorts:
        print("Scanning Port: %s" % targetPort)
        connectScan(targetHost, int(targetPort))

if __name__ == '__main__':
    connectScan('00.000.00.00', 80)     #TODO Type your IP address and port number here
    portScan('00.000.00.00', [80, 22])      #TODO Type your IP address and port numbers that you want to scan through