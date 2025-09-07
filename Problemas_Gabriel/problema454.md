# [4. 4Sum II](https://leetcode.com/problems/4sum-ii/description/)

**Dificuldade:** Médio  
**Tópicos:** Array, Hash Table  

**Descrição:**

Dados quatro arrays de inteiros `nums1`, `nums2`, `nums3` e `nums4`, todos de tamanho `n`, retorne o **número de tuplas** `(i, j, k, l)` tais que:

- `0 <= i, j, k, l < n`  
- `nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0`  

---

## Exemplos:

### Exemplo 1:

**Entrada:** `nums1 = [1,2]`, `nums2 = [-2,-1]`, `nums3 = [-1,-2]`, `nums4 = [0,2]`

**Saída:** `2`  

**Explicação:** As duas tuplas são:  
1. `(0, 0, 0, 1)` → `nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0`  
2. `(1, 1, 0, 0)` → `nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0`  

---

### Exemplo 2:

**Entrada:** `nums1 = [0]`, `nums2 = [0]`, `nums3 = [0]`, `nums4 = [0]`

**Saída:** `1`  

---

## Restrições:

- `n == nums1.length`  
- `n == nums2.length`  
- `n == nums3.length`  
- `n == nums4.length`  
- `1 <= n <= 200`  
- `-2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28`  
