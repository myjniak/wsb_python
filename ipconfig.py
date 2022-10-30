import socket
import subprocess


def get_command_output(command: str) -> str:
    wynik_z_konsoli = subprocess.check_output(command)
    napis_string = (wynik_z_konsoli.decode(encoding='ANSI'))
    return napis_string


napis = get_command_output("ipconfig")
lines = napis.splitlines()
for line in lines:
    if "IPv4" in line:
        print(line.split()[-1])


host = socket.gethostname()
print(host)
print(socket.gethostbyname(host))
