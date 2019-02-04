# -*- coding:utf-8 -*-
from _datetime import datetime


class FunctionTester:

    def __init__(self, test_function, report_file, *func_args):
        self.__result = 0
        self.__f = test_function
        self.__func_args = func_args
        self.report_file = report_file
        self.__start = None
        self.__end = None
        self.__diff = None

    def __call_func(self, *args, **kwargs):
        return self.__f(*args, **kwargs)

    def show_info(self, message, attribute):
        info = message + ' ' + attribute
        print(info)
        return info

    def __enter__(self):

        f_name = self.show_info('Функция', self.__f.__name__)

        self.__start = datetime.now()
        s_time = self.show_info('Начало работы:', str(self.__start))

        result = self.__call_func(*self.__func_args)

        self.__end = datetime.now()
        e_time = self.show_info('Завершение работы:', str(self.__end))

        self.__diff = self.__end - self.__start
        d_time = self.show_info('Затрачено времени:', str(self.__diff))

        self.file = open(self.report_file, 'w', encoding='utf-8')
        report_items = (f_name, s_time, e_time, d_time)
        for report_item in report_items:
            self.file.write(report_item + '\n')
        self.file.write("Результат работы функции: %s\n" % result)

        return self.file

    def __exit__(self, *error_attributes):
        print('Освобождение ресурсов...')
        self.file.close()
        if any(error_attributes):
            with open('error.log', '+a') as f:
                print('Program name: %s ' % self.__f.__name__, file=f)
                for error in error_attributes:
                    print(error, file=f)


def create_string_from_list(symbol_count):
    return ''.join([str(x) for x in range(symbol_count)])


def create_string_from_string(symbol_count):
    s = ''
    for i in range(symbol_count):
        s += str(i)
    return s


def compare_functions(func1, func2, file_1, file_2, times):

    with FunctionTester(func1, file_1, times) as f:
        f.write("Дата тестирования: %s" % str(datetime.now()))

    print()

    with FunctionTester(func2, file_2, times) as f:
        f.write("Дата тестирования: %s" % str(datetime.now()))


if __name__ == '__main__':

    compare_functions(
                        create_string_from_list,
                        create_string_from_string,
                        "%s.txt" % create_string_from_list.__name__,
                        "%s.txt" % create_string_from_string.__name__,
                        1000000)
