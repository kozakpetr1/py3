import math
from turtle import *
i = 45
color('red', 'yellow')
begin_fill()
while True:
    x = int(200 * math.sin(i*math.pi/360))
    forward(x)
    left(170)
    i += 45
    if abs(pos()) < 1:
        break
end_fill()
done()