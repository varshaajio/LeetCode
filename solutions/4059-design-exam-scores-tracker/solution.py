import bisect
class ExamTracker(object):

    def __init__(self):
        self.t=list()
        self.p=list()

    def record(self, time, score):
        """
        :type time: int
        :type score: int
        :rtype: None
        """
        self.t.append(time)
        if not self.p:
			self.p.append(score)
        else:
			self.p.append(self.p[-1]+score)

    def totalScore(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: int
        """
        leftsplit=bisect.bisect_left(self.t,startTime)
        rightsplit=bisect.bisect_right(self.t,endTime)-1
		
        if len(self.t)<=leftsplit or 0>rightsplit or leftsplit>rightsplit:
            return 0
        t=self.p[rightsplit]
        if leftsplit>0:
            t-=self.p[leftsplit-1]
        return t


# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)
