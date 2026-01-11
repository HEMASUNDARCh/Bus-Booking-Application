import pandas as pd
data={"Name":["King","payal","sunny","pinky","samm","kajal"],
      "Age":[25,30,35,31,27,37],
      "Gender":["male","female","male","feamle","male","female"],
      "Salary":[20000,None,35000,None,40000,None],
      "Joining date":[2,15,27,4,25,7]}
df=pd.DataFrame(data)
print(df)