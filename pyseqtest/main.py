from datetime import datetime
from time import sleep

from typing import Callable
from typing import Any


class SeqTest(object):
    """
    Teste em sequência.

    Todos os testes devem iniciar como
    "test"
    """

    def __init__(self):
        self._last_test = None
        self._tests_exec = 0

    def _run_test(self, method_test: Callable) -> None:
        method_name = method_test.__name__
        self._last_test = method_name

        print(f'{method_name}... ', end='')
        start_time = datetime.now()

        # run test
        method_test()

        finish_time = datetime.now() - start_time
        print(f'finished in {finish_time}')

    def run(self) -> None:
        """Start tests.

        :return: None
        """

        print('PySeqTest')
        print('=========')

        def filter_methods(x) -> list:
            methods = []

            for attr in x:
                attr_object = self.__getattribute__(attr)
                if attr.startswith('test') and callable(attr_object):
                    methods.append(attr_object)

            return methods

        methods_test = filter_methods(self.__dir__())

        total_tests = len(methods_test)
        print(f'{total_tests} testes presentes.\n')

        # try run setup
        try:
            setup = self.__getattribute__('setup')
        except AttributeError:
            pass
        else:
            setup()

        # run tests
        for test in methods_test:
            self._run_test(test)

        # finish all tests
        print(f'\nAfirmações: {self._tests_exec}')
        print('\033[32m[ OK ]\033[m Testes finalizados')

    def is_true(self, condition: Any, msg_error: str = None) -> None:
        if not condition:
            print('\n')
            if msg_error:
                print(f'\033[31m[ ERROR ]\033[m {self._last_test}: {msg_error}')
            else:
                print(f'\033[31m[ ERROR ]\033[m{self._last_test}: Condição não é verdadeira')

            exit(0)

        self._tests_exec += 1


class Test(SeqTest):
    def __init__(self):
        super().__init__()

    def test_database(self):
        sleep(2)

    def test_database_2(self):
        sleep(2)

    def test_database_3(self):
        sleep(2)


if __name__ == '__main__':
    Test().run()
