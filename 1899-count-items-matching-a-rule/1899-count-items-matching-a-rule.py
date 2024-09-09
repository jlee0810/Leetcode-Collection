class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        type_dic = defaultdict(list)
        color_dic = defaultdict(list)
        name_dic = defaultdict(list)

        for idx, item in enumerate(items):
            t,c,n = item
            type_dic[t].append(idx)
            color_dic[c].append(idx)
            name_dic[n].append(idx)

        if ruleKey == "type":
            return len(type_dic[ruleValue])
        elif ruleKey == "color":
            return len(color_dic[ruleValue])
        else:
            return len(name_dic[ruleValue])