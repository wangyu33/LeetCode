class solution(object):
    def convert(self, s, numRows):
        if len(s) <= numRows:
            return s
        str = list(s)
        ans = []
        for j in range(numRows):
            temp = j
            while temp < len(s):
                ans.append(str[temp])
                if j == 0 or j == numRows - 1:
                    temp = temp + 2 * numRows - 2
                else:
                    temp = temp + 2 * numRows -(j + 1) * 2
                    if temp >= len(s):
                        break
                    ans.append(str[temp])
                    temp = temp + 2 * j
                #print(ans)
        return  ''.join(ans)


def main():
    s = "PAYPALISHIRING"
    numRows = 4
    print(solution().convert(s,numRows))

if __name__ == "__main__":
    main()


