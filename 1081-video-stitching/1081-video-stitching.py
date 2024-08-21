class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips = deque(sorted(clips, key = lambda x: (x[0],-x[1])))

        if clips[0][0] != 0:
            return -1

        t, cSet, ans = 0, set(), 0

        while clips:
            while clips and clips[0][1] <= t: 
                clips.popleft()
            while clips and clips[0][0] <= t: 
                cSet.add(clips.popleft()[1])
            if clips and not cSet:
                return -1
            if not cSet and t < time:
                return -1
            t = max(cSet)
            ans+= 1
            if t >= time: 
                return ans 
            cSet = set()

        return -1