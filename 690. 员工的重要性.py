# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: [Employee]
        :type id: int
        :rtype: int
        208ms, beats: 70.24%
        """
        imp = 0
        id_imp_map = {}
        id_sub_map = {}
        for employee in employees:
            id_imp_map.update({
                employee.id: employee.importance
            })
            id_sub_map.update({
                employee.id: employee.subordinates
            })
        imp += id_imp_map[id]
        subs = id_sub_map[id]
        while subs:
            next_ids = []
            for sub in subs:
                imp += id_imp_map[sub]
                next_ids.extend(id_sub_map[sub])
            subs = next_ids
        return imp


e = Employee
a = e(1, 5, [2, 3])
b = e(2, 3, [])
c = e(3, 3, [])
i = 1
s = Solution()
r = s.getImportance([a, b, c], 1)
print(r)
