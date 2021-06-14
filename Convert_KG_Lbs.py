weight = input("Weight: ")
KG_OR_LBS = input("(K)g or (L)bs: ")
weight
KG_OR_LBS = KG_OR_LBS.upper()
if KG_OR_LBS.__eq__("K"):
    converted = float(weight) / 0.45
    print("Weight in Lbs: " + str(converted))
elif KG_OR_LBS.__eq__("L"):
    converted = float(weight) * 0.45
    print("Weight in Kgs: " + str(converted))