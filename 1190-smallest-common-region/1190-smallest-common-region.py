class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parent = {}
        
        for region in regions:
            for child in region[1:]:
                parent[child] = region[0]

        def dfs(region, ancestors):
            if region in parent:
                dfs(parent[region], ancestors)
            ancestors.add(region)
        
        ancestors1 = set()
        dfs(region1, ancestors1)

        while region2 not in ancestors1:
            region2 = parent[region2]
        
        return region2