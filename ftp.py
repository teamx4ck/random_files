#!/bin/python3.8
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


# The port the FTP server will listen on.
# This must be greater than 1023 unless you run this script as root.
FTP_PORT = 8080

# The name of the FTP user that can log in.
FTP_USER = "rk"

# The FTP user's password.
FTP_PASSWORD = "rk"

# The directory the FTP user will have full read/write access to.
FTP_DIRECTORY = "/sdcard"


def main():
    authorizer = DummyAuthorizer()

    # Define a new user having full r/w permissions.
    authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm='elradfmw')

    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a customized banner (string returned when client connects)
    handler.banner = "pyftpdlib based ftpd ready."

    # Optionally specify range of ports to use for passive connections.
    #handler.passive_ports = range(60000, 65535)

    address = ('127.0.0.1', FTP_PORT)
    server = FTPServer(address, handler)

    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()


if __name__ == '__main__':
    main()