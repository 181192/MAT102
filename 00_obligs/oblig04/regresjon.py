# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 13:22:24 2017
@author: kathi
"""
from pydataset import data
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sci

cars = data('cars')
# Speed numeric Speed - mph
x = cars.speed
# dist numeric Stopping distance -ft
y = cars.dist

def graph_style():
    # Graph size adjustment
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 1, 1)
    # Major ticks every 5
    # Minor ticks every 1
    major_ticks = np.arange(0, 125, 5)
    minor_ticks = np.arange(0, 125, 1)
    # Graph visual setup
    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)
    ax.tick_params(which='both', direction='out')
    # grid visibility
    ax.grid(which='both')
    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)
    # Graph labels
    plt.ylabel('Stopping distance in ft')
    plt.xlabel('Car speed in mph')
    plt.plot(x, y, 'o', label='Data fra Cars observasjon')

def calculatedY(n):
    n = n * 1.5 + ((n ** 2) / (2 * 0.7 * 9.81665))
    return n

graph_style()
print('Oppgave 1 - Regresjon ')
print('a)')
plt.legend()
plt.show()


print('b)')
p1 = np.polyfit(x, y, 1)
print('Lineær: ')
print('     Slope and Intercept:')
print(p1)
graph_style()
plt.plot(x, np.polyval(p1, x), 'r-', label='Lineær Regresjon')
plt.legend()
plt.show()


p2 = np.polyfit(x, y, 2)
print('Kvadratisk: ')
print('     Coefficients:')
print(p2)
graph_style()
plt.plot(x, np.polyval(p2, x), 'b--', label='Kvadratisk Regresjon')
plt.legend()
plt.show()


p3 = np.polyfit(x, y, 3)
print('Kubisk: ')
print('     Coefficients:')
print(p3)
graph_style()
plt.plot(x, np.polyval(p3, x), 'm:', label='Kubisk Regresjon')
plt.legend()
plt.show()

graph_style()
plt.plot(x, np.polyval(p1, x), 'r-', label='Lineær Regresjon')
plt.plot(x, np.polyval(p2, x), 'b--', label='Kvadratisk Regresjon')
plt.plot(x, np.polyval(p3, x), 'm:', label='Kubisk Regresjon')
plt.legend()
plt.show()

# c) utifra determinasjonskoeffisienten ser kvadratisk regresjonskurve best ut
print('R^2:')
slope, intercept, r_value, p_value, std_err = sci.linregress(x,y)
print('R_value^2 Lineær:')
print(pow(r_value,2))

print('\nR^2 Lineær:')
slope, intercept, r_value, p_value, std_err = sci.linregress(x,np.polyval(p1,x))
print('R_value^2 Lineær:')
print(pow(r_value,2))

print('\nR^2 Kvadratisk:')
slope, intercept, r_value, p_value, std_err = sci.linregress(x,np.polyval(p2,x))
print('R_value^2 Kvadratisk:')
print(pow(r_value,2))

print('\nR^2 Kubisk:')
slope, intercept, r_value, p_value, std_err = sci.linregress(x,np.polyval(p3,x))
print('R_value^2 Kubisk:')
print(pow(r_value,2))

print('\nVi ser at den kvadratiske tilnærmingen oppfyller med 97.5% nyaktighet\n')

# d) 43 ft
# e)
# print(calculatedY(x))
graph_style()
plt.plot(x, calculatedY(x), 'r-', label='Kalkulert bremselengde fra formel n = n * 1.5 + ((n**2)/(2*0.7*9.81665)')
print('e)')
plt.legend()
plt.show()

# Den kvadratiske regresjonskurven er jevn med den kalkulerte kurven.
graph_style()
plt.plot(x, calculatedY(x), 'r-', label='Kalkulert bremselengde fra formel n = n * 1.5 + ((n**2)/(2*0.7*9.81665)')
plt.plot(x, np.polyval(p2, x), 'b--', label='Kvadratisk Regresjon')
print('Kvadratisk Regresjon og kalkulert bremselengde: ')
plt.legend()
plt.show()
