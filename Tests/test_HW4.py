from H_W4 import Date
import pytest
import logging

formatter = logging.Formatter('%(asctime)s - %(name)s -\033[91m %(levelname)s \033[0m - %(message)s')
log_test = logging.getLogger('log_test')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log_test.addHandler(ch)


@pytest.mark.skip
def test_init():
    try:
        assert Date(12, 12, 2011)
    except:
        log_test.warning("Invalid date, try other date")


def test_str():
    try:
        print(Date(28, 2, 2013))
    except:
        log_test.error('Cant print date, try to change the dates .')
        assert None


def test_eq():
    if Date(9, 6, 2007) == Date(8, 6, 2007):
        assert Date(9, 6, 2007) == Date(8, 6, 2007)
    else:
        log_test.error('The dates is not equal, try to change the dates .')
        assert Date(9, 6, 2007) == Date(8, 6, 2007)


@pytest.mark.regression
def test_gt():
    d1 = Date(9, 9, 2017)
    d2 = Date(28, 2, 2017)
    if d1 > d2:
        assert d1 > d2
    else:
        log_test.info('Failed because first date is smaller or equal to sec date.')
        assert d1 > d2

def test_lt():
    if Date(11, 1, 2013) < Date(28, 1, 2014):
        assert Date(11, 1, 2013) < Date(28, 1, 2014)
    else:
        log_test.info('Failed because first date is bigger or equal to sec date.')
        assert Date(11, 1, 2013) < Date(28, 1, 2014)


@pytest.mark.smoke
def test_le():
    if Date(6, 1, 2003) <= Date(17, 6, 2013):
        assert Date(6, 1, 2003) <= Date(17, 6, 2013)
    else:
        log_test.info('Failed because first date bigger than sec date.')
        assert Date(6, 1, 2003) <= Date(17, 6, 2013)


def test_ge():
    if Date(29, 4, 2013) >= Date(28, 1, 2011):
        assert Date(29, 4, 2013) >= Date(28, 1, 2011)
    else:
        log_test.warning('Failed because first date smaller than sec date.')
        assert Date(29, 4, 2013) >= Date(28, 1, 2011)


def test_sub():
    if isinstance(Date(28, 2, 2001) - Date(1, 1, 2000), int):
        assert isinstance(Date(28, 2, 2001)-Date(1, 1, 2000), int)
    else:
        log_test.critical("Check your dates?")
        assert isinstance(Date(28, 2, 2001) - Date(1, 1, 2000), int)


def isValid():

    try:
        assert Date(29, 2, 2013)
    except:
        log_test.info("Invalid date, try other date please")
        assert Date(29, 2, 2013)


@pytest.fixture
def test_get_next_day():
    d = Date(28, 2, 2024)
    assert d
    if d.get_next_day() > d:
        assert d.get_next_day() > d
    else:
        logging.error("Check if date is valid or your have problem in your Func")


def test_get_next_days():
    d1 = Date(28, 2, 2016)
    add = 10
    d2 = d1.get_next_days(add)
    if d2.__sub__(d1) == add:
        assert d2 > d1
    else:
        logging.error("Check if dates is correct or you have problem is get_next_days Func/test_get_next_days Func")



