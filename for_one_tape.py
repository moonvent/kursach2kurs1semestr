class mt_for_one_tape:
    result_word = str()     # результирующее слово
    amount_of_steps = 0     # кол-во шагов для достижения целей
    tuple_alfabet = ('a', 'b', 'c')     # кортеж с литерами принадлежащим алфавиту

    state = None            # состояние, first_condition , second,
    number_state = str()    # тем самым меняя указатели на функции

    direction = '>'         # направление, в которое двигаемся , может быть >, <, stop
    letter = str()            # буква, которую мы сейчас рассматриваем
    cursor = 1              # курсор , то что бегает по строке

    """
        Машина тьюринга которая получает результаты второй(выдает первое слово) и третьей(выдает второе слово) мт,
        сравнивает эти слова, если они реверсивным выводит 1, если нет выводит 0.

        Как работает:
                Машина начинает свою работу с первой буквы слова, смотрит какая это буква,
            в зависимости от того какая это буква, переходит в состояние 2 3 или 4,
            после идет до края и исходя из состояния (2, 3 или 4), переходит в состояния
            5 6 или 7, соответсятвенно, далее, если буква соответствует состоянию, то есть
            5-ое состояние это состояние буквы а, если нашли букву а, затираем её, и отправляем в
            восьмое состояния, которое ведет каретку в начало и всё начинает заного.
            Если же буква не соответствует, к примеру ожидается a а стоит b, то состояние 5, 6 или 7
            переходит в состояние 9, затирает всю строчку и ставит 0, если же алгоритм доходит
            до конца удачно, то ставится 1.
    """

    def any_condition(self):
        """
            Функция состояния, условие - что делаем с символом на котором стоит,
            пример :
                if self.letter == '1':       # если заданный символ один (функция получает символ)
                    self.letter = '0'       # меняем букву, если прописано, то изменяем если не прописано то остается как было

                    self.direction = '>'    # изменяем направление движения, если прописано то изменяем, если нет, то остается как и было

                    self.number_of_state = self.second_condition            # в какое состояние переходим, 1 - функция называет first, 2 - second,
                                                                       # сколько состояний столько и методов состояний
                                                                       # если прописано, то изменяем если не прописано то остается как было

            Порядок именно такой, вначале идут то что меняется 100% и на что, допустим direction = '>' ,
            и только потом то, что меняется в зависимости от литеры.
        """
        pass

    def first_condition(self):
        self.number_state = '1'
        """
            Смотрим какая буква, затираем, и отправляем в нужное состояние:
            a -> 2
            b -> 3
            c -> 4

            Если же, после сверки обоих слов, когда на ленте осталась
            ничего, то ставим 1 и останавливаем машину.
        """
        self.direction = '>'
        if self.letter == 'a':
            self.letter = '_'
            self.state = self.second_condition
        elif self.letter == 'b':
            self.letter = '_'
            self.state = self.third_condition
        elif self.letter == 'c':
            self.letter = '_'
            self.state = self.fourth_condition
        elif self.letter == '_':
            self.letter = '1'
            self.direction = 'stop'

    def second_condition(self):
        """
            Двигаем до правого конца, после его достижения переходим в
            ПЯТОЕ состояние.
        """
        self.number_state = '2'
        self.direction = '>'
        if self.letter == '_':
            self.direction = '<'
            self.state = self.fifth_condition

    def third_condition(self):
        """
            Двигаем до правого конца, после его достижения переходим в
            ШЕСТОЕ состояние.
        """
        self.number_state = '3'
        self.direction = '>'
        if self.letter == '_':
            self.direction = '<'
            self.state = self.sixth_condition

    def fourth_condition(self):
        """
            Двигаем до правого конца, после его достижения переходим в
            СЕДЬМОЕ состояние.
        """
        self.number_state = '4'
        self.direction = '>'
        if self.letter == '_':
            self.direction = '<'
            self.state = self.seventh_condition

    def fifth_condition(self):
        self.number_state = '5'
        """
            В этом состоянии сверяем букву, если это A то переходим в состояние восемь,
            иначе в состояние девять, если это лябда, ставим 0 и завершаем работу программы.
        """
        self.direction = '<'
        if self.letter == 'a':
            self.letter = '_'
            self.state = self.eighth_condition
        elif self.letter in ('b', 'c'):
            self.letter = '_'
            self.state = self.ninth_condition
        elif self.letter == '_':
            self.letter = '0'
            self.direction = 'stop'

    def sixth_condition(self):
        """
            В этом состоянии сверяем букву, если это В то переходим в состояние восемь,
            иначе в состояние девять, если это лябда, ставим 0 и завершаем работу программы.
        """
        self.number_state = '6'
        self.direction = '<'
        if self.letter == 'b':
            self.letter = '_'
            self.state = self.eighth_condition
        elif self.letter in ('a', 'c'):
            self.letter = '_'
            self.state = self.ninth_condition
        elif self.letter == '_':
            self.letter = '0'
            self.direction = 'stop'

    def seventh_condition(self):
        """
            В этом состоянии сверяем букву, если это С то переходим в состояние восемь,
            иначе в состояние девять, если это лябда, ставим 0 и завершаем работу программы.
        """
        self.number_state = '7'
        self.direction = '<'
        if self.letter == 'c':
            self.letter = '_'
            self.state = self.eighth_condition
        elif self.letter in ('a', 'b'):
            self.letter = '_'
            self.state = self.ninth_condition
        elif self.letter == '_':
            self.letter = '0'
            self.direction = 'stop'

    def eighth_condition(self):
        """
            Данное состояние возвращает головку к первой букве слова.
        """
        self.number_state = '8'
        self.direction = '<'
        if self.letter == '_':
            self.direction = '>'
            self.state = self.first_condition

    def ninth_condition(self):
        """
            Данное состояние затирает все буквы слева, и если в конце выводит 0.
        """
        self.number_state = '9'
        self.direction = '<'
        if self.letter in self.tuple_alfabet:
            self.letter = '_'
        elif self.letter == '_':
            self.letter = '0'
            self.direction = 'stop'

    def heart(self, word, bot):
        """
            Сердце машины, то есть её работа, всё прописано тут, как она идет по состояниям, что возвращаем и т.д.

            Подробное описание:
                    При передачи слова в данную функцию, мы ставим текущее состояние на первое
                (меняем указатель переменной на функцию первого состояни), ставим головку в
                нужное место (курсор), далее преобразуем слово которое ввел пользователь
                из строки в список, для того чтоб можно было изменять в нем элементы, ибо
                строки в Python константны.
                    После всех приготовлений, переходим в цикл, который и будет выполнять
                всю работу по перемещению головки и захода в состояния.
                    Вначале мы берем из списка литеру на которой стоит головка(курсор),
                если не получается это сделать(ошибка) то это скорее всего из-за того что мы
                вышли за прописанные пределы (по умолчанию, слово веденное пользователем обрамляеся
                двумя L слева и справа, иногда требуется дойти до константы дальше, и для этого придумано
                выкидывание исключения, и если это произошло, просто добавляем константу L в конец списка,
                ВОЗМОЖНО кастыль:( ). После того как взяли нужную литеру переходи в состояние, на котором
                стоим, в нем проделываем нужные махинации и возвращаемся сюда. Тут, меняем литеру если её
                изменяли в состоянии, и с помозью условия и проверки переменной self.direction двигаемся
                либо, вправо влево, или останавливаемся, движения происходят увеличением или уменьшением
                переменной self.cursor. Если мт закончила свою работу, удаляем лишние L из списка,
                преобразовываем список в строку и возвращаем новое слово.
        """
        self.state = self.first_condition     # привязываем первое состояние к номеру состояния,
                                              # или же на каком состоянии мы стартуем
        word = list(word)   # преобразуем строку в список
        while True:     # бесконечный цикл, это и есть некая головка, которая будет ходить по литерам
            self.amount_of_steps += 1
            self.letter = word[self.cursor]      # получаем литеру на которой стоит головка
            temp_letter = self.letter
            self.state()      # проводим определенные операции с этой литерой
            word[self.cursor] = self.letter     # меняем символ который заменили в состоянии

            # записываем логи в файлы
            if bot is False:    # если пользователь ввёл слово, записываем логи
                with open('log.txt', 'a') as f:
                    temp_first_word = ''.join(word[:self.cursor]) + '(' + temp_letter.upper() + ')' + ''.join(word[1 + self.cursor:])
                    f.write('\n\n' + str(self.amount_of_steps) + '\tq' + self.number_state + '\t' + temp_first_word + '\n')

            # двигаемся в какую-либо сторону
            if self.direction == '>':
                self.cursor += 1
            elif self.direction == '<':
                self.cursor -= 1
            else:   # если self.direction == 'stop', останавливаем машину
                self.result_word = ''.join(word).replace('_', '')   # выходим из машины, соединяем полученное на выходе слово в строку и чистим от L
                return


if __name__ == '__main__':
    # mt = mt_for_one_tape()
    # mt.heart('_abba_', bot=False, cursor=1)
    # print(mt.result_word)
    pass
