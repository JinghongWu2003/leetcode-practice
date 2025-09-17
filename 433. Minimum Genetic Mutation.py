class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        genes = ['A', 'C', 'G', 'T']
        q = deque([(startGene, 0)])
        visited = {startGene}

        while q:
            gene, step = q.popleft()
            if gene == endGene:
                return step
            for i in range(len(gene)):
                for g in genes:
                    if g != gene[i]:
                        mutated = gene[:i] + g + gene[i + 1:]
                        if mutated in bank_set and mutated not in visited:
                            visited.add(mutated)
                            q.append((mutated, step + 1))
        return -1