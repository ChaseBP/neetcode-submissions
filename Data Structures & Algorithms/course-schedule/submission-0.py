class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # WHAT COURSES DEPEND ON 'I' PREREQ -> COURSES
        ADJ = { I: [] for I in range(numCourses)}
        # COUNT OF DEPENDENT COURSES FOR EACH COURSE
        IN_DEGREE = [0] * numCourses

        for COURSE, PREREQ in prerequisites:
            ADJ[PREREQ].append(COURSE)
            IN_DEGREE[COURSE] += 1 

        QUEUE = deque()
        for COURSE_ID in  range(numCourses):
            if IN_DEGREE[COURSE_ID] == 0:
                QUEUE.append(COURSE_ID)
        
        COMPLETED_COUNT = 0

        while QUEUE:
            CURR_COURSE = QUEUE.popleft()
            COMPLETED_COUNT += 1

            for NEXT_COURSE in ADJ[CURR_COURSE]:
                IN_DEGREE[NEXT_COURSE] -= 1 
            
                if IN_DEGREE[NEXT_COURSE] == 0:
                    QUEUE.append(NEXT_COURSE)
            
        return COMPLETED_COUNT == numCourses

            

