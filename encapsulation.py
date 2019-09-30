import core
import pandas as pd
core = core.Admission_Predictor()


# ##########        take in new input     ###############
l=[]
for i in range(7):
    print("INPUT YOUR " + str(i+1) + "th TERRIBLE DATA:")
    l.append(input())

#l = [337, 118, 4, 4.5, 4.5, 9.65, 1]  # l is supposed to be the input
df = pd.DataFrame(columns=['A', 'B', 'C', 'D', 'E', 'F', 'G'])
df = df.append(pd.DataFrame([l], columns=df.columns))
print(df)

# ##########         choose algorithm            ##############
# 1)choose training data
data_choose = 0  # [0,1] 0 for default UCLA data, 1 for external data
if data_choose == 0:
    pass
else:
    pass

# 2)get data description (optional)
description_choose = 1  # 0 for not showing, 1 for showing
if description_choose == 1:
    core.data_description()
else:
    pass

# 3)choose algorithm
algs_choose = 0  # [0,1] 0 for default, 1 for developer's own algorithm

# ##########       train system and get score                   ###############
if algs_choose == 0:
    pred = core.predict(df)
    print("Calculated Acceptance rate: " ,",".join([str(i) for i in pred]))
    decision = "High" if pred[0] > 0.80 else "Low"
    print(decision)

    train_X, test_X, train_y, test_y = core.model_decision()
    core.plot_data(test_y)
else:
    pass