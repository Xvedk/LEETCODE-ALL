class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(dict)
        for orig, chang, cost in zip(original, changed, cost):
            graph[orig][chang] = min(cost, graph[orig].get(chang, sys.maxsize))

        sum_min_costs, dict_costs = 0, {}
        for source_letter, target_letter in zip(source, target):
            if source_letter == target_letter:
                continue
            if source_letter in dict_costs:
                if target_letter in dict_costs[source_letter]:
                    sum_min_costs += dict_costs[source_letter][target_letter]
                    continue
                else:
                    return -1
            heap, memo = [(0, source_letter)], {}
            while heap:
                cost_current, letter = heappop(heap)
                if cost_current <= memo.get(letter, sys.maxsize):
                    for neighbor, cost_neighbor in graph[letter].items():
                        cost_new = cost_neighbor + cost_current
                        if cost_new < memo.get(neighbor, sys.maxsize):
                            memo[neighbor] = cost_new
                            heappush(heap, (cost_new, neighbor))
            if target_letter not in memo:
                return -1
            dict_costs[source_letter] = memo
            sum_min_costs += memo[target_letter]
        return sum_min_costs    
