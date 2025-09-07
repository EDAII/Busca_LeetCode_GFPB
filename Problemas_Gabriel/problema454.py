class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # Cria dicionário com somas do primeiro par
        ## OBS: Counter é uma subclasse de dicionário que ajuda a contar objetos hashable da biblioteca collections
        somas_ab = Counter(a + b for a in nums1 for b in nums2)
    
        # Conta quantas vezes -soma aparece no segundo par
        count = 0
        for c in nums3:
            for d in nums4:
                count += somas_ab.get(-(c + d), 0)
    
        return count
 
        