Packet Analyzer
==========================
Packet Analyzer is a tool to capture the packets and make it visualize.
To capture the packets I use C++ to write a eBPF program, which makes the speed of capture packets is really fast. (Please follow [Packet flow in Netfilter and General Networking](https://upload.wikimedia.org/wikipedia/commons/3/37/Netfilter-packet-flow.svg)) 
After get a bunch of packets, we use python to visualize those packets.

Basic Information
=================

GitHub repository:
https://github.com/JieJhih/Packet-Analyzer.git

Problem To Solve
================

A server will receive a bunch of packets every day, sometimes system administrator need to analyze each kind of packet (TCP? UDP? Specific IP?) occupy how many percent in daily. Using eBPF program is faster than other userspace tools, cooperate with Python could make data visible.

Perspective users
=================
1. System administrator who want to maintain server's health.
2. Data scientists who want to analyze the client agent, and packets peak or off-peak hours.

System architecture
=================

1. Capture the packets from eBPF program.
2. Send packets information to Python.
3. Organize a bunch of information of packets.
4. Show the statistic using Python GUI tool.

API decription
=================
1. Packet pool buffers.
2. Input filter type.
3. Output result
4. Time recording.

Engineering infrastructure
=================
1. Basic packet syntax parser
2. Basic packet data structure
3. Packets record usage

Schedule
=================

- week 7 written eBPF program in C++
- week 8 Design packet data structure
- week 9 implement filter function to filter different type of packets
- week 10 implement input parser
- week 11 implement GUI to show packets usage
- week 12 implement packets pool buffer in eBPF program

References
=================
1. https://zh.wikipedia.org/wiki/BPF
2. https://www.ithome.com.tw/news/139519
3. https://hackmd.io/@sysprog/linux-ebpf?type=view
