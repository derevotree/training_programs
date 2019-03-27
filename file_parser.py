"""Для примера я вложил файл events.txt
    скрипт выделяет все строки с окончанием NOK
    и показывает сколько записей с NOK
    каждую минуту/час/день/месяц"""

file_input = 'events.txt'
file_output = 'out.txt'


class NumOfEvents:
    def __init__(self, path_input, path_output):
        self.path_input = path_input
        self.path_output = path_output
        self.count = 1
        self.past_minute = None

    def sort_events(self):
        """ Данный метод не только сортирует, но там же и записывает данные
            т.к. ссылкается на метод record"""

        with open(self.path_output, 'w') as file_out:
            with open(self.path_input, 'r') as file_in:
                for line in file_in:
                    line = line[:-1]
                    if 'NOK' in line:
                        self.record(file=file_out, line=line)
                file_out.write(f'{self.past_minute}] {str(self.count)} \n')

    def record(self, file, line):
        """По умолчанию идёт запись за каждую минуту"""

        if line[0:17] == self.past_minute:
            self.count += 1
            self.past_minute = line[0:17]
        else:
            if self.past_minute is not None:
                file.write(f'{self.past_minute}] {str(self.count)} \n')
                self.count = 1
            self.past_minute = line[0:17]


class NumOfEventsByHour(NumOfEvents):

    def record(self, file, line):
        if line[0:14] == self.past_minute:
            self.count += 1
            self.past_minute = line[0:14]
        else:
            if self.past_minute is not None:
                file.write(f'{self.past_minute[:-2]}at {self.past_minute[-2:]} o-clock] {str(self.count)} \n')
                self.count = 1
            self.past_minute = line[0:14]


class NumOfEventsByDay(NumOfEvents):

    def record(self, file, line):
        if line[0:11] == self.past_minute:
            self.count += 1
            self.past_minute = line[0:11]
        else:
            if self.past_minute is not None:
                file.write(f'{self.past_minute}] {str(self.count)} \n')
                self.count = 1
            self.past_minute = line[0:11]


class NumOfEventsByMonth(NumOfEvents):

    def record(self, file, line):
        if line[0:8] == self.past_minute:
            self.count += 1
            self.past_minute = line[0:8]
        else:
            if self.past_minute is not None:
                file.write(f'{self.past_minute}] {str(self.count)} \n')
                self.count = 1
            self.past_minute = line[0:8]


num_of = NumOfEventsByDay(path_input=file_input, path_output=file_output)
num_of.sort_events()
