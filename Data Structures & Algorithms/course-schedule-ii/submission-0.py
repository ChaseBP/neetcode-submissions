class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        inDegree = [0] * numCourses

        queue = deque()

        ordering = []

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            inDegree[course] += 1
    
        for courseId in range(numCourses):
            if inDegree[courseId] == 0:
                queue.append(courseId)
        
        compCourses = 0
        
        while queue:
            currCourse = queue.popleft()
            compCourses += 1
            ordering.append(currCourse)

            for nextCourse in adj[currCourse]:
                inDegree[nextCourse] -= 1
                if inDegree[nextCourse] == 0:
                    queue.append(nextCourse)
        
        if compCourses == numCourses and len(ordering) == numCourses:
            return ordering
        else:
            return []
                
            
            