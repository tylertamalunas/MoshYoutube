# if applicant has high income AND good credit
#     Eligible for loan
has_high_income = False
has_good_credit = True
has_criminal_record = True

if has_high_income and has_good_credit:
    print("Eligible for loan")

# if applicant has high income or good credit
#       Eligible
if has_high_income or has_good_credit:
    print("Eligible")

#if applicant has good credit AND doesnt have a criminal record
if has_good_credit and not has_criminal_record:
    print("He is eligible")

# AND: both
# OR: at least one
# NOT: