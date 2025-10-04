class Solution(object):
	def maxArea(self,height):
		"""
		:type height:List[int]
		:rtype:int
		"""
		l=0
		r=len(height)-1
		m=0
		while l<r:
			temp=min(height[l],height[r])
			w=r-l
			a=w*temp
			if m<a:
				m=a
			if height[l]<height[r]:
				l+=1
			else:
				r-=1
		return m

