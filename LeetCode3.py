class solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 1:
            return 1
        elif len(s) < 1:
            return 0

        ans = 1
        dict = {}
        flag = -1
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = i
                ans = max(ans,i - flag)
            else:
                flag = max(flag, dict[s[i]])
                ans = max(i-flag, ans)
                dict[s[i]] = i
            print(ans,flag)
        return ans

def main():
    s = "au"
    print(solution().lengthOfLongestSubstring(s))

if __name__ == "__main__":
    main()



