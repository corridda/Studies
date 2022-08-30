# import logging
#
# logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
#                     format="%(asctime)s %(levelname)s %(message)s")
# logging.debug("A DEBUG Message")
# logging.info("An INFO")
# logging.warning("A WARNING")
# logging.error("An ERROR")
# logging.critical("A message of CRITICAL severity")

# x = 3
# y = 0
#
# logging.info(f"The values of x and y are {x} and {y}.")
# try:
#     z = x/y
#     logging.info(f"x/y successful with result: {z}.")
# except ZeroDivisionError as err:
#     logging.error("ZeroDivisionError",exc_info=True)


"""Настройка логирования с помощью пользовательских логгеров, обработчиков и форматировщиков"""
# x_vals = [2, 3, 6, 4, 10]
# y_vals = [5, 7, 12, 0, 1]
#
# for x_val, y_val in zip(x_vals, y_vals):
#     x, y = x_val, y_val
#     logging.info(f"The values of x and y are {x} and {y}.")
#     try:
#         x / y
#         logging.info(f"x/y successful with result: {x / y}.")
#     except ZeroDivisionError as err:
#         logging.exception("ZeroDivisionError")


"""Настройка пользовательского логгера для модуля main"""
import logging
from test_div import test_division

# получение пользовательского логгера и установка уровня логирования
py_logger = logging.getLogger(__name__)
py_logger.setLevel(logging.INFO)

# настройка обработчика и форматировщика в соответствии с нашими нуждами
py_handler = logging.FileHandler(f"{__name__}.log", mode='w')
py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

# добавление форматировщика к обработчику
py_handler.setFormatter(py_formatter)
# добавление обработчика к логгеру
py_logger.addHandler(py_handler)

py_logger.info(f"Testing the custom logger for module {__name__}...")

x_vals = [2, 3, 6, 4, 10]
y_vals = [5, 7, 12, 0, 1]

for x_val, y_val in zip(x_vals, y_vals):
    x, y = x_val, y_val
    # вызов test_division
    test_division(x, y)
    py_logger.info(f"Call test_division with args {x} and {y}")
