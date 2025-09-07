# [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/description/?envType=problem-list-v2&envId=binary-search)

**Dificuldade:** Difícil  
**Tópicos:** Array, Binary Search, Divide and Conquer  
**Descrição:**

Dado dois arrays **ordenados** chamados `nums1` e `nums2`, de tamanhos `m` e `n` respectivamente, retorne a **mediana** dos dois arrays combinados.

Você deve implementar um algoritmo com **complexidade de tempo O(log(m+n))**.

---

## Exemplos:

### Exemplo 1:

**Entrada:** `nums1 = [1,3]`, `nums2 = [2]`  

**Saída:** `2.00000`  

**Explicação:** O array mesclado é `[1,2,3]` e a mediana é `2`.

---

### Exemplo 2:

**Entrada:** `nums1 = [1,2]`, `nums2 = [3,4]`  

**Saída:** `2.50000`  

**Explicação:** O array mesclado é `[1,2,3,4]` e a mediana é `(2 + 3) / 2 = 2.5`.

---

## Restrições:

- `nums1.length == m`  
- `nums2.length == n`  
- `0 <= m <= 1000`  
- `0 <= n <= 1000`  
- `1 <= m + n <= 2000`  
- `-10^6 <= nums1[i], nums2[i] <= 10^6`  
