"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    ### Original answer
    # houses = set()

    # with open(filename, 'r') as cohort_data:

    #     for line in cohort_data:
    #         house = line.rstrip().split('|')[2]
    #         if house:
    #             houses.add(house)

    #     return houses


    ### Pythonic Code
    with open(filename, 'r') as cohort_data:

        houses_set = {line.rstrip().split('|')[2] for line in cohort_data if line.split('|')[2] != ''}
        return houses_set


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    ### Original answer
    # students = []

    # with open(filename, 'r') as cohort_data:

    #     for line in cohort_data:
    #         first_name, last_name, _, _, cohort_name = line.rstrip().split('|')

    #         if cohort_name not in ('I', 'G') and cohort in (cohort_name, 'All'):
    #             students.append(f'{first_name} {last_name}')     

    #     return sorted(students)


    ### Pythonic code
    with open(filename, 'r') as cohort_data:

        students = [f"{line.rstrip().split('|')[0]} {line.rstrip().split('|')[1]}" for line in cohort_data if line.rstrip().split('|')[2] and cohort in ('All', line.rstrip().split('|')[4])]

        return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    ### Original answer
    # dumbledores_army = []
    # gryffindor = []
    # hufflepuff = []
    # ravenclaw = []
    # slytherin = []
    # ghosts = []
    # instructors = []

    # roster_names = ['dumbledore\'s army', 'gryffindor', 'hufflepuff', 'ravenclaw', 'slytherin', 'ghosts', 'instructors']
    # rosters = [dumbledores_army, gryffindor, hufflepuff, ravenclaw, slytherin, ghosts, instructors]

    # with open(filename, 'r') as cohort_data:

    #     for line in cohort_data:
    #         first_name, last_name, house, _, cohort_name = line.rstrip().split('|')
    #         full_name = f'{first_name} {last_name}'

    #         if house.lower() in roster_names:
    #             idx = roster_names.index(house.lower())
    #             rosters[idx].append(full_name)
    #         elif cohort_name == 'I':
    #             rosters[6].append(full_name)
    #         elif cohort_name == 'G':
    #             rosters[5].append(full_name)      
        
    #     for list in rosters:
    #         list.sort()

    #     return rosters


    ### Pythonic code
    with open(filename, 'r') as cohort_data:

        dumbledores_army = sorted([f"{line.rstrip().split('|')[0]} {line.rstrip().split('|')[1]}" for line in cohort_data if line.rstrip().split('|')[2] == 'Dumbledore\'s Army'])

        cohort_data.seek(0)
        gryffindor = sorted([f"{line.rstrip().split('|')[0]} {line.rstrip().split('|')[1]}" for line in cohort_data if line.rstrip().split('|')[2] == 'Gryffindor'])

        cohort_data.seek(0)
        hufflepuff = sorted([f"{line.rstrip().split('|')[0]} {line.rstrip().split('|')[1]}" for line in cohort_data if line.rstrip().split('|')[2] == 'Hufflepuff'])
        
        cohort_data.seek(0)
        ravenclaw = sorted([f"{line.rstrip().split('|')[0]} {line.rstrip().split('|')[1]}" for line in cohort_data if line.rstrip().split('|')[2] == 'Ravenclaw'])
        
        cohort_data.seek(0)
        slytherin = sorted([f"{line.rstrip().split('|')[0]} {line.rstrip().split('|')[1]}" for line in cohort_data if line.rstrip().split('|')[2] == 'Slytherin'])
        
        cohort_data.seek(0)
        ghosts = sorted([f"{line.rstrip().split('|')[0]} {line.rstrip().split('|')[1]}" for line in cohort_data if line.rstrip().split('|')[4] == 'G'])
        
        cohort_data.seek(0)
        instructors = sorted([f"{line.rstrip().split('|')[0]} {line.rstrip().split('|')[1]}" for line in cohort_data if line.rstrip().split('|')[4] == 'I'])

        return [dumbledores_army, gryffindor, hufflepuff, ravenclaw, slytherin, ghosts, instructors]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    ### Original answer
    # all_data = []

    # with open(filename, 'r') as cohort_data:

    #     for line in cohort_data:
    #         first, last, house, advisor, cohort_name = line.rstrip().split('|')
    #         all_data.append((f'{first} {last}', house, advisor, cohort_name))

    # return all_data


    ### Pythonic code
    with open(filename, 'r') as cohort_data:

        all_data = [(f"{line.rstrip().split('|')[0]} {line.rstrip().split('|')[1]}", line.rstrip().split('|')[2], line.rstrip().split('|')[3], line.rstrip().split('|')[4]) for line in cohort_data]

        return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Someone else')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    for full_name, _, _, cohort_name in all_data(filename):
        if full_name == name:
            return cohort_name
    

def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    ### Original answer
    all_last_names = set()
    repeat_last_names = set()

    with open(filename, 'r') as cohort_data:

        for line in cohort_data:
            _, last, _, _, _ = line.rstrip().split('|')

            if last in all_last_names:
                repeat_last_names.add(last)
          
            all_last_names.add(last)

        return repeat_last_names
                
    ### Pythonic code

def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    ### Original answer
    housemates = set()
    spec_house = ''
    spec_cohort_name = ''

    for full_name, house, _, cohort_name in all_data(filename):
        
        if full_name == name:
            spec_house = house
            spec_cohort_name = cohort_name
            break
    
    for full_name, house, _, cohort_name, in all_data(filename):
        
        if house == spec_house and cohort_name == spec_cohort_name and full_name != name:
            housemates.add(full_name)
    
    return housemates


    ### Pythonic code


            
            
            


    
            


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
