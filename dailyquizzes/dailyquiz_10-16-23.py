from tydtools import chemLib as cl

def q1(mass, cs, tempi, tempf):
    q = mass * cs * (tempf - tempi)
    print(f"Q1: {q:.2f} J")

def q2(mass, cs, tempi, q):
    tempf = q*1e3 / (mass * cs) + tempi
    print(f"Q2: {tempf:.4f} deg C")

def q4(mass1, cs1, tempi1, tempi2, tempf):
    q1 = mass1 * cs1 * (tempf - tempi1)
    q2 = -q1
    mass2 = q2 / (4.184 * (tempf - tempi2))
    print(f"Q4: {mass2:.2f} g")

def q5(v1, t1, v2, t2, tf):
    deltat = tf - t1

q1(10.481, 1.105, 31.702, 22.753)
q2(273.07, 4.186, 5.3, 66.93)
q4(29.41, 0.727, 82.98, 10.46, 27.57)
q5(0, 0, 0, 0, 0)
