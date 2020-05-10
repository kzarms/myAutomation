if __name__ == '__main__':
    #n = int(input())
    #student_marks = {}
    #for _ in range(n):
    #    name, *line = input().split()
    #    scores = list(map(float, line))
    #    student_marks[name] = scores
    #query_name = input()

student_marks = {'Krishna':[67, 68, 69],'Arjun':[70, 98, 63],'Malika':[52, 56, 60]}
query_name = 'Arjun'

print("%.2f" % float(sum(student_marks[query_name])/len(student_marks[query_name])))


a = 13.946
print(a)
print("%.2f" % a)