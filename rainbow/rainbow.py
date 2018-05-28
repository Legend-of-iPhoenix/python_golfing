import console as s
import colorsys as h
m="Rainbows in Python!"
l=len(m)
r=range(l)
p=print
for i in r:
 for c in r:
  s.set_color(*h.hsv_to_rgb(((c+i)%l)/l,1,1))
  p(m[c],end='')
 p('')
