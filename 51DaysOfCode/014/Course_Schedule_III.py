import heapq
class Solution:
    def scheduleCourse(self, courses) :
        courses.sort(key=lambda c: c[1])
        que,cur=[],0
        for t,d in courses:
            heapq.heappush(que,-t)
            cur+=t
            if cur>d:
                cur+=heapq.heappop(que)
        return len(que)
            

courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
print(Solution().scheduleCourse(courses))
courses = [[3,2],[4,3]]
print(Solution().scheduleCourse(courses))
courses = [[5,5],[4,6],[2,6]]
print(Solution().scheduleCourse(courses))