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
    else:
        pi.setup(pinIn, pi.OUT)
    # Input from pin 11
    pinStatus = pi.input(pinIn)
    if not pinStatus:
        pi.output(pinOut, sts)
        return False
    else:
        pi.output(pinOut, sts)
        return True