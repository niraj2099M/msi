import math
import os
import time

def main():
    A = 0
    B = 0
    i = 0
    j = 0
    k = 0
    z = [0] * 1760
    b = [' '] * 1760
    print("\033[2J") # clear terminal
    while True:
        b = [' '] * 1760
        z = [0] * 1760
        for j in range(0, 628, 11):
            for i in range(0, 628, 2):
                c = math.sin(i / 100)
                d = math.cos(j / 100)
                e = math.sin(A)
                f = math.sin(j / 100)
                g = math.cos(A)
                h = d + 2
                D = 1 / (c * h * e + f * g + 5)
                l = math.cos(i / 100)
                m = math.cos(B)
                n = math.sin(B)
                t = c * h * g - f * e
                x = int(40 + 30 * D * (l * h * m - t * n))
                y = int(12 + 15 * D * (l * h * n + t * m))
                o = x + 80 * y
                N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
                if 0 <= y < 22 and 0 <= x < 80 and D > z[o]:
                    z[o] = D
                    b[o] = list(".,-~:;=!*#$@")[N if N > 0 else 0]
        os.system('clear') # clear terminal
        for k in range(1761):
            print((b[k] if k % 80 else '\n'), end='')
            A += 0.00004
            B += 0.00002
        time.sleep(0.03) # pause for a moment to slow down the loop

if __name__ == '__main__':
    main()
    