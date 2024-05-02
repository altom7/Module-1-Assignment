import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generating data for website analytics
website_data = {
    'Date': pd.date_range(start='2024-01-01', end='2024-04-30'),
    'Page_Views': np.random.randint(1000, 5000, size=120),
    'Time_Spent_Minutes': np.random.uniform(1, 10, size=120),
    'Bounce_Rate': np.random.uniform(30, 60, size=120),
    'Conversion_Rate': np.random.uniform(0.5, 3, size=120),
    'CTR': np.random.uniform(1, 5, size=120)
}

print("Length of 'Date' array:", len(website_data['Date']))
print("Length of 'Page_Views' array:", len(website_data['Page_Views']))
print("Length of 'Time_Spent_Minutes' array:", len(website_data['Time_Spent_Minutes']))
print("Length of 'Bounce_Rate' array:", len(website_data['Bounce_Rate']))
print("Length of 'Conversion_Rate' array:", len(website_data['Conversion_Rate']))
print("Length of 'CTR' array:", len(website_data['CTR']))

website_df = pd.DataFrame(website_data)

# Print the first few rows of website_df to verify
print(website_df.head())

# Generating data for social media engagement
social_media_data = {
    'Date': pd.date_range(start='2024-01-01', end='2024-04-30'),
    'Likes': np.random.randint(100, 500, size=120),
    'Shares': np.random.randint(50, 200, size=120),
    'Comments': np.random.randint(20, 100, size=120),
    'Follower_Count': np.random.randint(5000, 10000, size=120),
    'Referral_Traffic': np.random.randint(200, 1000, size=120)
}

social_media_df = pd.DataFrame(social_media_data)

# Generating data for sales transactions
sales_data = {
    'Date': pd.date_range(start='2024-01-01', end='2024-04-30'),
    'Transactions': np.random.randint(50, 200, size=120),
    'Average_Order_Value': np.random.uniform(50, 200, size=120),
    'Customer_Lifetime_Value': np.random.uniform(1000, 5000, size=120),
    'Repeat_Purchase_Rate': np.random.uniform(0.1, 0.5, size=120)
}

sales_df = pd.DataFrame(sales_data)

# Merging the datasets on 'Date'
merged_df = pd.merge(website_df, social_media_df, on='Date')
merged_df = pd.merge(merged_df, sales_df, on='Date')

# Data Cleaning 


# Exploratory Data Analysis
# Summary Statistics
summary_stats = merged_df.describe()

# Plotting Summary Statistics
plt.figure(figsize=(10, 6))
sns.barplot(data=summary_stats.loc[['mean', 'std']], ci=None)
plt.title('Mean and Standard Deviation of Key Metrics')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.show()

# Correlation matrix
corr_matrix = merged_df.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

# Pairplot
sns.pairplot(merged_df[['Page_Views', 'Time_Spent_Minutes', 'Bounce_Rate', 'Conversion_Rate', 
                        'Likes', 'Shares', 'Comments', 'Follower_Count', 'Referral_Traffic', 
                        'Transactions', 'Average_Order_Value', 'Customer_Lifetime_Value', 
                        'Repeat_Purchase_Rate']])
plt.show()
