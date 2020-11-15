import csv
import numpy as np
import datetime

num_atoms = 100
atoms = np.ones(num_atoms, dtype=np.int)

def log_result(array, time):
    with open('./reslt.csv', 'a') as f:
        writer = csv.writer(f)
        nmsg = "{} 回目".format(time)
        pmsg = "{} %".format(cal_uncoll_rate(array))
        result_row = np.hstack((nmsg, pmsg, array))
        writer.writerow(result_row)


def collapse_prob(rate):

    nums = np.arange(1, 1001, dtype=np.int)
    selected = np.random.choice(nums, 1)[0]
    if selected >= rate:
        return 1
    else:
        return 0

def cal_uncoll_rate(array):
    length = len(array)
    not_coll_num = array.sum()

    not_coll_rate = 100 * not_coll_num / length

    return not_coll_rate

def is_end(array, rate):

    uncoll_rate = cal_uncoll_rate(array)

    if uncoll_rate < rate:
        return True
    else:
        return False

# Record Rarameters & Start msg
with open('./reslt.csv', 'a') as f:
    writer = csv.writer(f)
    start_time = datetime.datetime.now()
    nmsg = "Start: {}".format(start_time)
    # pmsg = "{} %".format(cal_uncoll_rate(array))
    # msg_row = np.hstack((nmsg, pmsg, array))
    msg_row = np.hstack((nmsg, "apple"))
    writer.writerow(msg_row)

times = 1

while True:

    for i in range(num_atoms):

        if atoms[i] == 1:
            atoms[i] = collapse_prob(50)
        else:
            pass

    log_result(atoms, times)

    times += 1

    if is_end(atoms, 50):
        break
    else:
        pass

# Record End msg
with open('./reslt.csv', 'a') as f:
    writer = csv.writer(f)
    end_time = datetime.datetime.now()
    elapsed = end_time - start_time
    end_msg = ["{}".format(elapsed)]
    writer.writerow(end_msg)
