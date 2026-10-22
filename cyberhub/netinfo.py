""" Gets local information (IP, network, etc.) """

import socket
import ipaddress


def get_local_ip():
    """ Creates a UDP socket that doesn't send any packets to get local IP address. """
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        try:
            sock.connect(("8.8.8.8", 80))
            address, _ = sock.getsockname() # port not used
            return address
        
        except OSError as e:
            if e.errno == errno.ENETUNREACH:
                return "127.0.0.1"
            else:
                raise


def get_local_network(ip):
    """ Gets IPv4 network from local IP address """
    addr = ipaddress.ip_network(f"{ip}/24", strict=False)
    num_hosts = len(list(addr.hosts()))
    return addr, hosts



if __name__ == "__main__":
    ip = get_local_ip()
    ipv4, num_hosts = get_local_network(ip)
    print(ip)
    print(ipv4)
    print(num_hosts)