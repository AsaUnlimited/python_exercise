try:
    foobar
except:
    print("PROBLEM!")
print("after the try")

d = {"lagos": "ikeja"}


def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None


while True:
    try:
        num = int(input("Enter a number: "))
    except:
        print("Thats not a number")
    else:
        print("I'm in the else block, i run if theres no error")
        break
    finally:
        print("I run no matter what!")
print("next line prints after the entire block")

print(get(d, "city"))
