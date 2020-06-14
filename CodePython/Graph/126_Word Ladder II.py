class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        # 先建无权无向图
        # 再双端BFS遍历
        from collections import defaultdict
        def build_graph_effective(wordList):
            graph = defaultdict(list)
            for w in wordList:
                for i in range(len(w)):
                    w_list = list(w)
                    w_list[i] = '*'
                    w_str = ''.join(w_list)
                    graph[w].append(w_str)
                    graph[w_str].append(w)
            return graph

        #方法1：直接DFS, 对较长的单词串会超时
        # def dfs(graph, end, cur_node, cur_path, vistied, paths):
        #     if cur_node==end:
        #         if len(paths):
        #             if len(paths[0])>len(cur_path):  #当前路径比已有路径短时，用当前的覆盖以前的
        #                 paths.clear()
        #                 paths.append(cur_path[:])
        #             elif len(paths[0])==len(cur_path): #当前路径和已有路径等长，追加
        #                 paths.append(cur_path[:])
        #         else:
        #             paths.append(cur_path[:])  #已有路径为空时，直接添加
        #     else:
        #         for v in graph[cur_node]:
        #             if not vistied[v]:
        #                 vistied[v] = True
        #                 if '*' not in v:
        #                     cur_path.append(v)
        #                 dfs(graph, end, v, cur_path, vistied, paths)
        #                 if '*' not in v:
        #                     cur_path.pop()
        #                 vistied[v] = False


        #方法2：先用BFS找到最短路径的长度
        #       再用DFS找所有最短路径，递归式如果当前路径大于最短路径就提前结束
        def bfs_shortest(graph, begin, end):
            queue = [(begin, 1)]
            visited = defaultdict(bool)
            visited[begin] = True
            while queue:
                cur_node, cur_level = queue.pop(0)
                if cur_node==end:
                    return cur_level//2+1
                for v in graph[cur_node]:
                    if not visited[v]:
                        visited[v]=True
                        queue.append((v, cur_level+1))

        def dfs_end(graph, end, cur_node, cur_path, vistied, paths, shortest):
            if len(cur_path)>shortest:
                return
            if cur_node==end:
                if len(paths):
                    if len(paths[0])>len(cur_path):  #当前路径比已有路径短时，用当前的覆盖以前的
                        paths.clear()
                        paths.append(cur_path[:])
                    elif len(paths[0])==len(cur_path): #当前路径和已有路径等长，追加
                        paths.append(cur_path[:])
                else:
                    paths.append(cur_path[:])  #已有路径为空时，直接添加
            else:
                for v in graph[cur_node]:
                    if not vistied[v]:
                        vistied[v] = True
                        if '*' not in v:
                            cur_path.append(v)
                        dfs_end(graph, end, v, cur_path, vistied, paths, shortest)
                        if '*' not in v:
                            cur_path.pop()
                        vistied[v] = False


        #方法3：只使用BFS
        def bfs(graph, begin, end):
            # BFS遍历使用的队列
            queue = [(begin, 1)]
            # 标记节点是否被访问过，使用节点第一次被访问时的层级信息
            visited = defaultdict(int)
            visited[begin] = 1
            # 记录到每个节点的所有最短路劲
            node_path = defaultdict(list)
            node_path[begin].append([begin])
            while queue:
                cur_node, cur_level = queue.pop(0)
                if cur_node==end:
                    break
                for next_node in graph[cur_node]:
                    # 如果当前节点没有遍历过
                    if not visited[next_node]:
                        visited[next_node] = cur_level+1
                        queue.append((next_node, cur_level+1))
                        for path in node_path[cur_node]:
                            if '*' not in next_node:
                                node_path[next_node].append(path+[next_node])
                            else:
                                node_path[next_node].append(path)
                    #如果当前节点在BFS遍历的下一层级，即使其被访问过，当时到当前的路径还可以增加
                    elif visited[next_node]>cur_level:
                        for path in node_path[cur_node]:
                            if '*' not in next_node:
                                node_path[next_node].append(path+[next_node])
                            else:
                                node_path[next_node].append(path)
            return node_path[end]


        def visit_level(graph, queue, direct, pre_level, visited, node_paths, other_visited, other_node_paths, paths):
            meet_flag = False
            while queue and queue[0][1] - pre_level == 1:
                cur_node, cur_level = queue.pop(0)
                for next_node in graph[cur_node]:
                    if other_visited[next_node]:  # 首尾两端的遍历相遇
                        meet_flag = True  # 设置标志，相遇后这一层遍历后就退出
                        # 组合拼接路径
                        for path_cur in node_paths[cur_node]:
                            for path_other in other_node_paths[next_node]:
                                if direct==0:  #当前是正序遍历
                                    paths.append(path_cur + path_other[::-1])
                                else:
                                    paths.append(path_other + path_cur[::-1])
                        continue
                    # 如果当前节点没有遍历过
                    if not visited[next_node]:
                        visited[next_node] = cur_level + 1
                        queue.append((next_node, cur_level + 1))
                        for path in node_paths[cur_node]:
                            if '*' not in next_node:
                                node_paths[next_node].append(path + [next_node])
                            else:
                                node_paths[next_node].append(path)
                    # 如果当前节点在BFS遍历的下一层级，即使其被访问过，当时到当前的路径还可以增加
                    elif visited[next_node] > cur_level:
                        for path in node_paths[cur_node]:
                            if '*' not in next_node:
                                node_paths[next_node].append(path + [next_node])
                            else:
                                node_paths[next_node].append(path)
            return meet_flag

        #方法4：双端BFS
        def bfs_bidirect(graph, begin, end):

            # BFS遍历使用的队列
            queue_begin = [(begin, 1)]
            # 标记节点是否被访问过，使用节点第一次被访问时的层级信息
            visited_begin = defaultdict(int)
            visited_begin[begin] = 1
            # 记录到每个节点的所有最短路劲
            node_path_begin = defaultdict(list)
            node_path_begin[begin].append([begin])

            queue_end = [(end, 1)]
            # 标记节点是否被访问过，使用节点第一次被访问时的层级信息
            visited_end = defaultdict(int)
            visited_end[end] = 1
            # 记录到每个节点的所有最短路劲
            node_path_end = defaultdict(list)
            node_path_end[end].append([end])

            meet_flag = False
            paths = []
            pre_level_begin = 0
            pre_level_end = 0
            while queue_begin and queue_end:
                # 正序
                if meet_flag:
                    break
                # 把同一层的遍历完，不然数据会有缺失
                meet_flag = visit_level(graph, queue_begin, 0, pre_level_begin, visited_begin, node_path_begin,
                                        visited_end, node_path_end, paths)
                pre_level_begin += 1

                # 反序
                if meet_flag:
                    break
                meet_flag = visit_level(graph, queue_end, 1, pre_level_end, visited_end, node_path_end,
                                        visited_begin, node_path_begin, paths)
                pre_level_end += 1
            return paths


        if endWord not in wordList:
            return []
        wordList.append(beginWord)
        wordList = list(set(wordList))
        graph = build_graph_effective(wordList)

        # paths = []
        # visited = defaultdict(bool)
        # visited[beginWord] = True
        #方法1
        # dfs(graph, endWord, beginWord, [beginWord], visited, paths)
        # retrun paths
        #方法2
        # shortest = bfs_shortest(graph, beginWord, endWord)
        # if shortest:
        #     dfs_end(graph, endWord, beginWord, [beginWord], visited, paths, shortest)
        # return paths

        #方法3
        # return bfs(graph, beginWord, endWord)

        #方法4：双端BFS
        return bfs_bidirect(graph, beginWord, endWord)



s = Solution()

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

# beginWord = "red"
# endWord = "tax"
# wordList = ["ted","tex","red","tax","tad","den","rex","pee"]

# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

print(s.findLadders(beginWord, endWord, wordList))