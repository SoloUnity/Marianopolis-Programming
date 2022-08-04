def exercise1():
    import math
    print(math.cos(math.pi))
    help(math.cos)

    #-1.0
    #Help on built-in function cos in module math:
    #cos(x, /)
    #Return the cosine of x (measured in radians).

    print(cos(pi))
    #Traceback error

    from math import cos , pi
    print(cos(pi))
    #Prints -1.0

    print(math.cos(math.pi))
    #traceback

def exercise2():
    N_FIELDS = 5  # number of items on each row in the file.

    # Indices of the fields.
    SEPAL_LENGTH = 0
    SEPAL_WIDTH = 1
    PETAL_LENGTH = 2
    PETAL_WIDTH = 3
    SPECIES = 4

    N_SPECIES = 3

    # Codes for the species.
    IRIS_SETOSA = 0
    IRIS_VERSICOLOR = 1
    IRIS_VIRGINICA = 2

    def field_index_to_name(index):
        '''Converts a field index to a human-readable name.'''
        field_names = ('sepal length', 'sepal width', 'petal length', 'petal width', 'species')
        if index < 0 or index >= N_FIELDS:
            return "invalid field"
        return field_names[index]

    def latin_name_to_number(name):
        '''Converts the Latin scientific names in the file to a numeric
        code. The numeric code is used instead of the name in order to
        allow our data analysis to compute correlations of each of the
        four measurements with the species.

        You will use this function in iris_data() to convert the name to
        a number.
        '''
        if name == 'Iris-setosa':
            return IRIS_SETOSA
        elif name == 'Iris-versicolor':
            return IRIS_VERSICOLOR
        elif name == 'Iris-virginica':
            return IRIS_VIRGINICA
        else:
            print('Unrecognized species:', name)
            return -1

    def number_to_latin_name(number):
        '''Convert back from a species code number to a human-readable
        string. Used primarily for data visualization.'''
        if number == IRIS_SETOSA:
            return "Iris setosa"
        elif number == IRIS_VERSICOLOR:
            return "Iris versicolor"
        elif number == IRIS_VIRGINICA:
            return "Iris virginica"
        else:
            return "Unknown species: " + str(number)

    def get_column(data, col):
        '''Extract a particular column of data from the data object.'''
        return [fields[col] for fields in data]

    def get_species(data, species):
        '''Extract only the data associated with a particular species.'''
        return [fields for fields in data if fields[-1] == species]
    def iris_data():
        '''Opens the data file and converts the contents into a Python "list
        of lists."

        Each data line in the file looks like this:

        5.0 3.3 1.4 0.2 Iris-setosa

        The 5 fields are as follows:
        1. the sepal length in cm
        2. the sepal width in cm
        3. the petal length in cm
        4. the petal width in cm.
        5. the latin name of the species, either:
            Iris-setosa, Iris-versicolor, or Iris-virginica

        The file may also contain comment lines that begin with a '#'
        character. Your code must ignore these!

        '''
        file = open('/Users/gordonng/Downloads/lab8/iris.txt')
        data = []
        for line in file:
            if line[0] == '#':
                continue
            else:
                lineSplit = line.split()
                for value in range(len(lineSplit)-1):
                    lineSplit[value] = float(lineSplit[value])
                lineSplit[4] = latin_name_to_number(lineSplit[4])
                data.append(lineSplit)

            # 1. You must ignore lines that start with a hash '#' character.
            # 2. You must process each line by splitting it into fields, and then
            # converting the fields into numeric types. You will then append
            # the list of fields onto the end of the data list.
            # 3. If you do everything correctly, you should have a list of
            # 150 sublists, and each sublist should contain 5 items. The
            # first sublist will correspond to the first line in the file, so
            # it should contain [5.1, 3.5, 1.4, 0.2, 0]. The first four
            # items correspond to the float measurements. The final item is
            # the integer code corresponding to the species, IRIS_SETOSA.
            pass
        file.close()
        print(data)
        return data
    iris_data()


def exercise3and4():
    import irisfile
    import statistics
    N_FIELDS = 5  # number of items on each row in the file.

    # Indices of the fields.
    SEPAL_LENGTH = 0
    SEPAL_WIDTH = 1
    PETAL_LENGTH = 2
    PETAL_WIDTH = 3
    SPECIES = 4

    N_SPECIES = 3

    # Codes for the species.
    IRIS_SETOSA = 0
    IRIS_VERSICOLOR = 1
    IRIS_VIRGINICA = 2

    def field_index_to_name(index):
        '''Converts a field index to a human-readable name.'''
        field_names = ('sepal length', 'sepal width', 'petal length', 'petal width', 'species')
        if index < 0 or index >= N_FIELDS:
            return "invalid field"
        return field_names[index]

    def latin_name_to_number(name):
        '''Converts the Latin scientific names in the file to a numeric
        code. The numeric code is used instead of the name in order to
        allow our data analysis to compute correlations of each of the
        four measurements with the species.

        You will use this function in iris_data() to convert the name to
        a number.
        '''
        if name == 'Iris-setosa':
            return IRIS_SETOSA
        elif name == 'Iris-versicolor':
            return IRIS_VERSICOLOR
        elif name == 'Iris-virginica':
            return IRIS_VIRGINICA
        else:
            print('Unrecognized species:', name)
            return -1

    def number_to_latin_name(number):
        '''Convert back from a species code number to a human-readable
        string. Used primarily for data visualization.'''
        if number == IRIS_SETOSA:
            return "Iris setosa"
        elif number == IRIS_VERSICOLOR:
            return "Iris versicolor"
        elif number == IRIS_VIRGINICA:
            return "Iris virginica"
        else:
            return "Unknown species: " + str(number)

    def get_column(data, col):
        '''Extract a particular column of data from the data object.'''
        return [fields[col] for fields in data]

    def get_species(data, species):
        '''Extract only the data associated with a particular species.'''
        return [fields for fields in data if fields[-1] == species]

    file = open('/Users/gordonng/Downloads/lab8/iris.txt')
    data = []
    IRIS_SETOSA = 0
    IRIS_VERSICOLOR = 1
    IRIS_VIRGINICA = 2
    SEPAL_LENGTH = 0
    SEPAL_WIDTH = 1
    PETAL_LENGTH = 2
    PETAL_WIDTH = 3
    SPECIES = 4

    N_SPECIES = 3
    for line in file:
        if line[0] == '#':
            continue
        else:
            lineSplit = line.split()
            for value in range(len(lineSplit)-1):
                lineSplit[value] = float(lineSplit[value])
            lineSplit[4] = irisfile.latin_name_to_number(lineSplit[4])
            data.append(lineSplit)
        pass
    file.close()


    petalWidth = irisfile.get_column(data, PETAL_WIDTH)
    petalLength = irisfile.get_column(data, PETAL_LENGTH)
    sepalWidth = irisfile.get_column(data, SEPAL_WIDTH)
    sepalLength = irisfile.get_column(data, SEPAL_LENGTH)

    petalWidth1 = irisfile.get_column(irisfile.get_species(data, IRIS_SETOSA), PETAL_WIDTH)
    petalLength1 = irisfile.get_column(irisfile.get_species(data, IRIS_SETOSA), PETAL_LENGTH)
    sepalWidth1 = irisfile.get_column(irisfile.get_species(data, IRIS_SETOSA), SEPAL_WIDTH)
    sepalLength1 = irisfile.get_column(irisfile.get_species(data, IRIS_SETOSA), SEPAL_LENGTH)

    petalWidth2 = irisfile.get_column(irisfile.get_species(data, IRIS_VERSICOLOR), PETAL_WIDTH)
    petalLength2 = irisfile.get_column(irisfile.get_species(data, IRIS_VERSICOLOR), PETAL_LENGTH)
    sepalWidth2 = irisfile.get_column(irisfile.get_species(data, IRIS_VERSICOLOR), SEPAL_WIDTH)
    sepalLength2 = irisfile.get_column(irisfile.get_species(data, IRIS_VERSICOLOR), SEPAL_LENGTH)

    petalWidth3 = irisfile.get_column(irisfile.get_species(data, IRIS_VIRGINICA), PETAL_WIDTH)
    petalLength3 = irisfile.get_column(irisfile.get_species(data, IRIS_VIRGINICA), PETAL_LENGTH)
    sepalWidth3 = irisfile.get_column(irisfile.get_species(data, IRIS_VIRGINICA), SEPAL_WIDTH)
    sepalLength3 = irisfile.get_column(irisfile.get_species(data, IRIS_VIRGINICA), SEPAL_LENGTH)
    def formatted(x):
        return ("{} {} {} {}".format(min(x), max(x), round(statistics.mean(x), 2),round(statistics.stdev(x), 2)))
    print("Combined data: ")
    print("sepal length:",formatted(sepalLength))
    print("sepal width:",formatted(sepalWidth))
    print("petal length:",formatted(petalLength))
    print("petal width:",formatted(petalWidth))

    print("For species Iris setosa")
    print("sepal length:", formatted(sepalLength1))
    print("sepal width:", formatted(sepalWidth1))
    print("petal length:", formatted(petalLength1))
    print("petal width:", formatted(petalWidth1))

    print("For species Iris versicolor")
    print("sepal length:", formatted(sepalLength2))
    print("sepal width:", formatted(sepalWidth2))
    print("petal length:", formatted(petalLength2))
    print("petal width:", formatted(petalWidth2))

    print("For species Iris virginica")
    print("sepal length:", formatted(sepalLength3))
    print("sepal width:", formatted(sepalWidth3))
    print("petal length:", formatted(petalLength3))
    print("petal width:", formatted(petalWidth3))

    import matplotlib.pyplot as plt

    colors = ('red', 'blue', 'green')

    # List of names used in the 'legend' below.
    names = []

    j = IRIS_SETOSA
    k = IRIS_VERSICOLOR
    p = IRIS_VIRGINICA

    names.append(number_to_latin_name(j))
    names.append(number_to_latin_name(k))
    names.append(number_to_latin_name(p))
    s = get_species(data, j)
    l = get_species(data,k)
    i = get_species(data,p)

    x = get_column(s, PETAL_LENGTH)
    y = get_column(s, PETAL_WIDTH)
    plt.scatter(x, y, color=colors[j])
    plt.scatter(get_column(l, PETAL_LENGTH), get_column(l, PETAL_WIDTH), color=colors[k])
    plt.scatter(get_column(i, PETAL_LENGTH), get_column(i, PETAL_WIDTH), color=colors[p])

    plt.xlabel('petal length, cm')
    plt.ylabel('petal width, cm')

    plt.legend(names)
    plt.show()

exercise3and4()

