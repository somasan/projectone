v = int(input())
t = int(input())
if t == 0:
    print(0)
elif v >= 0:
    c = v * t // 109
    print(v * t - c * 109)
elif v < 0 and v * t <= -109 and v * t % -109 != 0:
    a = (-v) * t // 109
    print((v * t + (a + 1) * 109))
elif v < 0 and v * t <= -109 and v * t % -109 == 0:
    print(0)
elif v < 0 and v * t > -109:
    print(109 + v * t)
