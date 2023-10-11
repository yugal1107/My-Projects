import matplotlib.pyplot as plt
import pandas as pd

#Reading csv files
data = pd.read_csv("CSE data.csv")
col = data.columns
sub = []      
mean = []
for i in range(1,6):
    sub.append(col[i])
    mean.append(data[col[i]].mean())

# Data for the bar chart
categories = sub
values = mean  # Represents the values for each category

# Create the bar chart
plt.bar(categories, values)

#Writing text on bar chart 
for i in range(0,5):
    rounded = round(mean[i],3)
    plt.text(i,mean[i],str(rounded))

# Add labels and title
plt.xlabel('Subjects')
plt.ylabel('Average Marks of all students in each subject')
plt.title('Result of CSE 2nd Sem')

#Rotating to prevent overlapping
plt.xticks(rotation=5)

# Display the chart
plt.show()
