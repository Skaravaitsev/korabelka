import cmath
def calculate_XH(frequency, speed_of_sound, distance_between_elements, num_elements):
    phi = []
    XH = []
    for i in range(180):
        loc_phi = i - 90
        loc_XH = 0 + 0j
        for j in range(num_elements):
            delay = j*distance_between_elements/speed_of_sound*cmath.sin(loc_phi/180*cmath.pi)
            phase = 2 * cmath.pi*frequency*delay

            w = (1/2)*(1-cmath.cos(2*cmath.pi*(j/num_elements)))
            loc_XH += w * cmath.exp(1j*phase)
        XH.append(abs(loc_XH))
        phi.append(loc_phi)
    max_XH = max(XH)
    for i in range(180):
        XH[i] /= max_XH
    return phi, XH
