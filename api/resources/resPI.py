from api.models import pi

def resPi(pinIn, pinOut, status):
    sts = 1
    if status== 1:
        sts = 0
    pi.setup(pinIn, pi.IN)
    pi.setup(pinOut, pi.OUT)
    # Input from pin 11
    pinStatus = pi.input(pinIn)
    if not pinStatus:
        pi.setup(pinOut, sts)
        return False
    else:
        pi.setup(pinOut, sts)
        return True