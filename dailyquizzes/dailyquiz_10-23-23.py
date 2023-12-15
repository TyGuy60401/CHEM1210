import matplotlib as mpl
H = 6.63e-34
c = 2.9979e8
avo = 6.022e23


formatter = mpl.ticker.EngFormatter()

def calc_wavelength(ni, nf):
    deltaE = -2.18e-18 * (1/(nf**2) - 1/(ni**2))
    v = deltaE / H
    # v = c / lambda
    # lambda = c / v
    lamb = c / v

    print(f"Delta E: {deltaE:.3e}")
    print(f"Lambda: {formatter(lamb)}")

def q1(ni, nf):
    calc_wavelength(ni, nf)

def q2(ni, nf):
    calc_wavelength(ni, nf)


q1(5, 2)
q2(1, 3)