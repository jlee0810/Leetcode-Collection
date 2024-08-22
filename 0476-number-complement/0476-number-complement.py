class Solution:
    def findComplement(self, num: int) -> int:
        bin_num = "{0:b}".format(num)

        complement_bin = ""
        for c in bin_num:
            if c == '0':
                complement_bin += '1'
            else:
                complement_bin += '0'
        return int(complement_bin, 2)