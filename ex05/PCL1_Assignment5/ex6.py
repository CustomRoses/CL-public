def A(TP, TN, FP, FN):
    if TP + FP + FN + TN == 0:
        return 0
    return (TP + TN) / (TP + TN + FP + FN)


def P(TP, FP):
    if TP + FP == 0:
        return 0
    return TP / (TP + FP)


def R(TP, FN):
    if TP + FN == 0:
        return 0
    return TP / (TP + FN)


def F(TP, FP, FN):
    if TP + FP + FN == 0:
        return 0
    return 2 * P(TP, FP) * R(TP, FN) / (P(TP, FP) + R(TP, FN))


print("POS\t\tA\t\tP\t\tR\t\tF")
print("-" * 35)
with open("measurement_data.txt", "r") as f:
    BA = 0
    BP = 0
    BR = 0
    BF = 0
    for line in f.readlines():
        POS, TP, FP, TN, FN = line.split("\t")
        if POS == "POS":
            continue
        TP = int(TP)
        FP = int(FP)
        TN = int(TN)
        FN = int(FN)
        Ax, Px, Rx, Fx = A(TP, TN, FP, FN), P(TP, FP), R(TP, FN), F(TP, FP, FN)
        if Ax > BA:
            BA = Ax
        if Px > BP:
            BP = Px
        if Rx > BR:
            BR = Rx
        if Fx > BF:
            BF = Fx
        if len(POS) < 4:
            POS = POS + " " * (4 - len(POS))
        print("{}\t{:.2f}\t{:.2f}\t{:.2f}\t{:.2f}".format(POS, Ax, Px, Rx, Fx))
    print("-" * 35)
    print("Largest A Value: {:.2f}".format(BA))
    print("Largest P Value: {:.2f}".format(BP))
    print("Largest R Value: {:.2f}".format(BR))
    print("Largest F Value: {:.2f}".format(BF))
