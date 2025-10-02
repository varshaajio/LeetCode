class Solution(object):
	def maxBottlesDrunk(self,numBottles,numExchange):
		"""
		:type numBottles:int
		:type numExchange:int
		:rtype:int
		"""
		tot=numBottles
		em=numBottles
		while (em>=numExchange):
			em-=numExchange
			numExchange+=1 
			tot+=1		
			em+=1		
		return tot

		
