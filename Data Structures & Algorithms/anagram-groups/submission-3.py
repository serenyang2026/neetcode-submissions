from collections import Counter
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(list)
        for w in strs:
            key = "".join(sorted(w))
            counts[key].append(w)
        return list(counts.values())
        

