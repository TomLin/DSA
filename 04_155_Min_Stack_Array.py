class MinStack:
    '''
    一個非常好的圖解網頁：
    https://alrightchiu.github.io/SecondRound/stack-neng-gou-zai-o1qu-de-zui-xiao-zhi-de-minstack.html
    '''
    def __init__(self):

        self.stack = [None] * 10
        # 創造一個min_stack來追縱最小值
        self.min_stack = [None] * 10
        self.i_top = None

    def push(self, val: int) -> None:

        # Corner case: 當第一個值時
        if self.i_top is None:
            self.i_top = 0
            self.stack[self.i_top] = val
            self.min_stack[self.i_top] = val

        # 當最後一個值時
        elif self.i_top + 1 == len(self.stack):
            # stack的空間不夠了，expand space
            new_stack = [None] * (2 * len(self.stack))
            new_min_stack = [None] * (2 * len(self.stack))
            for i, (y,z) in enumerate(zip(self.stack, self.min_stack)):
                new_stack[i] = y
                new_min_stack[i] = z

            self.stack = new_stack
            self.min_stack = new_min_stack

            # 把新的值push進去
            self.i_top += 1
            self.stack[self.i_top] = val

            # 取代新的min_val
            if val < self.min_stack[self.i_top-1]:
                self.min_stack[self.i_top] = val
            else:
                self.min_stack[self.i_top] = self.min_stack[self.i_top-1]
        else:
            self.i_top += 1
            self.stack[self.i_top] = val

            # 取代新的min_val
            if val < self.min_stack[self.i_top-1]:
                self.min_stack[self.i_top] = val
            else:
                self.min_stack[self.i_top] = self.min_stack[self.i_top-1]

    def pop(self) -> None:

        # Corner case: 當都沒有值時
        if self.i_top is None:
            return None

        # Corner case: 當僅剩一個值時
        elif self.i_top == 0:
            val = self.stack[self.i_top]
            self.stack[self.i_top] = None
            self.min_stack[self.i_top] = None
            self.i_top = None
            return val
        else:
            val = self.stack[self.i_top]
            self.stack[self.i_top] = None
            self.min_stack[self.i_top] = None
            self.i_top -= 1
            return val

    def top(self) -> int:

        # Corner case: 當都沒有值時
        if self.i_top is None:
            return None

        else:
            val = self.stack[self.i_top]
            return val

    def getMin(self) -> int:

        # Corner case: 當都沒有值時
        if self.i_top is None:
            return None

        else:
            min_val = self.min_stack[self.i_top]
            return min_val
