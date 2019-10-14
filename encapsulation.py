# THIS FILE IS CURRENTLY USELESS#

import core
import pandas as pd
import sys

def main(argv):
    import core
    core = core.Admission_Predictor()
    l=[]
    # ##########        take in new input     ###############
    for i in range(7):
        l.append(argv[i])

    # l = [337, 118, 4, 4.5, 4.5, 9.65, 1]  # l is supposed to be the input
    # df = pd.DataFrame(columns=['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    # df = df.append(pd.DataFrame([l], columns=df.columns))
    # print(df)

    # ##########         choose algorithm            ##############
    # 1)choose training data
    # data_choose = 0  # [0,1] 0 for default UCLA data, 1 for external d
    # if data_choose == 0:
    #     pass
    # else:
    #     pass

    # 2)get data description (optional)
    # description_choose = 0  # 0 for not showing, 1 for showing
    # if description_choose == 1:
    #     core.data_description()
    # else:
    #     pass

    # 3)choose algorithm
    # algs_choose = 0  # [0,1] 0 for default, 1 for developer's own algorithm

    # ##########       train system and get score                   ###############
    # if algs_choose == 0:
    #     pred = core.predict(df)
    #     print("Calculated Acceptance rate: ", ",".join([str(i) for i in pred]))
    #     decision = "High" if pred[0] > 0.80 else "Low"
    #     print(decision)
#
    s1, s2 = core.model_decision()
    return s1,s2
    # core.plot_data(test_y)
    # else:
    #     pass
def ret_score(args):
    return main(args)
if __name__ == "__main__":
   main(sys.argv[1:])
   # order：  Gre(out of 340) , Toefl(out of 120),  UniversityRating(0-5), SOP(out of 5), LOR(out of 5), CGPA(out of 10), Research(0/1)
