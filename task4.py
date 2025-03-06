class SpecialStack:
    def __init__(self):
        self.main_stack = []  # Stack to store elements
        self.min_stack = []   # Stack to store minimum values
        self.max_stack = []   # Stack to store maximum values

    def push(self, x):
        self.main_stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self):
        if not self.main_stack:
            return None  
        popped_value = self.main_stack.pop()
        if popped_value == self.min_stack[-1]:
            self.min_stack.pop()
        if popped_value == self.max_stack[-1]:
            self.max_stack.pop()
        
        return popped_value

    def get_min(self):
        if not self.min_stack:
            return None  
        return self.min_stack[-1]  
    def get_max(self):
        if not self.max_stack:
            return None  
        return self.max_stack[-1]
s = SpecialStack()
s.push(5)
s.push(1)
s.push(3)
print(s.get_min())  # Output: 1
print(s.get_max())  # Output: 5
s.pop()
print(s.get_min())  # Output: 1
print(s.get_max())  # Output: 5
s.pop()
print(s.get_min())  # Output: 5
print(s.get_max())  # Output: 5