class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        sandwiches = deque(sandwiches)
        cnt = 0
        
        while True:
            if queue[0] == sandwiches[0]:
                queue.popleft()
                sandwiches.popleft()
                cnt = 0
            
            else:
                lastinline = queue[0]
                queue.popleft()
                queue.append(lastinline)
                cnt += 1
            
            if len(queue) == 0 or len(sandwiches) == 0:
                break

            if cnt >= len(queue):
                break
        
        return len(queue)
