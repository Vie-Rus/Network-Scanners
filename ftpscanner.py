"""
Created by V I E R U S   ||   Date 07/30/2023
This is a simple FTP port scanner program.
Allowing you to anonymously scan an IP address and check if the port is FTP or not.
"""
#Import
import ftplib

def anonLogin(hostname):
    #If the port is FTP it will print a succeded print in the terminal
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous')
        print("\n [+] " + str(hostname) + " FTP anonymous Login Succeded.\n")
        return True

    #If the port is not an FTP it will print a failed print in the terminal
    except Exception:
        print("\n [-] " + str(hostname) + " FTP anonymous Failed.\n")
        return False

if __name__== '__main__':
    anonLogin('00.000.00.00')   #Type in your IP address here