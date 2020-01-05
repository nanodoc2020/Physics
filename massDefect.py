# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 15:57:48 2020
massDefect takes a number of protons, neutrons or electrons, and calculates the mass
defect for a nucleus composed of those individual nucleons. The inputs are
number of particle 1, type of particle 1, number of particle 2, type of 
particle 2, "p","n", or "e". The known mass of the resulting particle in kg
and u are then entered. 
@author: Erik Larsen
"""

def massDefect(n1,p1,n2,p2,known_mass,known_massu):
    #Define the masses:
    import scipy.constants as sc
    if p1=="p":
        m1=sc.proton_mass
        [m1u,a,b]=sc.physical_constants["proton mass in u"]
        print("\nProton mass: ",m1,"kg;",m1u,"u")
    elif p1=="n":
        m1=sc.neutron_mass
        [m1u,a,b]=sc.physical_constants["neutron mass in u"]
        print("\nNeutron mass: ",m1,"kg;",m1u,"u")
    else:
        m1=sc.electron_mass
        [m1u,a,b]=sc.physical_constants["electron mass in u"]
        print("\nElectron mass",m1,"kg;",m1u,"u")
        
    if p2=="p":
        m2=sc.proton_mass
        [m2u,a,b]=sc.physical_constants["proton mass in u"]
        print("Proton mass: ",m2,"kg;",m2u,"u")
    elif p2=="n":
        m2=sc.neutron_mass
        [m2u,a,b]=sc.physical_constants["neutron mass in u"]
        print("Neutron mass: ",m2,"kg;",m2u,"u")
    else:
        m2=sc.electron_mass
        [m2u,a,b]=sc.physical_constants["electron mass in u"]
        print("Electron mass",m2,"kg;",m2u,"u")
    
    amu=sc.physical_constants["atomic mass constant energy equivalent in MeV"]
    amu=amu[0]
    sum1=n1*m1+n2*m2
    sum1u=n1*m1u+n2*m2u
    print("\nThe individual masses sum to: ",sum1,"kg;",sum1u,"u; \nbut the known mass is: ", known_mass,"kg;",known_massu,"u.")
    massD=sum1-known_mass
    massDu=sum1u-known_massu
    print("\nThe mass defect is: ",massD,"kg;",massDu,"u.")
    print("This missing mass is converted into the binding energy:")
    E=round(massDu*amu,3)
    EJ=E*1.60218*10**-19
    print("\nE=",EJ,"J\nE=",E,"MeV.")
    Epn=round(E/(n1+n2),3)
    print("The binding energy per nucleon is",Epn,"MeV." )
    
    
