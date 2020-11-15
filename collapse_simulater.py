import csv
import numpy as np
import datetime

# "1"を崩壊していない原子、"0"を崩壊した原子として扱う
# "1"は不安定な原子、"0"は安定な原子で一度"1"が崩壊するとそれ以上は崩壊しない場合を想定
# 例えば、"1"が"Cs137","0"が"Ba137"
num_atoms = 100     # 原子の数[個]
collapse_rate = 2  # 1judgeで崩壊する確率[‰] intで指定
atoms = np.ones(num_atoms, dtype=np.int)  # 1で埋められた配列
end_rate = 3.175       # 未崩壊の原子の割合がこの値を切るとシミュレーション停止 [%]

def log_result(array, time):
    # 結果を保存
    with open('./reslt.csv', 'a') as f:
        writer = csv.writer(f)
        nmsg = "{} 回目".format(time)                 # 何回目のjudgeか
        pmsg = "{} %".format(cal_uncoll_rate(array))  # 未崩壊率
        result_row = np.hstack((nmsg, pmsg, array))
        writer.writerow(result_row)


def collapse_prob(rate):
    # 崩壊するか決定
    nums = np.arange(1, 1001, dtype=np.int)
    selected = np.random.choice(nums, 1)[0]
    if selected >= rate:
        return 1
    else:
        return 0

def cal_uncoll_rate(array):
    # 未崩壊率を計算
    length = len(array)
    not_coll_num = array.sum()

    not_coll_rate = 100 * not_coll_num / length

    return not_coll_rate

def is_end(array, rate):
    # 未崩壊率が指定値を切ってるか確認
    uncoll_rate = cal_uncoll_rate(array)

    if uncoll_rate < rate:
        return True
    else:
        return False

# Record Rarameters & Begin msg
with open('./reslt.csv', 'a') as f:
    writer = csv.writer(f)
    start_time = datetime.datetime.now()
    stmsg = "Start: {}".format(start_time)
    nmsg = "Atom: {}".format(num_atoms)
    rmsg = "Collapse rate: {} ‰".format(collapse_rate)
    begin_msg = np.hstack((stmsg, nmsg, rmsg))
    writer.writerow(begin_msg)

times = 1  # 何回目のjdgeか

while True:

    for i in range(num_atoms):

        if atoms[i] == 1:
            atoms[i] = collapse_prob(collapse_rate)
        else:
            pass

    log_result(atoms, times)

    times += 1

    if is_end(atoms, end_rate):
        break
    else:
        pass

# Record End msg
with open('./reslt.csv', 'a') as f:
    writer = csv.writer(f)
    end_time = datetime.datetime.now()
    etmsg = "End: {}".format(end_time)
    elapsed = end_time - start_time
    emsg = "Elapsed: {}".format(elapsed)
    end_msg = np.hstack((etmsg, emsg))
    writer.writerow(end_msg)
