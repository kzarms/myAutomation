class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        #SList = list(map(int, scores.split()))
        AvgScore = sum(self.scores)//len(self.scores)
        if AvgScore < 40:
            return 'T'
        if 40 <= AvgScore < 55:
            return 'D'
        if 55 <= AvgScore < 70:
            return 'P'
        if 70 <= AvgScore < 80:
            return 'A'
        if 80 <= AvgScore < 90:
            return 'E'
        if 90 <= AvgScore <= 100:
            return 'O'


# line = input().split()
# firstName = line[0]
# lastName = line[1]
# idNum = line[2]
# numScores = int(input()) # not needed for Python
# scores = list( map(int, input().split()) )
s = Student('Alice', 'Boris', 1234, [10, 20, 40, 56, 100])
#s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())