# Abrar Rouf
# CS 100 2017F Section H01
# HW 19, Dec 10, 2017


class Course_Section:
    def __init__(self, sec_num, crs_name, enrlld_stdnts=[]):
        self.section_number = sec_num
        self.course_name = crs_name
        self.enrolled_students = enrlld_stdnts

    def enroll(self, std_info):
        if self.enrolled_students == []:
            if std_info[1] not in self.enrolled_students:
                self.enrolled_students.append(std_info)
                print('%s (UCID: %s) has successfully enrolled in section %d of %s.' % (std_info[0], std_info[1], self.section_number, self.course_name))
        elif self.enrolled_students != []:
            for entry in self.enrolled_students:
                if std_info[1] not in entry:
                    self.enrolled_students.append(std_info)
                    print('%s (UCID: %s) has successfully enrolled in section %d of %s.' % (std_info[0], std_info[1], self.section_number, self.course_name))
                    break
                elif std_info[1] in entry:
                    print('Student already enrolled!')
                    break

    def drop(self, std_info):
        if self.enrolled_students == []:
            print('No students enrolled to be dropped!')
        elif self.enrolled_students != []:
            for entry in self.enrolled_students:
                if std_info[1] in entry:
                    self.enrolled_students.remove(entry)
                    print('%s (UCID: %s) has successfully been dropped from section %d of %s.' % (std_info[0], std_info[1], self.section_number, self.course_name))
                    break
                elif std_info[1] not in entry:
                    print('%s with UCID %s does not exist in section %d of %s.' % (std_info[1], std_info[0], self.section_number, self.course_name))
    university = 'NJIT'


s1 = Course_Section(1, 'CS 100')
print(s1.section_number)
print(s1.course_name)
print(s1.enrolled_students)
s1.enroll(('John', 'j24'))
s1.enroll(('Jonathan', 'j24'))
s1.drop(('Jonathan', 'j24'))
s1.drop(('Tom', 't32'))
print(s1.university)
