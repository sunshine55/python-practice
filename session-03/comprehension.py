class Student:
    def __init__(self, name, grade, favorite):
        self.name = name
        self.grade = grade
        self.favorite = favorite
        
students = [Student('Tom',10,'PHP'), 
            Student('John',6,'Python'),
            Student('David',6,'C#'),
            Student('Paul',8,'C#'),
            Student('Matt',2,'Java'),
            Student('Peter',9,'PHP'),
    ]

avg = sum([item.grade for item in students])/len(students)
print 'Students: %d    Average: %d' % (avg,len(students))

# Data projection
good_grades = [item.grade for item
	in students if item.grade > avg]

print 'LIST of GOOD GRADES (above average)'	
for grade in good_grades:
    print 'Grade: ',grade

# Filter
csharp_students = [item for item in students if item.favorite == 'C#']
print 'LIST of C# Students'	
for s in csharp_students:
    print 'Student: %s grade: %d', (s.grade,s.grade)

# Create a different data structure
lang_grade = [(item.favorite, item.grade) for item  in students]

for row in lang_grade:
    print '%s\t%d' % row

grade_by_lang = {}
for row in lang_grade:
    if row[0] not in grade_by_lang:
        group = [item[1] for item in lang_grade if item[0]==row[0]]
        grade_by_lang[row[0]] = sum(group)/len(group)
    
print 'Lang\tAvg'    
for item in grade_by_lang.items():
    print '%s\t%d' % item