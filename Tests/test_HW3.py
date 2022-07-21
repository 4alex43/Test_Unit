import pytest
from H_w3 import *
import logging
import statistics

formatter = logging.Formatter('%(asctime)s - %(name)s -\033[91m %(levelname)s \033[0m - %(message)s')
log_test = logging.getLogger('log_test')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log_test.addHandler(ch)

def test_split_male_female():
    data_set = {
        1234234: {"name": "Tal", "sex": "male", "age": 22},
        2432442: {"name": "Shay", "sex": "female", "age": 33},
        3765765: {"name": "Tamir", "sex": "male", "age": 45},
        4765756: {"name": "Daniel", "sex": "female", "age": 36},
    }
    data_set_m = split_male_female(data_set)["Male"]
    data_set_f = split_male_female(data_set)["Female"]

    if len(data_set_m) + len(data_set_f) == len(data_set):
        assert len(data_set_m) + len(data_set_f) == len(data_set)
    else:
        log_test.warning('Something wrong at split, check your Func')
        assert len(data_set_m) + len(data_set_f) == len(data_set)



def test_find_median_average():
    data_set = {
        5574747: {"name": "Alex", "sex": "male", "age": 67, "job:": "QA automation"},
        7757445: {"name": "2pac", "sex": "male", "age": 120, "Alive or dead": "Alive"},
        6213213: {"name": "Tali", "sex": "female", "age": 98}
    }

    res = find_median_average(data_set)
    avg = res["Average"]
    median = res["median"]
    avg_test = (67 + 120 + 98) / 3
    median_test = statistics.median([67, 120, 98])

    if avg == avg_test and median_test == median:
        assert res
    else:
        assert logging.error('Error in calculating avg and median ')



def test_print_values_above():
    data_set = {
        1: {"name": "Tal", "sex": "male", "age": 22},
        2: {"name": "Shay", "sex": "female", "age": 33},
        3: {"name": "Tamir", "sex": "male", "age": 45},
        4: {"name": "Daniel", "sex": "female", "age": 36},
        5: {"name": "Alex", "sex": "male", "age": 67, "job:": "QA automation"},
        6: {"name": "2pac", "sex": "male", "age": 120, "Alive or dead": "Alive"},
        7: {"name": "Tali", "sex": "female", "age": 98}
    }

    try:
        print_values_above(data_set, 20)
    except:
        log_test.error('Nothing to print')
        assert None



