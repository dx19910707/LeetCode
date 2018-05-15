class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        l = []
        if len(list1) > len(list2):
            list1,list2 = list2,list1
        for i in range(len(list1)):
            if list1[i] in list2:
                index = list2.index(list1[i])
                if not l:
                    l.append([i+index,list1[i]])
                else:
                    if i + index < l[0][0]:
                        l = [[i+index,list1[i]]]
                    elif i + index == l[0][0]:
                        l.append([i+index,list1[i]])
        return [x[1] for x in l]