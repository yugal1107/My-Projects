import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("ITIOT Data.csv")
# print(data.shape)
col = data.columns
#marks_to_disp = []
occ_all = []
x_values = []

for i in range(0,21):
    x_values.append(i)

#Plotting Line Graph 

#Counting marks from data and plotting them 
for i in range(2,7):
    occ_sub = []
    #Loop for counting
    for j in range (0,21):
        occurence_i = data[col[i]].value_counts().get(j,0)
        occ_sub.append(occurence_i)
    plt.plot(x_values , occ_sub , label = col[i])
    #plt.fill_between(x_values , occ_sub)
#   occ_all.append(occ_sub)

plt.xlabel("Marks of Students")
plt.ylabel("No of Students scoring x marks")
plt.title("Marks Data Analysis")

xtick = []
ytick = []

for i in range(0,25,2):
    xtick.append(i)
    ytick.append(i)

plt.xticks(xtick)
plt.yticks(ytick)

plt.grid()
plt.legend()
plt.show()

# print (occ_all)
# print (col)

