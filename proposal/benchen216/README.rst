==========================================
Proposal for logic gate circuit simulation
==========================================

Basic information
=================
In recent days, FPGA SoC and some kinds of SoC can be use as AI or deep learning accessor,
also 5g will use FPGA as RFSoc to extend the radio transmission.

project URL:

https://github.com/benchen216/logic-gate-sim


Perspective users
=================

1. The student that feel verilog is so difficult.
2. The people want to run simple logic circuit.

System architecture
===================

Data Flow

1. read in logic gate circuit syntax
2. construct the circuit and fill to data type
3. read in the input to run the circuit
4. output the result

API description
===============

1. logic gate circuit
2. input value
3. out put result
4. performance trace

Engineering infrastructure
==========================

1. circuit syntax parser
2. circuit data structure
3. Garbled Circuit real world usage
4. performance tracer

Schedule
========

* week 6 proposal draft
* week 7 implement circuit syntax parser
* week 8 design circuit data structure
* week 9 improve performance
* week 10 implement addition circuit (Garbled Circuit) real number
* week 11 finalizing program quality and code refactoring
* week 12 prepare presentation

References
==========

1. https://www.electronics-tutorials.ws/logic/logic_1.html
2. https://en.wikipedia.org/wiki/Logic_gate
3. https://www.intel.com.tw/content/www/tw/zh/products/programmable/fpga.html
4. https://www.bnext.com.tw/article/55882/xilinx-fpga-vitis-5g-rfsoc