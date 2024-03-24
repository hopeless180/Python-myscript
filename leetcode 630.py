courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
def maxCourses(courses):
    # 按照课程的截止日期进行排序
    courses.sort(key=lambda x: x[1])
    
    max_courses = 0  # 最大可以修读的课程数
    current_day = 0  # 当前的日期
    
    for duration, end_day in courses:
        # 如果当前课程可以在截止日期之前完成
        if current_day + duration <= end_day:
            current_day += duration
            max_courses += 1
    
    return max_courses

def maxCourses_GA(courses):
    # 按照截止日期排序
    import heapq
    courses.sort(key=lambda x: x[1])
    
    max_courses = 0  # 最大可以修读的课程数
    current_day = 0  # 当前的日期
    max_heap = []  # 用于保存课程持续时间的最大堆
    
    for duration, end_day in courses:
        # 如果当前课程可以在截止日期之前完成
        if current_day + duration <= end_day:
            heapq.heappush(max_heap, -duration)  # 将持续时间加入最大堆，注意取负数
            
            current_day += duration
            max_courses += 1
        # 如果无法在截止日期之前完成，尝试用当前课程替换掉最长的课程
        elif max_heap:
            longest_duration = -heapq.heappop(max_heap)
            # 如果当前课程持续时间小于最长课程，则用当前课程替代
            if duration < longest_duration:
                current_day += duration - longest_duration
                heapq.heappush(max_heap, -duration)
    
    return max_courses

# 示例用法
courses = [[2, 5], [2, 6], [3, 7], [1, 3]]
result = maxCourses(courses)
print(result)
result = maxCourses_GA(courses)
print(result)

