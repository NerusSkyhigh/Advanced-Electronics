#!/usr/bin/env python
# coding: utf-8

# # Lecture 02 - 14 September 2021
# 
# In the previous lecture we gave some basic definitions and showed that a LTI system is fully characterized by its **impulse response**.
# 
# An interesting property of LTI systems is that it is possible to imagine them the impulse response and the input sequence as the two inputs of a convolution. This means that is is possible to freely swap the input sequence and the impulse response.
# 
# \begin{align*}
#     x[n] \rightarrow [SYSTEM] \rightarrow y[n] &\implies (x[n], h[n]) \rightarrow [CONVOLUTION] \rightarrow y[n] \\
#     &\implies (h[n], x[n]) \rightarrow [CONVOLUTION] \rightarrow y[n]
# \end{align*}
# 
# Matematically:
# \begin{align*}
#     y[n] = \sum_{k=-\infty}^{\infty} x[n] h[n-k]\quad \xrightarrow[k'=n-k]{k=k'-n} \quad \sum_{k'=-\infty}^{\infty} x[n-k'] h[k']
# \end{align*}
# 
# We will now discuss three important features that a system can have, namely **reality**, **causality / non causality** and **marginal stability / bibo stability**.
# 
# ## Key properties of a system
# 
# ### Reality
# A system is said to be real iff $h[n]\in \mathcal{R}$.
# 
# ### (Non) Causality
# A system is said to be causal (or nonanticipative) iff $h[n] = 0 \textit{ if } n<0$. An equivalent definition is: the output $y[n_{0}]$ depends on only the input $x[n]$ for values of $n < n_{0}$. The idea behind this property is that the output depends only on past inputs and not on future inputs.
#  
# 
# A non causal system is defined **by substituting the "less than" with a "greater than"**: <br/>
# A system is said to be causal (or nonanticipative) iff $h[n] = 0 \textit{ if } n>0$. An equivalent definition is: the output $y[t_{0}]$ depends on only the input $x[n]$ for values of $t>n_{0}$.
# 
# 
# ```{note}
# A system can be BOTH causal and NON CAUSAL. A class of systems that satisfy this properties are amplifiers $h[n]= \alpha\ \delta[n]$. These kind of systems respect both conditions as the have $h[n]=0$ for both $t<0$ and $t>0$.
# ```
# 
# ### Marginal Stability
# A system is marginal stable iff $\exists L<+\infty\ :\ |h[n]| \leq L\ \forall n$.
# 
# An example of marginal stable system is one with $h[n]=U[n]\leq 1$ (*the integrator*):
# \begin{equation*}
#     y[n] = \sum_{k=-\infty}^{+\infty} x[k] U[n-k] = \sum_{k=-\infty}^{n} x[k]
# \end{equation*}
# 
# ### BIBO Stability
# A system is BIBO Stable (Bounded Input - Bounded Output) if to each and every bounded input $x[n]$ it corresponds a bounded output.
# \begin{equation*}
#     \forall\ x[n]\ :\ |x[n]|<+\infty \implies \exists L<\infty\ :\ |y[n]|<L \forall n
# \end{equation*}
# 
# #### e.g. BIBO Stable system 
# An amplifiers is a BIBO stable system (trivial if we take$L=\max_{n}\{x[n]\}\times\alpha$) but an integrator is not. If we choose $x[n]=U[n]$ we have:
# \begin{equation*}
#     y[n] = \sum_{k=-\infty}^{n} U[k] = \sum_{k=0}^{n} 1 = n+1
# \end{equation*}
# so I can just choose $n=L$ to "surpass" every $L$ I've chosen.
# 
# ### Th: BIBO Stability
# ```{admonition} Theorem
# Condition sufficient and necessary for a system to be BIBO Stable is that $h[n]$ is **absolutely convergent**, that is $\exists L <\infty\ :\ \sum_{n}|h[n]| \le L$.
# ```
# 
# #### Proof of sufficiency ($\impliedby$)
# Assume the input sequence to be bounded $|x[n]| \leq L\in\mathcal{R}^{+}\ \forall n$ and apply the Cauchy–Schwarz inequality:
# 
# \begin{align*}
#     |y[n]| = |\sum_{k} h[k] x[n-k]| \leq \sum_{k} |h[k]|\ |x[n-k]| \leq \max_{k}\{h[k]\} \sum_{k} |h[n-k]| \leq \max_{k}\{h[k]\} L < +\infty
# \end{align*}
# 
# 
# #### Proof of necessity ($\implies$)
# The proof of necessity is a bit trickier. Instead of the direct why we will work "ad absurdum" by proving that *if $h[k]$ is NOT absolutely convergent then the system is NOT BIBO stable*. This proof works because the other cases were already taken care of [^cases].
# 
# [^cases]: Let's list the cases for clarity's sake:
#     - $h[k]$ is NOT absolutely convergent $\implies$ S is NOT BIBO stable: it's the proof
#     - $h[k]$ is absolutely convergent $\implies$ S is NOT BIBO stable: impossible for the "Proof of sufficiency"
#     - $h[k]$ is NOT absolutely convergent $\implies$ S is BIBO stable: it's in the proof
#     - $h[k]$ is absolutely convergent $\implies$ S is BIBO stable: that's what we are aiming for
#     
# Let's consider a sequence defined as:
# \begin{equation}
#     x[n] = \left\{\begin{array}{lr}
#         \frac{h^*[-n]}{|h[-n]|} \quad \textit{if} \quad |h[-n]|\neq 0\\
#         0  \quad \textit{if} \quad |h[-n]| = 0\
#         \end{array}\right.
# \end{equation}
# Now we evaluate the output of said system in n=0 and use the fact that $h[n]$ is NOT absolutely convergent:
# \begin{align*}
#     y[n] = \sum_{k} h[k] \frac{h^*[k-n]}{|h[k-n]|} \rightarrow y[0] = \sum_{k} h[k] \frac{h^*[k]}{|h[k]|} = \sum_k |h[k]| = +\infty
# \end{align*}
# 
# With this this we proved that if $h[k]$ is not absolutely convergent then the system can not be BIBO stable.
# 
# 
# ### Stability of a sequence
# 
# Sometime we will talk about BIBO stability of a sequence. In this context it means $\sum_n |x[n]| < +\infty$.
# 
# 
# ## Difference equations
# 
# TBA
