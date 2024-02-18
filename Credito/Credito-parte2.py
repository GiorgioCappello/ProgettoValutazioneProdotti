import numpy as np
import math as mt
from scipy.stats import norm
from scipy import integrate
import matplotlib.pyplot as plt


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

## Parte 2

N = 100000
K = 1000

# Simulazione dei tempi di fallimento
U = np.random.uniform(0,1,N)
tau = -1/lambda1 * np.log(1-U)

# Istogramma
plt.hist(tau, bins=K)
plt.xlabel('Tempi di default')
plt.ylabel('Numbero di volte osservato')
plt.title('Tempi di default')
plt.show()

# Calcolo della probabilità empirica dei tempi di default nei singoli intervalli
counts, _ = np.histogram(tau, bins=K)

# Calcolo delle probabilità relative
prob = counts / N

# Funzione per simulazione del sottostante
def sottostante(X0, sigma, t, z):
    return X0 + sigma*mt.sqrt(t)*z

# Prezzo sottostante
I = []
for i in range(1,N):
    z = np.random.normal()
    t = (tau[i-1] + tau[i])/2
    X = sottostante(X0, sigma, t, z)
    I.append(prezzo_bc(X, K, sigma, t)*np.exp(-r*t))


'''
#calcolo dell'intervallo di confidenza al 98% per il CVA
lower_bound = np.percentile(CVA_simulazioni, 1)
upper_bound = np.percentile(CVA_simulazioni, 99)

print("L'intervallo di confidenza al 98% per il CVA:", (lower_bound, upper_bound))
'''