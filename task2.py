def trap(heights):
    stack = []
    water_trapped = 0  

    for i in range(len(heights)):
        while stack and heights[i] > heights[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            distance = i - stack[-1] - 1
            bounded_height = min(heights[i], heights[stack[-1]]) - heights[top]
            water_trapped += distance * bounded_height
        
        stack.append(i)

    return water_trapped  

heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(heights))  # Output: 6