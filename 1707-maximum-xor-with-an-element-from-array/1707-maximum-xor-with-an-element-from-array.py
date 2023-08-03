from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def build_trie(self, num):
        curr = self.root
        for i in range(31, -1, -1):
            value = (num >> i) & 1
            if value not in curr.children:
                curr.children[value] = TrieNode()
            curr = curr.children[value]

    def search(self, num):
        curr = self.root
        res = 0
        for i in range(31, -1, -1):
            value = 1 - ((num >> i) & 1)
            if value in curr.children:
                curr = curr.children[value]
                res |= 1 << i
            else:
                curr = curr.children[1 - value]
        return res

    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = [ -1 for i in range(len(queries))]
        nums.sort()
        for i in range(len(queries)):
            queries[i].append(i)
        queries.sort(key=lambda x: x[1])
        
        num_index = 0
        print(queries)
        for i in range(len(queries)):
            while num_index < len(nums) and nums[num_index] <= queries[i][1]:
                self.build_trie(nums[num_index])
                num_index += 1
            if num_index:
                res[queries[i][2]] = self.search(queries[i][0])
                
        return res
