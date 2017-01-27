from ftplib import FTP

class Ftp_operations():
    server = '108.161.128.110'
    username = 'pyftpuer'
    password = 'PyDanta@1'
    location = '/home/pyftpuser'
    global ftp
    ftp = FTP(server)

    try:
        ftp.login(username,password)
        ftp.cwd(location)
    except:
        print("FTP server connection couldn\'t be established")

    @staticmethod
    def send_file(ftp):
        file = "madhu6.txt"
        ftp.storbinary('STOR' + file + open(file,'rb'))
        ftp.quit()
        file.close()

Ftp_operations.send_file()

#########
# import ftplib
#
# server = '108.161.128.110'
# ftp = ftplib.FTP()
# host = "ftp.site.uk"
# port = 21
# ftp.connect(server)
# print (ftp.getwelcome())
# try:
#   print ("Logging in...")
#   ftp.login("pyftpuer", "PyDanta@1")
# except:
#  "failed to login"