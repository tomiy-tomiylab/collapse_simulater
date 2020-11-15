import csv
import numpy as np

length = 100
atoms = np.ones(length, dtype=np.int)

def log_result(array, time):
    with open('./reslt.csv', 'a') as f:
        writer = csv.writer(f)
        nmsg = "{} 回目".format(time)
        pmsg = "{} %".format(cal_ncoll_rate(array))
        result_row = np.hstack((nmsg, pmsg, array))
        writer.writerow(result_row)


def prob_collapse():

    judg = np.random.choice([True, False], 1)
    if judg:
        return 1
    else:
        return 0

def cal_ncoll_rate(array):
    length = len(array)
    not_coll_num = array.sum()

    not_coll_rate = 100 * not_coll_num / length

    return not_coll_rate

def judg_end(array, rate):

    not_coll_rate = cal_ncoll_rate(array)

    if not_coll_rate < rate:
        return True
    else:
        return False

num_times = 1

while True:

    for i in range(length):

        if atoms[i] == 1:
            atoms[i] = prob_collapse()
        else:
            pass

    log_result(atoms, num_times)

    num_times += 1

    if judg_end(atoms, 10):
        break
    else:
        pass
