class solution(object):
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s

        ans = s[0]
        s = list(s)
        for i in range(len(s)):
            for j in range(min(i, len(s) - i - 1) + 1):
                if s[i - j] == s[i + j]:
                    if (j * 2 + 1) > len(ans):
                        ans = s[i - j: i + j + 1]
                else:
                    break
            for j in range(min(i, len(s) - i - 2) + 1):
                if s[i - j] == s[i + j + 1]:
                    if (j * 2 + 2) > len(ans):
                        ans = s[i - j: i + j + 2]
                else:
                    break
        return ''.join(ans)

def main():
    s = "cbbd"
    print(solution().longestPalindrome(s))

if __name__ == "__main__":
    main()
