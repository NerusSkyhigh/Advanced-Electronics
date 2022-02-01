#!/usr/bin/env python
# coding: utf-8

# # Multiplexers and demultiplexers
# ## Laboratory Class 02 - 22 September 2021
# 
# ### Topics
# - Hardware and software architectures:
#     - combinatorial and sequential circuits;
#     - synchronous and asynchronous circuits;
#     - example: asynchronous counter and synchronous version using a finite-state machine.
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
# - development of a synchronous counter based on a “master clock”.
# 
# ---
# 
# ## Types of Circuits:
# - Combinatorial circuits: just a bunch of logic gates put in cascade. There is no way to control the flow of information but, at the same time, you are using all the speed available.
# - Sequential circuits: circuits where _a_ memory element is present. Usually, it is some kind of flip flop and, therefore, a clock is needed.
# - Asynchronous circuits: circuits where all the parts are clocked by a single master clock. It assures that all the submodules are synchronized and avoids race condition problems.
# - Synchronous circuits: different parts of the circuit are clocked with different clocks. Easier to implement and allows for part of the circuit to work at a higher speed. Mitigation for race condition is a handshake protocol where each module has to signal the end of its computation.
# 
# 
# ## D Type Flip Flops
# 
# ![](https://upload.wikimedia.org/wikipedia/commons/c/c4/Flipflopd.png)
# 
# It is the simplest type of flip flop. At each clock cycle, it can be set to store a $1$ or a $0$ and it will hold it up to a change. It is the basic component of memories.
# 
# ## Multiplexers
# - (De)Multiplexers are asynchronous combinatorial circuits that allow transmitting data from $n$ different lines with a single data cable and $ceil\left(log_2(n)\right)$ selector lines. Only one line can be active at a given time.
# 
# ![Abstract example of multiplexer from wikipedia](https://upload.wikimedia.org/wikipedia/commons/e/e0/Telephony_multiplexer_system.gif)
