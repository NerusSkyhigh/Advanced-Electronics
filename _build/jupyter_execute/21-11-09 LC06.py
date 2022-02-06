#!/usr/bin/env python
# coding: utf-8

# # Waveform generation
# 
# ## Laboratory Class 06 - 11 November 2021
# 
# ### Topics
# - Basic hardware circuits:
#     - shift register.
# - Verilog programming language:
#     - shift register.
# 
# ## Problems:
# - implementation of sawtooth waveform generators.
# 
# ---
# 
# ## Shift Registers
# ```{admonition} from [wikipedia](https://en.wikipedia.org/wiki/Shift_register)
# A shift register is a type of digital circuit using a cascade of flip-flops where the output of one flip-flop is connected to the input of the next. They share a single clock signal, which causes the data stored in the system to shift from one location to the next. By connecting the last flip-flop back to the first, the data can cycle within the shifters for extended periods, and in this form, they were used as a form of computer memory.
# ```
# ### Pseudorandom noise generator
# An interesting application of shift register is a pseudorandom noise generator. A 31–bit pseudorandom number generator can be generated in the following way:
# - Implement a 31–bit shift register (SR),
# - Feed–back the serial input (i.e. the 0th bit) with the XOR of the 30th and the 27th bit,
# - Connecting eight randomly selected flip–flop outputs to the eight LEDs;
# 
# The mathematics of this algorithm is beyond the scope of the course. As usual, [wikipedia](https://en.wikipedia.org/wiki/Xorshift) is a good starting point if you want to dive into the topic. Two remarks are due:
# - ```31'b0``` is a trivial point that will generate only a static sequence of zeros
# - The XOR algorithm is not cryptographically secure. DO NOT try to use it when security is a concern. There are faster and better algorithms in that case.
# 
# ## Waveforms
# ![](https://upload.wikimedia.org/wikipedia/commons/7/77/Waveforms.svg)
# 
# ### Sinusoidal Wave
# Will be implemented in a later class.
# 
# ### Square Wave
# It can be implemented with a simple frequency divider and a bit flip.
# 
# ### Sawtooth Waveform
# This is an easy one. It is just a matter of implementing a counter and passing the output of the counter to a DAC.
# 
# ### Triangular Waveform
# A triangular waveform is composed of two opposite sawtooth waveforms one near the other. The descending ramp can easily be implemented by taking the negation of the counter's output, in this way a single positive counter will handle all the counting.
# 
# 
# 
