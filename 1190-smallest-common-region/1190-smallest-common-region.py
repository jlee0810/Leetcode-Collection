class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parent = {}
        for region in regions:
            for child in region[1:]:
                parent[child] = region[0]

        def path_to_root(region: str) -> Set[str]:
            path = []
            while region in parent:
                path.append(region)
                region = parent[region]
            path.append(region)
            return path
        
        path1 = path_to_root(region1)
        path2 = path_to_root(region2)

        set_path1 = set(path1)
        for region in path2:
            if region in set_path1:
                return region
    
        return -1