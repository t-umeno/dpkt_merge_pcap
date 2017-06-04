#!/usr/bin/python

import dpkt,socket

input_pcap_file1="input1.pcap"
input_pcap_file2="input2.pcap"
output_pcap_file="output.pcap"

def main():
    input_pcap1 = open(input_pcap_file1,'rb')
    pcr1 = dpkt.pcap.Reader(input_pcap1)
    input_pcap2 = open(input_pcap_file2,'rb')
    pcr2 = dpkt.pcap.Reader(input_pcap2)
    output_pcap = open(output_pcap_file,'wb')
    pcw = dpkt.pcap.Writer(output_pcap)
    
    for ts,buf in pcr1:
        pcw.writepkt(buf,ts)

    for ts,buf in pcr2:
        pcw.writepkt(buf,ts)
        
    input_pcap1.close
    input_pcap2.close
    output_pcap.close
    
if __name__ == '__main__':
    main()

