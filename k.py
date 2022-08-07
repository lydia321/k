class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        newList = [[(i[0] ** 2) + (i[1] ** 2), i] for i in points]
        newList.sort()
        
        return [i[1] for i in newList][:k]
    