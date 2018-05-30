class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        keys = [0]
        d = {0:True}
        while keys:
            new_keys = []
            for key in keys:
                room = rooms[key]
                for k in room:
                    if k in d:
                        continue
                    d[k] = True
                    new_keys.append(k)
            keys = new_keys
        l = [i for i in d.keys()]
        l.sort()
        all_rooms = list(range(len(rooms)))
        if l == all_rooms:
            return True
        return False
