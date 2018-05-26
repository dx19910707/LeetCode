class MapSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.map.update({key:val})

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        res = 0
        for k,v in self.map.items():
            if k.startswith(prefix):
                res += v
        return res
