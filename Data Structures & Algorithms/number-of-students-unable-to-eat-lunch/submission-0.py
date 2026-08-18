class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while (len(set(students))!=1 or students[0]==sandwiches[0] ) and len(students)!=0:
            if students[0] == sandwiches[0]:
                students = students[1:]
                sandwiches = sandwiches[1:]
            else:
                a = students[0]
                students = students[1:]
                students.append(a)
        return len(students)
