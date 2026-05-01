class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        roots = [i for i in range(n)]
        emailToIdx = {}
        def find(node):
            while roots[node] != roots[roots[node]]:
                roots[node] = roots[roots[node]]
            return roots[node]
        
        for i in range(n):
            account = accounts[i]
            for email in account[1:]:
                if email in emailToIdx:
                    roots[find(i)] = find(emailToIdx[email])
                emailToIdx[email] = find(i)
        
        tmp = defaultdict(list)
        for email, idx in emailToIdx.items():
            rootI = find(idx)
            tmp[rootI].append(email)
        for v in tmp.values():
            v.sort()
        return [[accounts[idx][0]]+emails for idx, emails in tmp.items()]