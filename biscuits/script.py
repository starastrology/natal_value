from astro import get_estimated_value

for y in range(1990, 1993):
    for m in range(1, 13):
        for d in range(1, 32):
            ev=get_estimated_value(str(y),str(m),str(d))
            if ev[2][1] < 0:
                print(y, m , d)
                print(ev[0])
                print(ev[1])
                print("+========+")
