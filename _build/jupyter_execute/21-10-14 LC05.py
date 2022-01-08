#!/usr/bin/env python
# coding: utf-8

# # Driving the DACs and the ADCs hosted on the development board. Nyquist–Shannon sampling theorem made real.
# 
# ## Laboratory Class 05 - 14 October 2021
# 
# ### Topics
# - Numerical representation of natural and integer numbers:
#     - 2’s complement representation of integers;
#     - inversion of an integer $(−1) · n = (∼ n) + 1$;
#     - sum, difference $a − b = a + (−1) · b$, multiplication $a · b = |a| · |b| · sign(a) · sign(b)$;
#     - multiplication times 2k and division by 2k by means of the shift operator;
#     - using the 2’s complement representation with ADC/DACs.
# - Verilog programming language:
#     - driver of the ADCs placed on the development board;
#     - driver of the DACs placed on the development board.
# 
# ## Problems
# - evaluation of the Nyquist frequency and the transfer function gain (voltage-to-number-to-voltage) of a ADC-DAC feedthrough system;
# - implementation of a delayer.
# 
# 
# ---
# 
# ## Numerical representation of natural and integer numbers:
# I think everything important I can say is said in [this video](https://youtu.be/ys1ftk5a2A4) and on [wikipedia](https://en.wikipedia.org/wiki/Two%27s_complement).
# Take time to read through top comments. There are some interesting advices! 
# ## Evaluation of the Nyquist frequency
# This one is a nice one. 
