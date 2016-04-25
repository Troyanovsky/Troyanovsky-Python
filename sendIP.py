import smtplib
import socket
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

newIP = str(socket.gethostbyname(socket.gethostname()))
try:
    oldIP = readFile("IP.txt")
except:
    oldIP = "None"
if newIP != oldIP:
    writeFile("IP.txt",newIP)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("troyanovzhao@gmail.com", "zhao970908")
    msg = "MAC IP is " + readFile("IP.txt")
    server.sendmail("troyanovzhao@gmail.com", "gzhao@andrew.cmu.edu", msg)
    server.quit()
    print("Sent!")
else:
    print("IP unchanged")