import numpy as np
import math as mt
from scipy.stats import norm
from scipy import integrate
from matplotlib import pyplot


## punto A

# Parametri (parte 2)
lgd = 0.60
X0 = 100
K = 95
sigma = 20
T = 2
t = 0
# Parametri dei CDS (parte 1)
r = 0.03
lambda1 = 0.0255

# Funzione per calcolare il prezzo del derivato con dinamica Bachelier
def prezzo_bc(X0, K, sigma, t):
    b1 = (X0 - K)/(sigma*mt.sqrt(t))
    return (X0 - K)*norm.cdf(b1) + sigma*mt.sqrt(t)*norm.pdf(b1)

# Calcolo valore CVA
integranda = lambda s: prezzo_bc(X0, K, sigma, s)*lambda1*mt.exp(-lambda1*s)
CVA = - lgd*mt.exp(-r*T)*integrate.quad(integranda, t, T)[0]

print ("Prezzo CVA:", CVA)

'''
#DA RIVEDERE!!

N = 100000
dt = T/N

#simulazione dei tempi di fallimento
default_times = np.random.uniform(0, T, N)    #RAMDOMICO !

#calcolo del CVA per ciascuna realizzazione
CVA_simulazioni = []
for i in range(N):
    default_time = default_times[i]
    default_indicator = default_time <= T
    EAD_i = EAD * default_indicator
    PD_i = norm.cdf((np.log(X_0 / K) + (r - 0.5 * sigma**2) * T) / (sigma * np.sqrt(T)))
    CVA_i = calcolo_CVA(-LGD, PD_i, EAD_i, r, T)
    CVA_simulazioni.append(CVA_i)

#calcolo dell'intervallo di confidenza al 98% per il CVA
lower_bound = np.percentile(CVA_simulazioni, 1)
upper_bound = np.percentile(CVA_simulazioni, 99)

print("L'intervallo di confidenza al 98% per il CVA:", (lower_bound, upper_bound))


'''
