import collections

class Solution:
    def accountsMerge(self, accounts):

        # 并查集
        def init(nums):
            return list(range(nums))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y

        email_to_name = {}
        email_to_id = {}
        idx = 0
        parent = init(1001)
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name
                if email not in email_to_id:
                    email_to_id[email] = idx
                    idx += 1
                union(email_to_id[account[1]], email_to_id[email])
        ans = collections.defaultdict(list)
        for email in email_to_id:
            ans[find(email_to_id[email])].append(email)
        return [[email_to_name[v[0]]] + sorted(v) for v in ans.values()]


        # #DFS
        # graph = collections.defaultdict(set)
        # email_to_name = {}  # 存储每个email对应的账户名
        # for account in accounts:
        #     name = account[0]  # 将每个账号的第1个email和其他email建立连接
        #     for e in account[1:]:
        #         graph[account[1]].add(e)
        #         graph[e].add(account[1])
        #         email_to_name[e] = name
        # ans = []
        # visited = set()
        # for email in graph.keys():
        #     if email not in visited:  # 当前email是所在图是一个岛
        #         stack = [email]  # 对每个岛进行深度优先遍历
        #         visited.add(email)
        #         cur_ans = []
        #         while len(stack):
        #             node = stack.pop()
        #             cur_ans.append(node)
        #             for v in graph[node]:
        #                 if v not in visited:
        #                     visited.add(v)
        #                     stack.append(v)
        #         ans.append([email_to_name[email]] + sorted(cur_ans))
        # return ans


# accounts = [["Alex", "Alex5@m.co", "Alex4@m.co", "Alex0@m.co"], ["Ethan", "Ethan3@m.co", "Ethan3@m.co", "Ethan0@m.co"],
#             ["Kevin", "Kevin4@m.co", "Kevin2@m.co", "Kevin2@m.co"], ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe2@m.co"],
#             ["Gabe", "Gabe3@m.co", "Gabe4@m.co", "Gabe2@m.co"]]
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
solution = Solution()
print(solution.accountsMerge(accounts))