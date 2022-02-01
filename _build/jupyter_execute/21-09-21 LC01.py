#!/usr/bin/env python
# coding: utf-8

# # Introduction to Verilog programming on an FPGA device. Counters and frequency dividers.
# 
# ## Laboratory Class 01 - 21 September 2021
# 
# 
# ### Topics
# - A short overview of FPGA devices and HDL programming languages.
# - Introductory problem: design of a 1 Hz counter with 8–LED array display, relying on standard analog and digital circuitry and an 8 Hz clock source.
# - Basic hardware circuits:
#     – frequency divider;
#     – counter.
# - Verilog programming language:
#     - module architecture;
#     - example: development of an 8–bit, 1 Hz counter with an 8–LED array display;
#     - basic modules implementing basic hardware circuits:
#         - frequency divider;
#         - counter.
# 
# ### Problems:
# - development of an 8–bit, 1 Hz counter with an 8–LED array display, working from 0 to 255;
# - development of an 8–bit, 1 Hz counter with an 8–LED array display, working from 0 to 9;
# - development of an 8–bit, 10 Hz counter with an 8–LED array display, working from 0 to 9.
# 
# ### Additional problems:
# - development of a 10 Hz counter, working from 0 to 99, with a 2–digits BCD[^bcd] coding and a 2 x 4–LED array display;
# - development of a 10 Hz down counter.
# 
# ---
# 
# ```{admonition} Disclaimer
# This part of the note does NOT aim to teach Verilog or how to survive in a laboratory. The first can be learned using apposite websites like [hdlbits](https://hdlbits.01xz.net/wiki/Main_Page) while the second skill requires years of training and struggle. The only way to learn how to survive in a laboratory is to be in a lab. It doesn't need to be an expensive one tho. To start a [beginner's FPGA](https://www.nandland.com/goboard/introduction.html) and a [basic oscilloscope](https://espotek.com/labrador/) are enough[^disclaimer]. In the worst-case there even exist simulators. Better than nothing, I guess.
# ```
# 
# [^bcd]: Binary coded decimal. Each digit is represented using four LEDs; they are placed in a decimal representation. e.g: $34$ would be written as 0011 0100 in BCD. 
# [^disclaimer]: I studied Verilog on hdlbits but I do not own the GoBoard or the EspoTek Labrador Board so I can not say anything about their quality. These are just linked to helping you start your researches
# 
# 
# ## Basic hardware circuits:
# Frequency dividers and counters are similar under many aspects to the extent that you can imagine a frequency divider as a counter and a threshold. When the desired number of input positive edges are counted, a positive edged is generated as output. Usually, frequency dividers are designed as a cascade of data flip flops (D-type FF).
# 
# ![D-type flip flop used as frequency halver](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/counter-cou1.gif)
# 
# A counter can be obtained in the same way by connecting the output $Q$ of each FF to the desired circuit. Check [this](https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgzCAMB0l3BWEAmM0AsB2SCCcyBGANiMwUjCXJCshoFMBaAggKAISJAA5uVNkIApHT9BBGu05CEg5AKFE+88ZIDuMuQoLpRKqKw06923eBEGjZsBY6CboyIaFgu+gq5S9LLt97tefE4cbsRiKGBaqsHSyNx0+si4btoGIeBm+pRRQpLp6JDKCujIJtFSXFg56N7uPshw4Q0J3k4azYEoYXFBzshEZSgDnW1DerXxI86RRfZxUxoznWCZrdP44WAbPT5bct4Fymsa6LHFsccgp358VQtdKXKF4aMNsyjPDvWfFoRcX69JokFPpXiDwfYLGDIeM6ADppkFGBPKDpiikZ54YtMRYVqIsVdnvoCgkFKMSeEKQSqRZDuZHM47sThqiTizisNqZzaUioc5jPShNZPK8fnpPiL+cK3BKuKK+MjHuBJe1eYNFfUMf9MSrldrKo0NeTDZ50JzdWb8abuQyTobaSa5Wj-ridU6AEo8I4K-Z8CTieAoaBIZDBqBQYPOWoKIFkqOkwSTAlJizeZNw1Nw3VJzwCo2sT05-72EXhgo0cN0GAIfno8Qo0rfBMfBKNV7suTDAiYJ2LeZZeYBUZ7TYbAjzclnQTXIR8jSyZsLnhV1gAWV8KEbQMbckj646HSBjV3Nf3XZ7y6EF5Pa-Ag9kl4CN-XI-HfEmb5QQdPV2kwlEH6-N+t5LpMYEJMBbJWlwsgKrqsF6jQ8wEku+ioZc6F8AgKJrOk2FKggD51DW879goCEoWRgj4S8zgINwgz0aI0ijBRFg0fC65MTQXCTLEwHoAQuAgEQkReiJNTiRI3B0QxPEic8LHTPegiieID7DmO8xEI0n6jDpdCfgZG76bpnhqSZjJ-hYxn-j4tk2bpDT2U5dAWeOK6kXQkxEGEkz6X5blhHZAVcHZ7lzgpWFcBZSkaLFMViZcHhuI2FnII2+liRlojpW2fTHo0xkdKZrZubpcmlUIcnuZVfTnjFukXlV3aNYZSgue1fDuR1TgAPYgJg3WOFcwjURG8CQLgPacMgSCGawA0dcMdCCZA40wJN01ELN81CItImYBJZZjRWm3wNtu3hmwS0xSNa0bbAF0zUQc3XQdO3Hatp3zU9cCXa9e03cdK2jetZ1-VNL1vQtS0QKDD0Q1t0NAx9qn3T9E3PTtgPvUAA) interactive simulation to better understand how it works.
# 
# More info can be found [here](https://www.electronics-tutorials.ws/counter/count_1.html). This website is also the source of the image used.

# <!-- ## A short overview on FPGA devices and on HDL programming languages.
# 
# According to wikipedia, a Field Programmable Gate Array (FPGA) is a device that contain an array of programmable logic blocks, and a hierarchy of reconfigurable interconnects allowing blocks to be wired together. Logic blocks can be configured to perform complex combinational functions, or act as simple logic gates like AND and XOR. In most FPGAs, logic blocks also include memory elements. Many FPGAs can be reprogrammed to implement different logic functions, allowing flexible reconfigurable computing as performed in computer software.  
# 
# 
# 
# 
# - Basic hardware circuits:
#     – frequency divider;
#     – counter.
# - Verilog programming language:
#     - module architecture;
#     - example: development of a 8–bit, 1 Hz counter with an 8–LED array display;
#     - basic modules implementing basic hardware circuits:
#         - frequency divider;
#         - counter. -->
