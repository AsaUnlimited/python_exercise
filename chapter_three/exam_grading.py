no_of_student = 0
fail_count = 0
pass_count = 0

while no_of_student <= 10:
    pass_fail = int(input("Enter 1 for pass and 2 for fail or enter -1 to terminate: "))
    if pass_fail == 1:
        pass_count += 1
    elif pass_fail == 2:
        fail_count += 1
    else:
        print("invalid input")
    no_of_student += 1

print(f"the number of student that pass is {pass_count} and the number of student that failed is {fail_count}")

if pass_count >= 8:
    print("Bonus to the instructor")
else:
    print("too many student fail your course")
