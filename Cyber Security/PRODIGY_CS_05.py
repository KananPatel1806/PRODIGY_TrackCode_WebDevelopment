from socketserver import UDPServer
from telnetlib import IP, RCP
from scapy.all import *

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        print(f"Source IP: {src_ip} | Destination IP: {dst_ip} | Protocol: {protocol}")

        if TCP in packet: # type: ignore
            payload = packet[RCP].payload
            print(f"TCP Payload: {payload}")
        elif UDP in packet: # type: ignore
            payload = packet[UDPServer].payload
            print(f"UDP Payload: {payload}")

# Example usage
if __name__ == "__main__":
    print("Starting packet sniffer... Press Ctrl+C to stop.")
    conf.L3socket = L3RawSocket  # Use L3RawSocket for layer 3 sniffing
    sniff(prn=packet_callback, store=0)
