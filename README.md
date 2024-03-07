# Network-Scanners
 A handful of different type of network scanners, ex Port(s) Scan, FTP Scan, Brute FTP Scan

    + bruteFTPscan.py
        This program is a Brute force scan of any File Transfer Protocol (FTP) ports by using the credential file of the admin's username and password. You will need to insert your own hostname under __main__
        If you can't connect to the port it will return that the login connection failed.

    + ftpscanner.py
        This program is a simple FTP port scanner, different from the brute FTP scanner it allows you to anonymously scan an IP address and checks if it is a FTP port or not. You will need to insert your own hostname under __main__        
        If it is not an FTP port the terminal will print that the FTP connection failed.

    + portscanner.py
        This program allows you to scan a Host IP address and connect to a custom port you can choose from or a series of ports you could scan through. You will need to insert your own hostname, currently there are port numbers to scan but those can be replaced, under __main__

    + credentials.txt
        - This is a text file with basic information for any file (bruteFTPscan.py, ) that may need it. The information on the file is a fake admin username, password and a two-factor authenication admin