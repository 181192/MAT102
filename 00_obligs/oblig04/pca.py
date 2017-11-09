# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 00:42:37 2017
@author: kathi
"""
import numpy as np
import scipy.io
import matplotlib.pyplot as plt
# from matplotlib.mlab import PCA
import scipy.linalg as sl

# Principal component analysis
# X = np.array-type, meanCentered, a = antall komponenter
# Kall: [scores, loadings, error] = pca(X)
def pca(X, a = 3, tol = 0.0001):
    X = np.array(X)
    E = X
    [n,m] = X.shape
    T = np.zeros([n,a])
    P = np.zeros([m,a])
    for i in range(a):
        t_new = np.random.rand(n)
        for iter in range(1000):
            t = t_new
            p = np.dot(E.T,t)
            p = p/sl.norm(p)
            t_new = np.dot(E,p)
            if sl.norm(t-t_new) <= tol:
                break
        else:
            raise Exception("Something went wrong")
        T[:,i] = t
        P[:,i] = p
        E = E - np.dot(t.reshape([n,1]),p.reshape([1,m]))
    return [T,P,E] # X = T*P.T + E

# For å sikre at søylene i X har middel = 0
# Typisk kall: X = meanCenter(X)
def meanCenter(X):
    X = np.array(X)
    return X - np.mean(X, axis = 0)

# For å sikre at søylene i X har standardavvik 1
# Typisk kall: X = standardize(X)
def standardize(X):
    # X allerede meanCentered
    stdX = np.std(X, axis=0)
    stdX[stdX == 0] = 1
    return X/stdX


data = scipy.io.loadmat('Innlevering4.mat')
X1 = np.array(data['X1'])
data['objNames1']
data['varNames1']
print('Oppgave 2 - Prinsipalkomponentanalyse ')
print('a)')
print('Matrise før standarisering: ')
print(np.matrix(X1))
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1)
plt.plot(X1, 'o')
plt.show()
X1 = ((X1-np.mean(X1))/np.std(X1))
print('-------------------------------------------------------------------')
print('Matrise etter standarisering: ')
print(np.matrix(X1))

# B) Standardization is important because you want the testing data on the
# same "scale" to make them possible to compare as equals.
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1)
plt.plot(X1, 'o')
plt.show()

# 2C)
plt.figure(1)
[T,P,E] = pca(X1, a=2)
plt.scatter(T[:, 0], T[:, 1])
for label, x, y in zip(data["objNames1"], T[:, 0], T[:, 1]):
    plt.annotate(
        label, 
        xy = (x, y), xytext = (5, -3),
        textcoords = 'offset points', ha = 'left')
    
# d: Svar: Markørene for 5a og 5b overlapper hverandre, så ja.
# e:
totalVar = np.trace(np.dot(X1, X1.T))
explainedVar = np.trace(np.dot(T, T.T))
percentageExplained = explainedVar/totalVar # 0.99
# f: 
plt.figure(2)
plt.scatter(P[:, 0], P[:, 1])
for label, x, y in zip(data["varNames1"], P[:, 0], P[:, 1]):
    plt.annotate(
        label, 
        xy = (x, y), xytext = (5, -3),
        textcoords = 'offset points', ha = 'left')
#Mulige kommentarer: melkeinnhold, kakaoinnhold og sukkerinnhold som
#fysiske målinger peker i samme retning som innstillingene ekstra melk,
#ekstra kakao og ekstra sukker.
#cocoa-odour peker omtrent i samme retning som den fysiske kakao-målingen
#sweet og milk-taste ligger begge omtrent midt mellom sukker og
#melk-innhold.
        
# g og h:
X2 = np.array(data['X2'])
X2 = meanCenter(X2)
X2 = standardize(X2)
plt.figure(3)
[T,P,E] = pca(X2, a=2)
plt.scatter(T[:, 0], T[:, 1])
for label, x, y in zip(data["objNames2"], T[:, 0], T[:, 1]):
    plt.annotate(
        label, 
        xy = (x, y), xytext = (5, -3),
        textcoords = 'offset points', ha = 'left')
plt.figure(4)
plt.scatter(P[:, 0], P[:, 1])
for label, x, y in zip(data["varNames2"], P[:, 0], P[:, 1]):
    plt.annotate(
        label, 
        xy = (x, y), xytext = (5, -3),
        textcoords = 'offset points', ha = 'left')
# h: Svar: fra figuren ser vi et veldig klart skille mellom stoffene med og
# uten tilsetting i andre komponent.    
    
    