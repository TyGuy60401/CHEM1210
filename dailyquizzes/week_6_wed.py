from tydtools.chemLib import *

def q1():
    print("sol")
    print("insol")
    print("sol")
    print("sol")
    print("insol")
    print("sol")
    return

def q2(vol, m):
    print(vol * m * molar_mass("CoS"), "grams")
    return

def q3(mass, vol1, vol2, m2):
    m = mass / molar_mass("MgCl2") / vol1
    moles = m * vol2
    moles2 = 2 * moles
    vol2 = moles2 / m2
    print(vol2, "L")
    return

def q4():
    print("NH4+")
    print("SO4 2-")
    return

def q5():
    print("Mg2+ aq")
    print("CO3 2- aq")
    print("McGO3 s")
    return

def q6(mass1, mass2):
    moleses = {
        'Ca(OH)2': mass1 / molar_mass('Ca(OH)2'),
        'AgNO3': mass2 / molar_mass('AgNO3') / 2
    }
    index = int(input(f"0 - Ca(OH)2 {moleses['Ca(OH)2']}\n1 - AgNO3 {moleses['AgNO3']}\n0 or 1 is less?  "))
    moles = moleses[list(moleses.keys())[index]]

    if index == 1:
        final_moles = 2 * moles
    else:
        final_moles = moles
    
    print(final_moles * molar_mass("AgOH"))

    return

q1()
print("")

q2(0.508, 1.39)
print("")

q3(1.34, 1.0, 0.017, 0.1)
print("")

q4()
print("")

q5()
print("")

q6(9.35, 7.82)