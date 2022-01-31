#!/usr/bin/env python
# coding: utf-8

# # Digital Filters
# 
# ---
# 
# # Implementation of a harmonic oscillator
# 
# ## Laboratory Class 05 - 14 October 2021
# 
# ### Topics
# - Theoretical and experimental aspects linked to the development of a harmonic oscillator:
#     - general discussion on the difficulty of implementing an oscillator;
#     - from the differential equation of a forced oscillator to the z–transform of the simulator response function V (z);
#     - derivation of the difference equation;
#     - setting of the boundary conditions for the cosine operation;
#     - dependency of the working frequency $f_0 = \frac{ω_0}{2\pi}$ on the parameter k, provided that $ω_0T ≪ 1$: and $f_0 = f_s/\left( 2^{\frac{k}{2}+1}\pi\right)$, with $f_s = 1/T$.
# 
# 
# ## Problems
# - implementation and characterization of a harmonic oscillator.
# 
# 
# ---
# 
# ## Harmonic Oscillator
# 
# ### Differential Equation
# Let's start by writing the differential equation into the "Laplace" space or "s-space". In this case the Fourier transform is not enough because it can not handle initial conditions.
# 
# \begin{align*}
#  \mathcal{L} \left\{ \ddot{x}+\omega_0 x\right\} &= s^2 \tilde{x}(s)-s x_0 - \dot{x}_0 + \omega_0^2\tilde{x}(s) = 0 \\
#  &\\
#  \tilde{x}(s)&=\frac{sx_0 + \dot{x}_0}{s^2+\omega_0^2}
# \end{align*}
# 
# 
# ### Bilinear transform
# It is possible to obtain the approximate transfer function by applyng the bilinear transform
# \begin{align*}
#  \omega = \frac{2i}{T}\frac{z-1}{z+1} + \mathcal{o}\left(\omega^3 T^3\right) \qquad s=-i\omega = + \frac{2}{T}\frac{z-1}{z+1}
# \end{align*}
# 
# After the sobstitution we obtain:
# \begin{align*}
#     V(z) &= \frac{Y(z)}{X(z)}= \frac{ (z+1)^2 T/4}{(z-1)^2 + (z+1)^2 \left(\frac{\omega T}{2}\right)}\\
#     \implies&Y(z)\left( 1-\frac{2c}{z}-\frac{1}{z^2}\right) = \frac{N(z)}{z^2} \\
#     \text{with}\qquad& c=(1-\frac{\omega_0^2 T^2}{4})/(1+\frac{\omega_0^2 T^2}{4})
#     &N(z)=\frac{(z+1)^2 T/4}{1+\frac{\omega_0^2 T^2}{4}}
# \end{align*}
# 
# By inverting the z-transform we get:
# \begin{align*}
#     y[n]-2cy[n-1]+y[n-2]=\text{boundary conditions}[n]
# \end{align*}
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
