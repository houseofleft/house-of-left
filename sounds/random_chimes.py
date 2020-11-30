from pyo import *

s = Server(nchnls=2).boot()

rand = Randi(min=5,max=15,freq=0.25)


# low
mid_l = Choice(choice=[48, 52, 55, 57], freq=rand)
fr_l = MToF(mid_l)

# mids
mid_m1 = Choice(choice=[60, 64, 67, 69], freq=rand)
mid_m2 = Choice(choice=[60, 64, 67, 69], freq=rand)
fr_m1 = MToF(mid_m1)
fr_m2 = MToF(mid_m2)

# highs
mid_h = Choice(choice=[81, 84, 88], freq=rand)
fr_h = MToF(mid_h)

l = SineLoop(freq = fr_l, mul = 0.1)
rev = Freeverb(l.mix(2), size=0.80, damp=0.10, bal=0.30).out()
m1 = SineLoop(freq = fr_m1, mul = 0.1).out(chnl=0)
m2 = SineLoop(freq = fr_m2, mul = 0.1).out(chnl=1)
h = SineLoop(freq = fr_h, mul = 0.1)
rev = Freeverb(h.mix(2), size=0.95, damp=0.5, bal=0.1).out()

s.gui(locals())
