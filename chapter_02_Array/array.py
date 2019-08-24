class Array:
    def __init__(self, arr=None, capacity=10):###静态数组，指定容量   capacity设定默认值，与实际拥有的元素数量无关
        if isinstance(arr, list):
            self._data = arr[:] ###数组 data                 ###私有属性，表示为 _data
            self._size = len(arr)  ###  
            return              ###初始化 size 和data
        self._data = [None] * capacity 
        self._size = 0 ###  data数组中的元素数量 由 size表示，初始化为0
 ### 私有属性，防止用户从外部获取 数据信息，避免 data和size之间的不一致（因为 用户会修改）
    def get_size(self):  ###获取数组中的 元素个数
        return self._size

    def get_capacity(self): ###  获取数组的 容量
        return len(self._data)

    def is_empty(self): ### 用来 检查数组是否为 0
        return self._size == 0

    def add_last(self, e):  
        self.add(self._size, e) ### 调用add 函数，此时index 为 size

    def add_first(self, e):
        self.add(0, e) ## 调用add函数，此时index 为0

    def add(self, index, e): ###向指定位置 index 添加元素e
        """从后往前"""
        if not 0 <= index <= self._size:  ###index小于 0 , 大于size，则抛出异常
            raise ValueError(
                'add failed. Require index >= 0 and index <= array sise.')
        if self._size == len(self._data): #### 判断 数组 是否 有足够空间
            if self._size == 0:
                self._resize(1)
            else: ### 占满，容量扩充为原来的2 倍
                self._resize(2 * len(self._data))
        for i in range(self._size - 1, index - 1, -1): ##i 大于 index , 小于 size
            self._data[i + 1] = self._data[i] ###将i 位置的元素 往后挪一位
        self._data[index] = e  ###此时，将e添加到 index处
        self._size += 1 ###维护数组的容量

    def get(self, index): 查询位置为index的元素
        if not 0 <= index < self._size: ### 检测 index 是否在合法范围内
            raise ValueError('get failed. Index is illegal.')
        return self._data[index] ##返回 索引为 index的元素

    def get_last(self):
        return self.get(self._size - 1)

    def get_first(self):
        return self.get(0)

    def set(self, index, e):  ###把 index位置的元素修改为e 
        if not 0 <= index < self._size: ### 检测是否 位于合法范围内
            raise ValueError('set failed. Index is illegal.')
        self._data[index] = e ###

    def contains(self, e):
        for i in range(self._size):
            if self._data[i] == e:
                return True
        return False

    def find_index(self, e):
        for i in range(self._size):
            if self._data[i] == e:
                return i
        return -1

    def remove(self, index):
        if not 0 <= index < self._size:
            raise ValueError('remove failed. Index is illegal.')
        ret = self._data[index]
        for i in range(index + 1, self._size):
            self._data[i - 1] = self._data[i]
        self._size -= 1
        # len(self._data)如果为1，len(self._data) // 2就会为0，不合理。
        if (self._size == len(self._data) // 4 and len(self._data) // 2 != 0):
            self._resize(len(self._data) // 2)
        return ret

    def remove_first(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self._size - 1)

    def remove_element(self, e):
        index = self.find_index(e)
        if index != -1:
            self.remove(index)

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data

    def swap(self, i, j):
        if i < 0 or i >= self._size or j < 0 or j >= self._size:
            raise ValueError('Index is illegal.')
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def __str__(self):
        return str('<chapter_02_Array.array.Array> : {}, capacity: {}'.format(self._data[:self._size], self.get_capacity()))

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    arr = Array()

    for i in range(10):
        arr.add_last(i)
    print(arr.get_capacity())
    # arr.add_last('zhe')
    # arr.add_last('wang')
    # arr.add_last('zwang')

    arr.add(1, 'zwang')
    print(arr.get_capacity())

    arr.remove_element('zwang')
    print(arr)

    arr.add_first(-1)
    print(arr)

    arr.remove_element(8)
    print(arr)

    arr.remove_element('zhe')
    print(arr)
