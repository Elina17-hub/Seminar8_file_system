from return_data_file import data_file



def copy_file():
    data, nf = data_file()
    answer = int(input("выберите файл,в который вы хотите перенести данные(от 1 до 2):"))
    while (answer < 1 or answer > 2) or answer == nf:
       answer = int(input("ошибка! вы ввели некоректное значение" 
                          "выберите файл,в который вы хотите перенести данные(от 1 до 2):")) 
    with open(f'db/data_{answer}.txt','r', encording='utf-8') as file:
        count_row_data_end = len(file.readlines()) + 1
    data = [f'{i + count_row_data_end};{data[i].split(";")[1]};'
            f'{data[i].split(";")[2]};'
            f'{data[i].split(";")[3]};'
            f'{data[i].split(";")[4]}'
             for i in range(len(data))] 
    with open(f'db/data_{answer}.txt','a', encording='utf-8') as file:
        file.writelines(data)
    print("данные успешно скопированы!")