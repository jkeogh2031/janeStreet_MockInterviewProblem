"""
Provided a set of facts about ratios between units, 
create a program that can then convert between units
when queried
"""

"""
Solution based on searching a graph
"""

from collections import deque


class unitConverter(object):
    def __init__(self):
        self.facts = {}

    def load_fact(self, fact: tuple[str, float, str]) -> None:
        self.facts[(fact[0], fact[2])] = fact[1]

    def answer_query(self, query: tuple[float, str, str]) -> float:
        conversion_ratio = self.find_ratio(query[1], query[2])
        return conversion_ratio * query[0] if conversion_ratio else None

    def find_ratio(self, val1: str, val2: str) -> float:
        visited = []
        initial = (visited, val1, 1)
        stack = deque([initial])
        
        while stack:
            curr_visited, curr_unit, curr_ratio = stack.popleft()
            
            for valA, valB in self.facts.keys():
                if (valA, valB) in curr_visited:
                    continue

                elif curr_unit == valA:
                    new_ratio = curr_ratio * self.facts[(valA, valB)]
                    new_visited = curr_visited + [(valA, valB)]

                    if val2 == valB:
                        return new_ratio
                    else:
                        stack.append((new_visited, valB, new_ratio))

                elif curr_unit == valB:
                    new_ratio = curr_ratio * (self.facts[(valA, valB)]**-1)
                    new_visited = curr_visited + [(valA, valB)]
                    
                    if val2 == valA:
                        return new_ratio
                    else:
                        stack.append((new_visited, valA, new_ratio))

