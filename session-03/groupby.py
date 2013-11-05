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

import itertools
students.sort(key=lambda f:f.favorite)
    
it = itertools.groupby(students, (lambda x: x.favorite))
for key,group in it:
    data_in_group = list(group)
    print 'Favorite: ', key, '=>', sum([item.grade for item in data_in_group])/len(data_in_group)

aggregation = [(group[0],sum([item.grade for item in group[1]])) for group in itertools.groupby(students, (lambda x: x.favorite))]
print aggregation
