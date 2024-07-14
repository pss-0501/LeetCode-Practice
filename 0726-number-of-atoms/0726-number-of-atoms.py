class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse_formula(formula):
            stack = [collections.Counter()]
            i, n = 0, len(formula)
            
            while i < n:
                if formula[i] == '(':
                    stack.append(collections.Counter())
                    i += 1
                elif formula[i] == ')':
                    top = stack.pop()
                    i += 1
                    start = i
                    while i < n and formula[i].isdigit():
                        i += 1
                    multiplicity = int(formula[start:i] or 1)
                    for element, count in top.items():
                        stack[-1][element] += count * multiplicity
                else:
                    start = i
                    i += 1
                    while i < n and formula[i].islower():
                        i += 1
                    element = formula[start:i]
                    start = i
                    while i < n and formula[i].isdigit():
                        i += 1
                    count = int(formula[start:i] or 1)
                    stack[-1][element] += count
                    
            return stack.pop()
        
        counts = parse_formula(formula)
        result = []
        for element in sorted(counts):
            result.append(element)
            if counts[element] > 1:
                result.append(str(counts[element]))
        return ''.join(result)