import heapq

class TaskManager(object):

    def __init__(self, tasks):
        """
        :type tasks: List[List[int]]
        """
        self.task_info = {}  # taskId -> (userId, priority)
        self.heap = []       # max-heap: (-priority, -taskId, taskId)
        
        for userId, taskId, priority in tasks:
            self.task_info[taskId] = (userId, priority)
            heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def add(self, userId, taskId, priority):
        self.task_info[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId, newPriority):
        userId, _ = self.task_info[taskId]
        self.task_info[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId):
        if taskId in self.task_info:
            del self.task_info[taskId]  # Lazy deletion

    def execTop(self):
        while self.heap:
            priority, neg_taskId, taskId = heapq.heappop(self.heap)
            if taskId in self.task_info:
                userId, cur_priority = self.task_info[taskId]
                if -priority == cur_priority:  # Valid entry
                    del self.task_info[taskId]
                    return userId
        return -1

