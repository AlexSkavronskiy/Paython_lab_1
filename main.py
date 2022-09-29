import csv
with open('books.csv','r',encoding='cp1251') as file:
    reader=csv.reader(file,delimiter=';')
    found_result=[]
    c_record=-1
    c_found=0
    c_refs=0
    refs=[]
    c_long_name=0
    print('Поиск книги по автору')
    name_author=input('Введите имя автора: ')
    for row in reader:
        row_txt=[]
        for i in row:
            row_txt+=[i]
        if len(row_txt[1])>30:
            c_long_name+=1
        if name_author in row_txt[3]:
            found_result.append(row_txt[1])
            c_found+=1
        if  0 <c_refs <21:
            date=row_txt[6]
            refs.append(f'{c_refs}: {row_txt[3]}. {row_txt[1]} - {date[6:10]}\n')
        c_refs+=1
        c_record+=1
    with open('refs.txt','w') as refs_file:
        refs_file.write("\n".join(refs))
if c_found == 0:
    print('Книга с данным автором не найдена')
else:
    print(f'Было найдено {c_found} записей:')
    print('\n'.join(found_result))
print(f'Количество записей: {c_found}\n')
print(f'Количество записей с названием больше 30 символов: {c_long_name}')

