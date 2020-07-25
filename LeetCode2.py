class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class solution(object):
    def addTwoNumbers(self, l1, l2):
        sum = 0
        flag = 0
        temp = 1
        while 1:
            sum = sum + (l1.val + l2.val) * temp
            temp = temp * 10
            if l1.next == None:
                flag = 1
                break
            elif l2.next == None:
                flag = 2
                break
            l1 = l1.next
            l2 = l2.next
        if flag == 2:
            while l1.next != None:
                l1 = l1.next
                sum = sum + l1.val * temp
                temp = temp * 10
        if flag == 1:
            while l2.next != None:
                l2 = l2.next
                sum = sum + l2.val * temp
                temp = temp * 10
        l3 = ListNode(sum % 10)
        ans = l3
        sum = sum // 10
        while sum != 0:
            l3.next = ListNode(sum % 10)
            l3 = l3.next
            sum = sum // 10
        return ans

def main():
    l1 = ListNode(9)
    l2 = ListNode(7)
    l3 = solution().addTwoNumbers(l1,l2)
    for i in range(2):
        print(l3.val)
        l3 = l3.next


if __name__ == "__main__":
    main()