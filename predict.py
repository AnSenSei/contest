import numpy as np
import pandas as pd

data = pd.read_csv("STATS .csv")
print(data.shape)
column_names = ["won-lost percent", "rank0", "offense", "rank1", "assist", "rank2", "field-goal", "rank3", "dffense",
                "rank4", "team_score"]
df = pd.DataFrame(np.zeros((64, 11)), columns=column_names, dtype=float)
row_index = 0
print(df.shape)
print(df.iloc[row_index][0])


def get_data(team):
    for index, row in data.iterrows():
        if row[1] == team:
            print("the rank and value for won-lost perenct to " + team + " is: " + row[0] + " " + row[4])
            df["won-lost percent"][row_index] = row[4]
            df["rank0"] = row[0]

        if row[7] == team:
            print("the rank and value for offense to " + team + " is " + row[6] + " " + row[10])
            df["offense"][row_index] = row[10]
            df["rank1"] = row[6]
        if row[14] == team:
            print("the rank and value for assist to " + team + " is " + row[13] + " " + row[17])
            df["assist"][row_index] = row[17]
            df["rank2"] = row[13]
        if row[21] == team:
            print("the rank and value for field-goal to " + team + " is " + row[20] + " " + row[24])
            df["field-goal"][row_index] = row[24]
            df["rank3"] = row[20]
        if row[28] == team:
            print("the rank and value for dffense to " + team + " is " + row[27] + " " + row[31])
            df["dffense"][row_index] = row[31]
            df["rank4"] = row[27]
    print(df.iloc[row_index])


team_names = ["Gonzaga", "Norfolk St.", "Oklahoma", "Missouri", "Creighton", "UC Santa Barbara", "Virginia",
              "Ohio", "Southern California", "Drake", "Kansas", "Eastern Wash.",
              "Oregon", "VCU", "lowa", "Grand Canyon", "Baylor", "Hartford", "UNC Asheville", "Wisconsin", "Villanova",
              "Winthrop", "Purdue", "North Texas", "Texas Tech", "Utah St.",
              "Arkansas", "Colgate", "Florida", "Virginia Tech", "Ohio St.", "Oral Roberts"]
team_names2 = ["Michigan", "Texas Southern", "LSU", "Stony Brook", "Colorado", "Georgetown", "Florida St.",
               "UNC Greensboro", "BYU", "UCLA", "Texas", "Abilene Christian", "UConn", "Maryland",
               "Alabama", "Iona", "Illinois", "Drexel", "Loyola Chicago", "Georgia Tech", "Tennessee", "Oregon St.",
               "Oklahoma", "Liberty", "San Diego St.", "Syracuse", "West Virginia",
               "Morehead St.", "Clemson", "Rutgers", "Houston", "Cleveland St."]
for team in team_names:
    get_data(team)
    row_index += 1

for team in team_names2:
    get_data(team)
    row_index += 1

print(df)

row_index1=0
for index, row in df.iterrows():
    df["team_score"][row_index1] = (float(row[0]) / 10 * 0.6) + (float(row[2]) / 10 * 0.3) + (float(row[4]) / 5 * 0.15) + (float(row[6]) / 5 * 0.15) - (float(row[
            8]) / 4 * 0.2)

    row_index1+=1

for index,row in df.iterrows():
    if(index<32):
        print(team_names[index])
    else:
        print(team_names2[index-32])
    print(row["team_score"])