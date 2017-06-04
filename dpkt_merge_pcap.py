#!/usr/bin/python

import getopt, sys
import dpkt,socket

def usage():
    print "dpkt_merge_pcap [-l input_pcap_file_list] [-o output_pcap_file]"

def main():
    input_pcap_file_list="/dev/stdin"
    output_pcap_file="/dev/stdout"

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hl:o:", ["help", "input_pcap_file_list=", "output_pcap_file="])
    except getopt.GetoptError as err:
        # print help information and exit:
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit(2)
        elif o in ("-l", "--input_pcap_file_list"):
             input_pcap_file_list = a
        elif o in ("-o", "--output_pcap_file"):
             output_pcap_file = a
        else:
            assert False, "unhandled option"

    output_pcap = open(output_pcap_file,'wb')
    pcw = dpkt.pcap.Writer(output_pcap)

    f = open(input_pcap_file_list)
    line = f.readline()

    while line:
        line = f.readline()
        input_pcap = open(line,'rb')
        pcr = dpkt.pcap.Reader(input_pcap)
        for ts,buf in pcr:
            pcw.writepkt(buf,ts)
        input_pcap.close
    f.close
        
    output_pcap.close
    
if __name__ == '__main__':
    main()

