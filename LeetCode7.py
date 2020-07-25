class solution(object):
    def reverse(self, x):
        flag = 1
        if x < 0:
            x  =  x * -1
            flag = -1
        x = list(str(x))
        t = 0
        x = x[::-1]
        x = int(''.join(x))
        if flag == -1:
            x =  x*-1
        if x > 2**31 -1 or x < -1 * 2**31:
            return 0
        return x

def main():
    num = 1534236469
    print(solution().reverse(num))

if __name__ == "__main__":
    main()