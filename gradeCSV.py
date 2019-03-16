list = []

##########################################################

def open_file(filename):
    import csv
    file = open(filename, "rt", encoding="utf8")
    fileCSV = csv.reader(file)
    for data in fileCSV:
        if data[0] != '' and data[1] != '':
            list.append(data)

def grade_number(Grade):
    grade = {'A' : 4,
             'B+' : 3.5, 'B' : 3,
             'C+' : 2.5, 'C' : 2,
             'D+' : 1.5, 'D' : 1}
    return grade[Grade]

def sub_year(Year):
    if type(Year) == str and len(Year) == 6:
        return int(Year[0:4]+Year[-1])
    else:
        return ValueError

##########################################################

def insert(value):
    index = 1
    if int(value[3]) == 1 or int(value[3]) == 3:
        for i in list[1:]:
            if sub_year(i[0]) > sub_year(value[0]):
                 list.insert(index, insert_list(value))
                 return 0
            index += 1
        list.insert(index, insert_list(value))
        return 0
    else:
        return ValueError

def insert_list(value):
    print(value)
    empty = []
    for i in range(0,6):
        empty.append(value[i])
    empty.append(grade_number(value[5]))
    for i in range(0,10):
        empty.append('')
    return empty

def delete(value):
    print('delete')
    for i in list:
        if value[0] == i[0] and value[1] == i[1]:
            list.remove(i)
            return 0
    return ValueError

def edit(value):
    print('edit')
    for i in range(len(list)):
        print(value[0])
        print(list[i][0])
        if value[0] == list[i][0] and value[0] == list[i][0]:
            print("a")
            print(list[i])
            list[i] = insert_list(value[2:][0])
            return 0
    return ValueError

def save_list(value):
    empty = []
    print(value)
    empty.append(value[0])
    for i in range(0, 6):
        empty.append('')
    for i in value[1:4]:
        empty.append(i)
    empty.append(str(value[3]/value[1])[:4])
    empty.append(str(value[4]/value[2])[:4])
    for i in range(0, 3):
        empty.append('')
    return empty

def save(value):
    file = open('{}.csv'.format(value[0][0]), 'w', encoding="utf-8")
    file.write(','.join(list[0]))
    file.write('\n')
    year = list[1][0]
    for i in list[1:]:
        print(i)
        if i[0] != year:
            for j in value[0][1]:
                if j[0] == year:
                    file.write(','.join(map(str, save_list(j))))
                    file.write('\n')
        file.write(','.join(map(str, i)))
        file.write('\n')
        year = i[0]
    file.write(','.join(map(str, save_list(value[0][1][-1]))))
    file.close()

def show_grade(grade):
    for i in grade:
        print("{}, weight {}, total weight {},"
              " score {}, total score {}, grade {}, total grade {}"
              .format(i[0], i[1], i[2], i[3], i[4],
                      str(i[3]/i[1])[:4], str(i[4]/i[2])[:4]))


##########################################################

def function(func, value):
    return func(value)

def input_value(number):
    value = { '1' : insert,
              '2' : edit,
              '3' : delete,
              '4' : save,
              '5' : show_grade}
    return value[number]

def value(number):
    if number == '1':
        return insert_value()
    elif number == '2':
        return edit_value()
    elif number == '3':
        return delete_value()
    elif number == '4':
        return save_value(), calculate_value()
    else:
        return calculate_value()

def insert_value():
    year = input("Example : 2559/1 \n"
                 "Enter Year : ")
    code = input("Example : 10123115 \n"
                 "Enter Code : ")
    name = input("Example : Computer \n"
                 "Enter Name : ")
    weight = input("Example : 3 \n"
                   "Enter weight : ")
    section = input("Example : 8 \n"
                    "Enter section : ")
    grade = input("Example : A \n"
                  "Enter grade : ")
    return year, code, name, weight, section, grade

def edit_value():
    yearOld = input("Example : 2558/2 \n"
                    "Enter Year old: ")
    codeOld = input("Example : 10123456 \n"
                    "Enter Code old: ")
    return  yearOld, codeOld, insert_value()

def delete_value():
    year = input("Example : 2559/1 \n"
                 "Enter Year : ")
    code = input("Example : 10123115 \n"
                 "Enter Code : ")
    return year, code

def save_value():
    name = input("Example : File_name \n"
                 "Enter name : ")
    return name, calculate_value()

def calculate_value():
    year = list[1:][0][0]
    grade = []
    weight, score, totalweight, totalscore = 0, 0, 0, 0
    for i in list[1:]:
        if i[6] == '-':
            continue
        elif i[0] == year:
            weight += int(i[3])
            score += int(i[3])*float(i[6])
        else:
            totalweight += weight
            totalscore += score
            grade.append((year, weight, totalweight, score, totalscore))
            year = i[0]
            weight = int(i[3])
            score = int(i[3])*float(i[6])
    totalweight += weight
    totalscore += score
    grade.append((year, weight, totalweight, score, totalscore))
    return (grade)

##########################################################
while True:
    try:
        filename = input("Example data.csv \n"
                         "Enter file name : ")
        open_file(filename)
        while True:
           try:
                number = input("Enter number 1 : insert \n"
                           "Enter number 2 : edit \n"
                           "Enter number 3 : delete \n"
                           "Enter number 4 : save \n"
                           "Enter number 5 : show \n"
                           "Enter number: ")
                if int(number) > 0 and int(number) < 6:
                    function(input_value(number), value(number))
           except:
               print("Invalid Value")
               pass
           for i in list:
               print(i)
    except:
        print("Invalid Value")
        pass
