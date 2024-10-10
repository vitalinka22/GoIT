import logging
from my_logger import get_logger

logger = get_logger("my_loger", logging.DEBUG)


def baz(num: int):
    logger.info("start")
    foo_ = 100
    result = foo_ + num
    logger.debug(f"{result}")
    return result


def foo(num: int):
    logger.error("AAAAAAAAA!")


if __name__ == "__main__":
    baz(500)
    foo(100)
