class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        if not graph:
            return [[]]
        current = [[0]]
        index = 0
        next = []
        res = []
        while index < len(graph):
            for i in current:
                if not graph[i[index]]:
                    res.append(i)
                else:
                    for j in graph[i[index]]:
                        next.append(i + [j])
            index += 1
            current, next = next, []
        return res
