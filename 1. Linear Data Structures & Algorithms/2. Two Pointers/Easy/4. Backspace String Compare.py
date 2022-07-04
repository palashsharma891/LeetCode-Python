class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x
            yield ''
        
        return all(x == y for x, y in zip(F(s), F(t)))
