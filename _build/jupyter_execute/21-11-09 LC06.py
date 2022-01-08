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
# A shift register is a type of digital circuit using a cascade of flip-flops where the output of one flip-flop is connected to the input of the next. They share a single clock signal, which causes the data stored in the system to shift from one location to the next. By connecting the last flip-flop back to the first, the data can cycle within the shifters for extended periods, and in this form they were used as a form of computer memory.
# ```
# ### Pseudorandom noise generator
# An interesting application of shift register is pseudorandom noise generator. I'll probably update this section later, but for now you can start from the [xorshift](https://en.wikipedia.org/wiki/Xorshift) method.
# 
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
# ### Tringular Waveform
# A triangular waveform composed of two opposite sawtooth wf one near the other. The descending ramp can easily be implemnted by taking the negation of the counter's output, in this way a single positive counter will handle all the counting.
# 
# 
# 
