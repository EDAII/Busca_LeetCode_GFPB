class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        # Definindo qual array é menor e colocando em nums1
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = len(nums1), len(nums2)

        low = 0
        high = len(nums1)
        total = m + n
        # Metade = total +1 para funcionar com pares e impares
        half = (total + 1) // 2 

        while low <= high:
        # Corte no array menor
            i = (low + high) // 2  
            j = half - i

        # Valores adjacentes ao corte
            left1  = nums1[i-1] if i > 0 else float('-inf')
            right1 = nums1[i]   if i < m else float('inf')
            left2  = nums2[j-1] if j > 0 else float('-inf')
            right2 = nums2[j]   if j < n else float('inf')

        # A partição está correta ?
            if left1 <= right2 and left2 <= right1:
        # Caso impar
                if total % 2 == 1:
                    return max(left1, left2)
        # Caso par        
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2

        # Move o corte para a esquerda
            elif left1 > right2:
                high = i - 1
        # Move o corte para a direita left2 > right1
            else:            
                low = i + 1

        