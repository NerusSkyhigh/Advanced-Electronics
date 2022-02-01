#!/usr/bin/env python
# coding: utf-8

# # Synchronous counters. Toggle flip-flops. Monostable multivibrators.
# ## Laboratory Class 03 - 23 September 2021
# 
# 
# ### Topics
# - Risetime issue when clocking a flip-flop.
# - Verilog programming language:
#     - basic modules implementing basic hardware circuits:
#         - synchronous toggle flip-flop [*];
#         - synchronous monostable multivibrator [*].
# 
# [^*]: to be developed within the problems.
# 
# ## Problems:
# - implementation of a synchronous module toggle flip-flop and, through this, of a toggle pushbutton to switch on/off an LED;
# - implementation of a synchronous module monostable multivibrator and, through this, of an improved toggle pushbutton to switch on/off an LED; observation of the bouncing effect in a pushbutton;
# - implementation, by means of a monostable multivibrator and an improved toggle pushbutton, of a timer to switch on an LED for a given time (programmable through the switches).
# 
# ---
# 
# ## Risetime issue when clocking a flip-flop
<<<<<<< HEAD
# Flip flops work due to internal delays that are essential to their implementation. A drawback of this is that, in rare circumstances, the clock may be too fast and have a period smaller than the internal delay giving rise to unreliable behaviors.
=======
# Flip flops are work  due to internal delays that are essential to their implementation. A drawback of this is that, in rare circustamces, the clock may be too fast and have a period smaller than the internal delay giving rise to unreliables behaviours.
>>>>>>> 7b5140664fa0ec9c10df743734622a245b74c7f6
# 
# 
# ## Syncronous Toggle Flip-Flop
# 
# ![T Type Flip-Flop. source: wikipedia](https://upload.wikimedia.org/wikipedia/commons/a/a9/T-Type_Flip-flop.svg)
# 
# ```{admonition} from [wikipedia](https://en.wikipedia.org/wiki/Flip-flop_(electronics)#T_flip-flop)
# If the T input is high, the T flip-flop changes state ("toggles") whenever the clock input is strobed. If the T input is low, the flip-flop holds the previous value. This behavior can be described in a truth table:
# 
# | Q | T | $Q_{\text{next}}$ | $Q_{\text{next}}$ |
# |:---:|:---:|:---:|:---:|
# | 0 | 0 | 0 | Hold state (no clock) |
# | 0 | 1 | 0 | Hold state (no clock) |
# | 1 | 0 | 1 | Toggle |
# | 1 | 1 | 1 | Toggle |
# 
# When T is held high, the toggle flip-flop divides the clock frequency by two. This "divide by" feature has applications in various types of digital counters.
# ```
# 
# As Wikipedia already stated T flip flops are essential to produce frequency dividers, counters, and shift registers.
# 
<<<<<<< HEAD
# **Note**: when implementing a synchronous Flip Flop in Verilog remember to let the FF activate only on positive edges of the input. This can be done by defining two variables ```ff_input``` and ```ff_previous_input``` and checking for a positive edge with
=======
# **Note**: when implementing a syncronous Flip Flop in verilog remember to let the FF activate only on positive edges of the input. This can be done by defining a two variables ```ff_input``` and ```ff_previous_input``` and check for a positive edge with
>>>>>>> 7b5140664fa0ec9c10df743734622a245b74c7f6
# ```
# if(!ff_previous_input & ff_input) begin
#    //code on pose edge of ff_input 
# end
# ff_previous <= ff_input;
# ```
# 
# ## Synchronous Monostable Multivibrator
# ```{admonition} from [wikipedia](https://en.wikipedia.org/wiki/Monostable_multivibrator)
# A monostable multivibrator, also called a one shot or a monoflop, is a sequential logic electronic circuit that generates an output pulse. When triggered, a pulse of pre-defined duration is produced. The circuit then returns to its stable state and produces no more output until triggered again.
# ```
# 
# A useful application of monostable multivibrators is *debouncing circuits*[^debouncing].
# 
# ![Bouncing waveform when pressing or releasing a switch.](https://hackaday.com/wp-content/uploads/2015/11/debounce_bouncing.png?resize=800,280)
# 
# As it is shown in the image taken from [hackaday](https://hackaday.com/2015/12/09/embed-with-elliot-debounce-your-noisy-buttons-part-i/), when a button is pressed or released the circuit will sense multiple inputs due to the mechanical nature of buttons. When a correct detection is essential, it is usually essential to introduce a monostable multivibrator as a debouncing circuit. After the first pulse, the monostable will ignore any input, like the infamous bounces, up until a predetermined time has elapsed. This will guarantee that only one input is detected in the time frame chosen. The only job left is to find the appropriate window where the bounces are ignored but multiple consecutive presses are detected. If the button is pressed by a human, usually a few milliseconds will do the job.
# 
<<<<<<< HEAD
# [^debouncing]: Check [this video](https://www.youtube.com/watch?v=Nj-Q8FQxHhU) for a funny yet complete explanation.
=======
# [^debouncing]: Check [this video](https://www.youtube.com/watch?v=Nj-Q8FQxHhU) for a funny explanation
>>>>>>> 7b5140664fa0ec9c10df743734622a245b74c7f6
