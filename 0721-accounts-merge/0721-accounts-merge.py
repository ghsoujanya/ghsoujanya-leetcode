class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])  # Path compression
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        uf = UnionFind()
        email_to_name = {}

        # 1. Build the Union-Find graph and map emails to owners
        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                if email not in uf.parent:
                    uf.parent[email] = email
                uf.union(first_email, email)
                email_to_name[email] = name

        # 2. Group emails by their root representative
        from collections import defaultdict
        groups = defaultdict(list)
        for email in uf.parent:
            root = uf.find(email)
            groups[root].append(email)

        # 3. Format output: [Name, sorted_emails...]
        result = []
        for root, emails in groups.items():
            result.append([email_to_name[root]] + sorted(emails))

        return result