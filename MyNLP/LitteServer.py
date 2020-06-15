from subprocess import check_output
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 9000))
sock.listen(10)

while True:
    conection, address = sock.accept()
    try:
        conection.settimeout(50)
        buf = conection.recv(1024)
        up = buf.decode(encoding="utf-8")
        cmd = ["bash", "./inference.sh", up]
        result = check_output(cmd)
        conection.send(result)
    except socket.timeout:
        print("Time out")
    conection.close()