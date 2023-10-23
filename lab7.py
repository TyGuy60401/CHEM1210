import numpy as np


def part1(cal, calncold, calnboth, tcold, thot, tfinal):
    deltathot  =  tfinal - thot
    deltatcold =  tfinal - tcold

    mcold = calncold - cal
    mhot = calnboth - calncold

    qhot = mhot * 4.184 * deltathot
    qcold = mcold * 4.184 * deltatcold

    qcal = -qhot - qcold
    Ccal = qcal / deltatcold
    print(f"DeltaTHot: {deltathot:.3f}")
    print(f"DeltaTCold: {deltatcold:.3f}")
    
    print(f"Qhot: {qhot:.3f}")
    print(f"Qcold: {qcold:.3f}")
    print(f"Qcal: {qcal:.3f}")
    print(f"Ccal: {Ccal:.3f}")
    print("\n")
    return Ccal


run1p1 = [19.783, 49.88, 79.420, 11.8, 44.2, 26.9]
run2p1 = [19.855, 46.860, 72.885, 12.5, 42.9, 26.6]
run3p1 = [19.862, 48.588, 78.928, 13.1, 41.0, 26.5]
runsp1 = [run1p1, run2p1, run3p1]

ccals = []
for run in runsp1:
    ccals.append(part1(*run))

total_ccals = sum(ccals)
print(f"Avg Ccal: {total_ccals/3:.3f}")


Ccal = 13.76
def part2(volhcl, volnaoh, mhcl, mnaoh, tinaoh, tihcl, tf):
    ""
    deltathcl = tf - tihcl
    deltatnaoh = tf - tinaoh

    cs = 4.184

    qhcl = mhcl * cs * deltathcl
    qnaoh = mnaoh * cs * deltatnaoh

    qcal = 13.76 * deltathcl

    qrxn = -qhcl - qnaoh - qcal
    deltah = qrxn / 0.02 / 1000
    print(f"Qrxn: {qrxn:.3f}\tDeltaH: {deltah:.3f}")
    print("")
    return qrxn, deltah
    

run1p2 = [20, 20, 20.233, 20.735, 21.1, 21.2, 27.6]
run2p2 = [20, 20, 20.227, 20.669, 21.0 ,21.4, 27.8]
run3p2 = [20, 20, 20.291, 20.669, 21.0, 21.3, 27.7]
runsp2 = [run1p2, run2p2, run3p2]

run1p2 = [40, 40, 40.233, 20.735, 21.1, 21.2, 27.6]
run2p2 = [40, 40, 40.227, 20.669, 21.0 ,21.4, 27.8]
run3p2 = [40, 40, 40.291, 20.669, 21.0, 21.3, 27.7]
runsp2 = [run1p2, run2p2, run3p2]

print("Part 2:")
qrxns = []
deltaHs = []
for run in runsp2:
    qrxns.append(part2(*run)[0])
    deltaHs.append(part2(*run)[1])

q_avg = np.average(qrxns)
q_std = np.std(qrxns)

h_avg = np.average(deltaHs)
h_std = np.std(deltaHs)
print(f"Qrxn avg: {q_avg}")
print(f"Qrxn std: {q_std}")
print("")
print(f"deltaH avg: {h_avg}")
print(f"deltaH std: {h_std}")