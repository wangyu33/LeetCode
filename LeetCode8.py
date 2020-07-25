class solution(object):
    def myAtoi(self, str):
        flag = 1
        ans = []
        chr_num = 0
        for i in range(len(str)):
            if str[i].isdigit():
                ans.append(str[i])
            elif len(ans) == 0 and str[i] == '-':
                flag = -1
                chr_num += 1
            elif len(ans) == 0 and str[i] == '+':
                chr_num += 1
            elif len(ans) == 0 and chr_num == 0 and str[i] == ' ':
                continue
            else:
                break
            if chr_num >= 2:
                break
        if len(ans) == 0:
            return 0
        ans = int(''.join(ans)) * flag
        if ans > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif ans < -2 ** 31:
            return -2 ** 31
        return ans

def main():
    str = "0-1"
    print(solution().myAtoi(str))

if __name__ == '__main__':
    main()