class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
    def computeDifference(self):
        self.maximumDifference = max(self.__elements) - min(self.__elements)

	# Add your code here

# End of Difference class

#_ = input()
#a = [int(e) for e in input().split(' ')]
a = [1, 2, 3, 4, 5]
d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
a == null
