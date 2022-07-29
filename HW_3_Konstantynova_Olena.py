# homework 3

student_exam_grade = ['student', 'grade', 'result: passed/failed']
list_of_grades = []                                                       # создаем пустой список
enter_exam_data = input('start - to enter data, stop - to finish: ')      # создаем переменную, которая запрашивает ввод данных: start для начала ввода и  stop - завершить ввод данных
while enter_exam_data != 'stop':                                          # создаем цикл, в котором запрашивается ввод данных до тех пор, пока не будет введено слово stop
    input_exam_data = input(f'enter information  {student_exam_grade}: ')
    exam_data = tuple(map(str, input_exam_data.split(',')))               # переменная, создает кортеж из введенных данных по разделителю ","
    list_of_grades.append(exam_data)                                      # кортеж, созданый в предыдущей строке, записывается как элемент в пустой список, созданный до цикла
    enter_exam_data = input('enter data, stop - to finish: ')             # запрашиваем введение следующих данных

print(list_of_grades)

s = sorted(list_of_grades, key=lambda i: i[1])                            # сортируем получившийся список результатов экзамена по оценкам
print(s)


idx_passed = []                                      # создаем пустой список, в который будем записыватьвсе индексы кортежей с результатом экзамена - passed
for i in s:                                          # перебираем все элементы сортированного списка результатов экзамена
    for n in i:                                      # перебираем все элементы каждого результата экзамена
        if n == 'passed':                            # если находим элемент "passed", то добавляем его в список
            idx_passed.append(s.index(i))


idx_failed = []                                     #  аналогично для результатов экзамена, содержащих "failed"
for i in s:
    for n in i:
        if n == 'failed':
            idx_failed.append(s.index(i))


for i in s:                                         # находим самую низкую оценку за экзамен среди студентов, которые сдали экзамен
    for n in i:
        if s.index(i) == min(idx_passed):
            idx_grade_passed = i[1]


for i in s:                                         # находим самую высокую оценку за экзамен среди студентов, которые НЕсдали экзамен
    for n in i:
        if s.index(i) == max(idx_failed):
            idx_grade_failed = i[1]


if max(idx_failed) < min(idx_passed):                                          # сравниваем индексы кортежей, содержащих самую высокую оценку среди несдавших экзамен и самую низкую из сдавших
    print('Exam results are set correctly and consistently')
    # find threshold per index
    print(f'examination threshold: {idx_grade_failed} - {idx_grade_passed}')   # находим порог сдачи экзамена
else:
    print('Exam results are incorrect')                                        # если peзультаты экзамена внесены неверно, выводим сообщение по этом


# К сожалению, в моем коде не внесены все возможные варианты, когда данные изначально вводятся пользователем некорректно, с лишними пробелами и прочее.
# но в "идельном мире" код работает: когда данные внесены правильно, через запятую без пробела, и есть данные со студентами как сдавшими экзамен, так и НЕсдавшими.
# постараюсь в следующих домашних работах учитывать все нюансы. Спасибо)

'''
для проверки правильно внесенных данных
s1,98,passed
s2,68,passed
s3,59,passed
s4,35,failed
s5,49,failed


для проверки НЕправильно введенных даных
s1,98,passed
s2,68,failed
s3,59,passed
s4,31,failed
s5,53,passed
'''