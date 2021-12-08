#!/usr/bin/env python
# coding: utf-8

# # Lecture 08 - 18 October 2021
# 
# This lecture will be focusses on more examples and applications of the simulation theorem.
# 
# ## Low pass filter (again)
# \begin{align*}
#     \tilde{G}(\omega) &= \frac{1}{1-i\omega \tau} \quad \tau=\frac{1}{RC}\\
#     V(z)& =\frac{1-c}{2}\frac{z+1}{z-c} \qquad \text{with } c=\frac{1-T/2\tau}{1+T/2\tau} \\
# \end{align*}
# 
# ### Properties:
# 1. **Check reality**: as easy as checking $V^*(z^*)=V(z)$
# 2. **Check causality**: $\left( 0\not \in ROC; \infty\in ROC \right)$  
#   The pole is in $\tilde{z}=c=\frac{1-T/2\tau}{1+T/2\tau}\simeq1-\epsilon$ which is inside $\Gamma_1$ and one can always find a path $\Gamma$ such that $\tilde{z}\ um\ \Gamma \subset \Gamma_1$.
# 3. **Bico stability**: checked in the same way as causality
# 4. Behaviour at $\omega=\pm \frac{\pi}{T}$: fine due to backwrds interpretation of the simulation theorem.
# \begin{align*}
# \tilde{H}(\omega)= V\left( z=e^{-i\omega T}\right)=\frac{1-c}{2}
# \end{align*}

# In[1]:


from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

T=1/1024 # Sampling time
omega = np.arange(start=np.log10(5), stop=np.log1o(0.91*np.pi/T), step=T)
f3dB = 10 # Hz

omega0=2*np.pi*f3dB
tau = 1/(2*np.pi*f3dB)
##print("T=\t{:e}\ntau=\t{:e}".format(T, tau))
fig, ax = plt.subplots(1, 2, figsize=(15, 5))


lp = 1/(1-1j*omega*tau) # Ideal Low pass 
mag_lp = 20*np.log10(np.abs(lp))
phase_lp = np.arctan(np.imag(lp)/np.real(lp))*180/np.pi


c = (1-T/(2*tau) ) / (1+T/(2*tau) )
lp_bt = 0.5*(1-c)*(np.exp(-1j*omega*T)+1 )/( c*np.exp(-1j*omega*T)-1)
mag_lp_bt = 20*np.log10(np.abs(lp_bt))
phase_lp_bt = -1*np.arctan( np.imag(lp_bt)/np.real(lp_bt))*180/np.pi


ax[0].semilogx(omega, mag_lp, label="LP")    # Bode magnitude plot
ax[0].semilogx(omega, mag_lp_bt, "--", label="Bilinear")    # Bode magnitude plot

ax[1].semilogx(omega, phase_lp, label="LP")
ax[1].semilogx(omega, phase_lp_bt, "--", label="Bilinear")

ax[0].vlines(omega0, min(mag_lp_bt), 20*np.log10(np.abs(1/(1-1j))),linestyles=":", label=r"$2\pi f_{3dB}$")
ax[1].vlines(omega0, 0, 45, linestyles=":", label=r"$2\pi f_{3dB}$ [$\simeq$45°]")


ax[0].set_title("Magnitude");  ax[1].set_title("Phase")
ax[0].set_xlabel(r"$\omega$ [Hz]"); ax[0].set_ylabel(r"Magnitude [dB]");
ax[1].set_xlabel(r"$\omega$ [Hz]"); ax[1].set_ylabel(r"Phase [deg°]");
ax[0].grid();   ax[1].grid()
ax[0].legend(); ax[1].legend()

fig.tight_layout()
plt.show()

