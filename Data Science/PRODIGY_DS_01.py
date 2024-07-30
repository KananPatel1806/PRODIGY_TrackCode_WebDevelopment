import matplotlib.pyplot as plt

# Example data
genders = ['Male', 'Female', 'Non-Binary', 'Prefer not to say']
counts = [450, 500, 75, 25]  # Example counts corresponding to each gender

# Plotting the bar chart
plt.figure(figsize=(8, 6))
plt.bar(genders, counts, color='skyblue')
plt.xlabel('Genders')
plt.ylabel('Counts')
plt.title('Distribution of Genders')
plt.show()
import seaborn as sns
import matplotlib.pyplot as plt

# Example data
genders = ['Male', 'Female', 'Non-Binary', 'Prefer not to say']
counts = [450, 500, 75, 25]  # Example counts corresponding to each gender

# Creating a bar plot using Seaborn
plt.figure(figsize=(8, 6))
sns.barplot(x=genders, y=counts, palette='pastel')
plt.xlabel('Genders')
plt.ylabel('Counts')
plt.title('Distribution of Genders')
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Example data
np.random.seed(0)
ages = np.random.randint(18, 70, size=100)  # Example ages

# Plotting the histogram
plt.figure(figsize=(8, 6))
plt.hist(ages, bins=10, edgecolor='black', alpha=0.7)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Ages')
plt.grid(True)
plt.show()
import seaborn as sns
import matplotlib.pyplot as plt

# Example data
np.random.seed(0)
ages = np.random.randint(18, 70, size=100)  # Example ages

# Creating a histogram using Seaborn
plt.figure(figsize=(8, 6))
sns.histplot(ages, bins=10, kde=False, color='skyblue')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Ages')
plt.grid(True)
plt.show()
