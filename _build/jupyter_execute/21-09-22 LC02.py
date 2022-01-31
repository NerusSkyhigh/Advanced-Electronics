#!/usr/bin/env python
# coding: utf-8

# # Multiplexers and demultiplexers
# ## Laboratory Class 02 - 22 September 2021
# 
# ### Topics
# - Hardware and software architectures:
#     - combinatorial and sequential circuits;
#     - synchronous and asynchronous circuits;
#     - example: asynchronous counter and synchronous version by means of a finite-state machine.
# - Basic hardware circuits:
#     - multiplexer;
#     - demultiplexer.
# - Verilog programming language:
#     - combinatorial (assign) and sequential (always) Verilog modules;
#     - basic modules implementing basic hardware circuits:
#         - multiplexer (synchronous and asynchronous version);
#         - synchronous counter with set to a preset value, and reset;
#     - blocking and non–blocking assignments.
# 
# ## Problems:
# - development of a stopwatch from 0 to 99.99 s (1/100 s resolution), with 2–digits BCD coding and a 2 x 4–LED array display;
# - development of a syncronous counter based on a “master clock”.
# 
# ---
# ## D Type Flip Flops
# ![](https://upload.wikimedia.org/wikipedia/commons/c/c4/Flipflopd.png)
# It is the simplest type of flip flop. At each clock cycle it can be set to store a $1$ or a $0$ and it will hold it up to a change. It is the basic component of memories.
# 
# ## Multiplexers
# - (De)Multiplexers are combinatorial circuits, that is they do not require a clock to work.
# - Allow to transfer data from $n$ lines with a single data line and $ceil\left(log_2(n)\right)$ selector lines. Only one line can be active at a given time.
