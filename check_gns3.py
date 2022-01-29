#python3.8
import telnetlib
import time

def main():
    time.sleep(1)
    # Specify host as ip address of GNS3 Server, i.e. '172.16.234.128' or 'localhost'
    host = 'localhost'
    # Specify tcp port number of node in gns3 project to be connected to via telnet
    port = 5004
    # Connect to specified address of gns3 server and port of destination node
    tn = telnetlib.Telnet(host, port)
    time.sleep(0.5)
    # Press Enter in cli
    tn.write(b'\n')
    # Expect '#' symbol in output folowed by hostname
    res = tn.expect([b'#'])
    # Execute ping command
    tn.write(b'ping 192.168.0.1 -c 1\n')
    time.sleep(1)
    # Read all data in output until '#' symbol folowed by hostname
    res = tn.expect([b'#'])
    print('Checking if host A is reacheble')
    print(b'0% packet loss' in res[-1])
    tn.close()

if __name__== "__main__":
    main()
