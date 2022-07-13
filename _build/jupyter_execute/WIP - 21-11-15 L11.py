#!/usr/bin/env python
# coding: utf-8

# # Lecture 11 - 15 November 2021
# 
# ## INFORMATION THEORY
# 
# In this lecture Information theory will be introduced following the so called Shannon's approach.
# 
# ### definition
# **Information** is a measure of uncertainty on a random variable
# 
# ### Example: Fair coin vs fake coin
# 
# #### Fake coin (tail only)
# Assume to have a fake coin with head on both sides. The probability of obtaining tail or cross are
# \begin{align*}
# \mathcal{P}(\text{tail}) &= 1\\
# \mathcal{P}(\text{head}) &= 0\\
# \end{align*}
# 
# In other words **Information of \{"Tossing the coin"\}=0** because I already know what the result will be.
# 
# #### Fair coin
# In this case the probability of obtaining tail or cross are
# \begin{align*}
# \mathcal{P}(\text{tail}) &= 1/2\\
# \mathcal{P}(\text{head}) &= 1/2\\
# \end{align*}
# 
# **Information of \{"Tossing the coin"\}>0** because tossing the coin is an unpredictable process.
# 
# ### Ensamble of events
# 
# 
# 
