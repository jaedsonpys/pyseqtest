from datetime import datetime
from time import sleep


class SeqTest(object):
    """
    Teste em sequência.

    Todos os testes devem iniciar como
    "test"
    """

    def __init__(self):
        self._last_test = None

    def run(self) -> None:
        """Start tests.

        :return: None
        """

        print('PySeqTest')
        print('=========\n')

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
            test_name = test.__name__
            print(f'{test_name}... ', end='')

            self._last_test = test_name
            start_time = datetime.now()

            test()
            finish_time = datetime.now() - start_time
            print(f'finished in {finish_time}')


if __name__ == '__main__':
    SeqTest().run()
