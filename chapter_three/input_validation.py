passes = 0
failures = 0

for student in range(10):
    result = 0
    while result != 1 and result != 2:
        result = int(input('Enter result (1 = pass, 2 = fail): '))

    if result == 1:
        passes += 1
    else:
        failures += 1
print('passed: ', passes)
print('failed: ', failures)

if passes >= 8:
    print('bonus to instructor')
else:
    print('instructor need to do more better job')
