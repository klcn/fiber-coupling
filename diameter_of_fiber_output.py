from math import pi

f = 6.24e-3 # focal length of lens in front of fiber
w = 3e-6 # fiber mode field diameter

# return output laser beam diameter in unit mm.
def dia(l):
    return (4*l*f)/(pi*w) *1e3

# print the output laser beam diameter, if the laser's wavelength is 450nm
print(dia(450e-9))
