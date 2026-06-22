class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position , speed = map(list,zip(*(sorted(zip(position,speed),reverse = True))))
        time = [(target - position[i])/speed[i] for i in range(len(position))]
        stack = [time[0]]
        for i in range(1,len(time)):
            if time[i]>stack[-1]:
                stack.append(time[i])
        return len(stack)