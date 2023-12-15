h = 6.63e-34
c = 2.9979e8
avo = 6.022e23

def q3(e):
    v = e / h
    print(f"{v:.4e} Hz")

def q4(n, lamb):
    v = c / lamb
    e = h * v
    e_total = e * n * 1e-6 * avo
    print(f"{e_total:.3f} J")

def q5(kcals, lamb):
    cals = kcals * 1000
    e_tot = cals * 4.184

    f = c / lamb
    e_1 = h * f
    e_ratio = e_tot / e_1
    moles = e_ratio / avo
    print(moles)



q3(3.58e-19)
q4(9.32, 400e-9)
q5(240, 53.34e-9)