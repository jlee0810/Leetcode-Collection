class Solution:
    def reverse(self, l, left, right):
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1

    def reverseEveryWord(self, l):
        lastSpace = 0
        for i in range(len(l)):
            if l[i] == " ":
                self.reverse(l, lastSpace, i - 1)
                lastSpace = i + 1
        self.reverse(l, lastSpace, len(l) - 1)

    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverseEveryWord(s)
        self.reverse(s, 0, len(s) - 1)