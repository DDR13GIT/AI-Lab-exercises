# Finding brother & sister of a child
bro_sis_List = [('parent', 'dipok', 'deb', 'male'), ('parent', 'dipok', 'debanjona', 'female'),
                ('parent', 'samir', 'sruti', 'female'), ('parent', 'dipok', 'jeet', 'male')]


def findBrother():
    personName = str(input("Person name:"))
    print('Brother:', end=' ')
    i = 0
    while (i <= 3):
        if ((bro_sis_List[i][0] == 'parent') & (bro_sis_List[i][2] == personName)):
            for j in range(4):
                if ((bro_sis_List[j][0] == 'parent') & (bro_sis_List[i][1] == bro_sis_List[j][1]) & (bro_sis_List[j][3] == 'male') & (bro_sis_List[j][2] != personName)):
                    print(bro_sis_List[j][2], end='\n')
        i = i+1


def findSister():
    personName = str(input("Person name:"))
    print('Sister:', end=' ')
    i = 0
    while (i <= 3):
        if ((bro_sis_List[i][0] == 'parent') & (bro_sis_List[i][2] == personName)):
            for j in range(4):
                if ((bro_sis_List[j][0] == 'parent') & (bro_sis_List[i][1] == bro_sis_List[j][1]) & (bro_sis_List[j][3] == 'female') & (bro_sis_List[j][2] != personName)):
                    print(bro_sis_List[j][2], end='\n')
        i = i+1


findBrother()
findSister()

# Finding Uncle & Aunt of a person
unc_aunt_List = [('parent', 'dipok', 'deb'), ('brother', 'dipok', 'samir'),
                 ('sister', 'dipok', 'uma'), ('brother', 'dipok', 'krisno'),
                 ('brother', 'dipok', 'suvro')]


def findUncle():
    personName = str(input("Person name:"))
    print('Uncle:', end=' ')
    i = 0
    while (i <= 2):
        if ((unc_aunt_List[i][0] == 'parent') & (unc_aunt_List[i][2] == personName)):
            for j in range(5):
                if ((unc_aunt_List[j][0] == 'brother') & (unc_aunt_List[i][1] == unc_aunt_List[j][1])):
                    print(unc_aunt_List[j][2], end='\n')
        i = i+1


def findAunt():
    personName = str(input("Person name:"))
    print('Aunt:', end=' ')
    i = 0
    while (i <= 2):
        if ((unc_aunt_List[i][0] == 'parent') & (unc_aunt_List[i][2] == personName)):
            for j in range(5):
                if ((unc_aunt_List[j][0] == 'sister') & (unc_aunt_List[i][1] == unc_aunt_List[j][1])):
                    print(unc_aunt_List[j][2], end='\n')
        i = i+1


findUncle()
findAunt()
