#!/usr/bin/env python
# coding: utf-8

# # Implementation of a stopwatch with LCD display
# ## Laboratory Class 03 - 12 October 2021
# 
# ### Topics
# - Finite-state machines.
# - Basic hardware circuits:
#     - data latches.
# - Verilog programming language:
#     - peripheral device drivers (ex.gr.: LCD driver with display of the lap mode).
# 
# ## Problems:
# - implementation of a synchronous 5-state finite-state machine with two pulse control;
# - final implementation of a stopwatch with 1/100 s resolution, start/stop, lap/reset function, and LCD display.
# 
# ---
# 
# ## Finite-state machines
# 
# ```{admonition} from [wikipedia](https://en.wikipedia.org/wiki/Finite-state_machine)
# A finite-state machine (FSM) or finite-state automaton (FSA, plural: automata), finite automaton, or simply a state machine, is a mathematical model of computation. It is an abstract machine that can be in exactly one of a finite number of states at any given time. The FSM can change from one state to another in response to some inputs; the change from one state to another is called a transition. An FSM is defined by a list of its states, its initial state, and the inputs that trigger each transition. Finite-state machines are of two types—deterministic finite-state machines and non-deterministic finite-state machines. A deterministic finite-state machine can be constructed equivalent to any non-deterministic one.
# ```
# Despite the long mathematical definition state machines are simpler than first expected. They just define how to switch from a state to an other depending on an event. Let's make and example with a well know state machine: Pac Man's ghosts:
# ![](https://miro.medium.com/max/1400/0*rVk-GYIMZJMD8Lxd)
# 
# The image taken from [a medium article](https://mark-truluck.medium.com/the-machine-in-the-ghost-46f856f94ed2) explains the behaviour of the ghosts with states and how they transition from one state to an other accordin to events.
# 
# States machines can be easily implemented with ```if-else```, ```switch``` construct and ```enums```. Each case correspond to a state and the condition to the event.
# 
# ## Data Latches
# A data latch is just a way to use D Flip-Flops to store data. Usually a data latch (or register) will store a new value only on a positive edge and will preserve the old value otherwise.
