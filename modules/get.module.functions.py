import importlib
import sys
from inspect import getmembers, isfunction


def get_module_functions(module_name):
    """
    Получаем все функции из модуля как объекты.
    """
    importlib.import_module(module_name)
    module = sys.modules[module_name]
    module_functions = getmembers(module, isfunction)
    return {func[0]: func[1] for func in module_functions}


if __name__ == '__main__':
    print(get_module_functions(__name__))