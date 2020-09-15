from api.models import pi

def resPi(pinIn, pinOut, status):
    sts = True
    print("PIN IN >>", pinIn)
    print("PIN Out >>" , pinOut)
    print("Status >>" ,status)
    if status== 1:
        sts = False
    if pinOut == 0:
        pi.setup(pinIn, pi.IN)
        print("---------  Pin select for Input  ---------------")
    else:
        pi.setup(pinIn, pi.OUT)
        print("---------  Pin select for Output  ---------------")
    # Input from pin 11
    pinStatus = pi.input(pinIn)
    print(pinStatus,">>")
    if not pinStatus:
        print("condition is false")
        pi.output(pinOut, sts)
        pi.cleanup()
        return False
    else:
        print("Condition is True")
        pi.output(pinOut, sts)
        pi.cleanup()
        return True