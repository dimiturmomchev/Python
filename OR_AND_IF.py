has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income or has_good_credit:
    print("Eligible for loan")

print("\n")

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")