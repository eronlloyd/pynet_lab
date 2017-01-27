import telnetlib

from secrets import ip_addr, username, password

TELNET_PORT = 23
TELNET_TIMEOUT = 6


def main():
    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    remote_conn.close()

if __name__ == "__main__":
    main()
