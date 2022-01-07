#!/usr/bin/env python
# coding: utf-8

# # Introduction to Verilog programming on a FPGA device. Counters and frequency dividers.
# 
# ## Laboratory Class 01 - 21 September 2021
# 
# 
# ### Topics
# - A short overview on FPGA devices and on HDL programming languages.
# - Introductory problem: design of a 1 Hz counter with 8–LED array display, relying on standard analog and digital circuitry and an 8 Hz clock source.
# - Basic hardware circuits:
#     – frequency divider;
#     – counter.
# - Verilog programming language:
#     - module architecture;
#     - example: development of a 8–bit, 1 Hz counter with an 8–LED array display;
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
# - development of a 10 Hz counter, working from 0 to 99, with a 2–digits BCD coding and a 2 x 4–LED array display;
# - development of a 10 Hz down counter.
# 
# ---
# 
# ```{admonition} Disclaimer
# This part of the note does NOT aim to teach Verilog or how to survive in a laboratory. The first can be learned using apposite websites like [hdlbits](https://hdlbits.01xz.net/wiki/Main_Page) while the second skill requires years of training and struggle. The only way to learn how to survive in a laboratory is to be in a lab. It doesn't need to be an expensive one tho. To start a [beginner's FPGA](https://www.nandland.com/goboard/introduction.html) and a [basic oscilloscope](https://espotek.com/labrador/) are enough[^disclaimer]. In the worst-case there even exist simulators. Better than nothing, I guess.
# ```
# 
# [^disclaimer]: I studied verilog on hdlbits but I do no own the GoBoard or the EspoTek Labrador Board so I can not say anything about their quality. These are just link to help you start your own researches

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
