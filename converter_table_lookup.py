"""
Provided a set of facts about ratios between units, 
create a program that can then convert between units
when queried
"""

"""
Solution based on building a table that links facts based on common units
"""


class unitConverter:
    def __init__(self):
        self.facts = []

    def isInTable(self, param):
        for index, fact_table in enumerate(self.facts):
            if param in fact_table.keys():
                return True, index
        return False, None

    def mergeTables(self, index1, index2, ratio, linking_param):
        for param in self.facts[index2].keys():
            self.facts[index1][param] = self.facts[index2][param] * ratio * self.facts[index1][linking_param]
        self.facts.pop(index2)

    def load_fact(self, fact: tuple[str, float, str]):
        if not self.facts:
            ftable = {fact[0]: 1, fact[2]: fact[1]}
            self.facts.append(ftable)
            return

        paramA_in_table, paramA_table = self.isInTable(fact[0])
        paramB_in_table, paramB_table = self.isInTable(fact[2])

        if paramA_in_table and paramB_in_table:
            # Join the two tables based on link
            self.mergeTables(paramA_table, paramB_table, fact[1], fact[0])

        elif paramA_in_table:
            # Add paramB into paramA table
            self.facts[paramA_table][fact[2]] = self.facts[paramA_table][fact[0]] * fact[1]
            
        elif paramB_in_table:
            # Add paramA into paramB table
            self.facts[paramB_table][fact[0]] = self.facts[paramB_table][fact[2]] * fact[1]**-1
    
        else:
            # Add new table
            ftable = {fact[0]: 1, fact[2]: fact[1]}
            self.facts.append(ftable)

    def answer_query(self, query: tuple[float, str, str]) -> float:
        for table in self.facts:
            if query[1] in table.keys() and query[2] in table.keys():
                return query[0] * (table[query[2]] / table[query[1]])


        


