class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        min_heap = []
        for i in range(len(times)):
            heappush(min_heap, i)

        arrive_dic = {}
        depart_dic = defaultdict(list)

        max_time = 0

        for idx, (arrive, depart) in enumerate(times):
            arrive_dic[arrive] = idx
            depart_dic[depart].append(idx)
            max_time = max(max_time, depart)

        sits_in = {}
        
        for time in range(max_time + 1):
            if time in depart_dic:
                for person in depart_dic[time]:
                    heappush(min_heap, sits_in[person])
                    del sits_in[person]

            if time in arrive_dic:
                least_chair = heappop(min_heap)
                person = arrive_dic[time]
                if person == targetFriend:
                    return least_chair
                else:
                    sits_in[person] = least_chair

        return -1
         