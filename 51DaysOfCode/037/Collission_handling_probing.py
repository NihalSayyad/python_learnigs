class HashTable:

    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] == None:
            self.arr[h] = (key, val)
        else:
            new_h = self.find_slot(key, val)
            self.arr[new_h] = (key, val)

    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]

    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index] == key:
                return prob_index
        raise Exception("Hashmap Full")

if __name__ == '__main__':
    hmap = HashTable()
    hmap['march 17'] = 240
    hmap['march 6']  = 190

    print(hmap['march 6'])
    print(hmap['march 17'])
    print(hmap.arr)