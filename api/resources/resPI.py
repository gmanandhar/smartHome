from api.models import pi

def resPi(pinIn, pinOut, status):
    pi.setup(pinIn, pi.IN)
    pi.setup(pinOut, pi.OUT)
    # Input from pin 11
    pinStatus = pi.input(pinIn)
    if pinStatus:
        pi.setup(pinOut, status)
        return False
    else:
        pi.setup(pinOut, status)
        return True