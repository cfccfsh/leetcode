class SummaryRanges:

    def __init__(self):
        self.num_set = set()

    def addNum(self, val: int) -> None:
        self.num_set.add(val)

    def getIntervals(self):
        if not self.num_set:
            return []

        res = []
        sorted_list = sorted(list(self.num_set))

        copy_list = sorted_list
        while True:
            piece_list = self.split_list(copy_list)
            if not piece_list:
                return res
            else:
                start, end = piece_list
                res.append([copy_list[start],copy_list[end]])
                copy_list = copy_list[end+1:]

    def split_list(self, target_list):
        if not target_list:
            return []
        start = 0
        end = 0
        for index, item in enumerate(target_list):
            if len(target_list) - 1 >= index + 1:
                if item+1 == target_list[index + 1]:
                    end += 1
                else:
                    return [start, end]
            else:
                return [start, end]