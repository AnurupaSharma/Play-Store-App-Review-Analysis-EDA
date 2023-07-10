# -*- coding: utf-8 -*-
"""Play Store App Review Analysis / EDA Capstone Project .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vx8Q-8M_ZiW21hOhvfzZRvs4pazvScAe

# **Project Name -** Play Store App Review Analysis/EDA

##### **Project Type**    - EDA
##### **Contribution**    - Individual

# **Project Summary -**

This is an EDA project in this project I will have to visualize the dataset using EDA. The dataset is about Play Store App Review which has 10841 rows and 13 columns like App represent name of the app , category represent category of the app, Rating represent app's rating by user out of 5, size represent the size of the app , Installs represent number of Installs of the app , Type represent weather the app is free or paid, Price represent the app in $ , content rating represent the target audience of the app, Genres represent the genre of app, Last Updated represent date the app updated last time, Current ver represent current version of app , Android Ver represent android version required to run the app. Play Store is one of the largest and most popular android app stores with over a million apps. My task is to import all the python libraries after that I will have to read and understand the data and observe the data by exploring few rows, checking shape, columns, data types etc after that I will clean and transform the data to make data efficient for analysis and visualisation and then visualise data withe the help of graphs and plots to learn trends , patterns and get answers to the question related to the data.

# **Problem Statement**

Our main objective is to analyze the dataset and find out which features contribute to app success and how these features affect the user engagement with the app.

# ***Let's Begin !***

## ***1. Know Your Data***

## Import Libraries
"""

# Commented out IPython magic to ensure Python compatibility.
# Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

"""## Dataset Loading"""

# Load Dataset
from google.colab import drive
drive.mount('/content/drive')

play_store_data = pd.read_csv("/content/drive/MyDrive/Play Store Data.csv")

"""## Dataset First View"""

# Dataset First Look
play_store_data.head()

"""## Dataset Rows & Columns count"""

# Dataset Rows & Columns count
play_store_data.shape

"""## Dataset Information"""

# Dataset Info
play_store_data.info()

"""## Duplicate Values"""

# Dataset Duplicate Value Count
play_store_data[play_store_data.duplicated()].shape

"""## Missing Values/Null Values"""

# Missing Values/Null Values Count
play_store_data.isnull().sum()

"""## What did you know about your dataset?

The dataset contain 10841 apps and 13 features.

The play_store_data.info() function showed us that some of the columns like 'Rating' have missing values and some have incorrect data types associated with them.

The dataset contain some duplicated value as well.

## ***2. Understanding Your Variables***
"""

# Dataset Columns
play_store_data.columns

# Dataset Describe
play_store_data.describe()

"""## Check Unique Values for each variable."""

# Check Unique Values for each variable.
play_store_data['App'].value_counts()

play_store_data['Category'].value_counts()

play_store_data['Rating'].value_counts()

play_store_data['Reviews'].value_counts()

play_store_data['Size'].value_counts()

play_store_data['Installs'].value_counts()

play_store_data['Price'].value_counts()

play_store_data['Type'].value_counts()

play_store_data['Content Rating'].value_counts()

play_store_data['Genres'].value_counts()

play_store_data['Last Updated'].value_counts()

play_store_data['Current Ver'].value_counts()

play_store_data['Android Ver'].value_counts()

"""## 3. ***Data Wrangling***

## Data Wrangling Code

## Handling Missing Value
"""

# dropping NAN values in Rating columns
play_store_data = play_store_data[~(play_store_data['Rating'].isnull())]

# dropping NAN values less than 10
play_store_data.dropna(inplace=True)

"""## Change The Variable To The Correct Types"""

# Price Column
play_store_data['Price'] = play_store_data['Price'].apply(lambda x:0 if x=="0" else float(x[1:]))

# Installs column
play_store_data['Installs'] = play_store_data['Installs'].apply(lambda x:int(x.replace(",","").replace("+","")))

# Reviews column
play_store_data['Reviews'] = play_store_data['Reviews'].astype('int')

# Last updated column
play_store_data['Last Updated'] = pd.to_datetime(play_store_data['Last Updated'])

# creating new column
play_store_data['Updated Month'] = pd.to_datetime(play_store_data['Last Updated']).dt.month

# updated month
play_store_data['Updated Month'] = pd.to_datetime(play_store_data['Updated Month'])

# dropping duplicates
play_store_data.drop_duplicates(inplace=True)

# reset index
play_store_data.reset_index(drop=True,inplace=True)

"""## What all manipulations have you done and insights you found?

The 'Price' column had an additional ‘$’ sign for every paid app that was visible clearly once we used the value_counts() function. This resulted in the column being treated as an object instead of a float-type value.

In 'Installs' column the values contain both the ‘,’ and ‘+’ symbols, which led to this misrepresentation as an object type.

'Reviews' column had No issues and was convert it into an int type.

The 'Last Updated' column has the data type as an object, I converted it to datetime format and created a new column 'Updated Month' for analysis.

I use drop_duplicates function to drop the duplicate values and reset the index using reset_index function.

## ***4. Data Vizualization, Storytelling & Experimenting with charts : Understand the relationships between variables***

## Chart - 1

Outliers Analysis with Box Plot
"""

# Chart - 1 visualization code
plt.boxplot(play_store_data['Price'])
plt.title('Price Box Plot')
plt.xlabel('Price')
plt.show()

# checking out the records with more than 30 dollar price
play_store_data[play_store_data['Price']>30]

# drop records having more than 30 dollar price
play_store_data = play_store_data[play_store_data['Price']<30]

"""### 1. Why did you pick the specific chart?

I used boxplot to check for outliers in the 'Price' column because box plot type plots are used to easily detect outliers.

### 2. What is/are the insight(s) found from the chart?

There are outliers in the 'Price' column. So, I removed the price greater than 30.

### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

Removing outliers in the 'Price' column can help ensure that the majority of your app's pricing falls within a reasonable range.

## Chart - 2
"""

# Chart - 2 visualization code
plt.boxplot(play_store_data['Reviews'])
plt.title("Reviews Box Plot")
plt.xlabel('Reviews')
plt.show()

# checking out the records with more than 10 million reviews
play_store_data[play_store_data['Reviews']>10000000]

# drop records having more than 1M reviews
play_store_data = play_store_data[play_store_data['Reviews']<=1000000]

"""### 1. Why did you pick the specific chart?

I used boxplots to check for outliers in the 'Review' column because box plot type plots are used to easily detect outliers.

### 2. What is/are the insight(s) found from the chart?

I found these are those super popular apps. Of course these are all real apps but right now I'm worried about which app might be promising, studying these apps won't be very useful. So the best option is to delete these records.

### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

By removing records that contain super popular apps,we can shift your attention towards identifying and analyzing apps that have the potential to become promising in the future. This approach allows us to explore and understand other apps in dataset that may have gone unnoticed or received less attention, providing an opportunity to discover new trends or hidden gems.

## Chart - 3
"""

# Chart - 3 visualization code
sns.distplot(play_store_data['Rating'],bins=20)
plt.title('Distribution of app rating')
plt.show()

"""### 1. Why did you pick the specific chart?

I used dist plot to represents the overall distribution of continuous data variables because distplot depicts the variation in the data distribution.

### 2. What is/are the insight(s) found from the chart?

Analysed the ratings using the dist plot, I saw that they are skewed towards higher ratings.

### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

The observation of a dist plot showing a skewed distribution towards higher ratings can provide valuable insights for a business. It suggests positive customer satisfaction, contributes to brand reputation, and can attract new customers.

## Chart - 4
"""

# Adults only 18+ and Unrated are not useful because very less in number so dropping these records
play_store_data = play_store_data[~play_store_data['Content Rating'].isin(['Adults only 18+','Unrated'])]

# Chart - 4 visualization code
content_rating_show = play_store_data['Content Rating'].value_counts()
content_rating_show

plt.pie(content_rating_show.values,labels=content_rating_show.index,autopct='%.2f%%')
plt.title("Content Rating Pie Chart")
plt.show()

"""### 1. Why did you pick the specific chart?

I used pie chart to show percentages of a whole and a parts-to-whole relationship for 'Content Rating' column.

### 2. What is/are the insight(s) found from the chart?

The insights gained from the pie chart can inform the Most of the apps belong to the Everyone category.

### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

The content rating distribution helps the client align their app offerings with the preferences and needs of different age groups.

## Chart - 5
"""

# Chart - 5 visualization code
genres_show = play_store_data['Genres'].value_counts().head(10)
genres_show

#Top 10 Genres
plt.barh(y=genres_show.index,width=genres_show.values,data=play_store_data,color='maroon')
plt.title("Top 10 Genres")
plt.xlabel('count of genres')
plt.ylabel('genre')
plt.show()

"""### 1. Why did you pick the specific chart?

I used a horizontal bar to compare different values ​​in the 'genre' column.

### 2. What is/are the insight(s) found from the chart?

Tools, Entertainment, Education genre apps are the top 3 genre apps people use.

### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

Knowing that Tools, Entertainment, and Education are the top genres of apps used by people allows the client to strategically focus their efforts and resources on developing and improving apps within these genres.

## Chart - 6
"""

# Chart - 6 visualization code
plt.scatter(play_store_data['Price'],play_store_data['Rating'],color='green')
plt.title('Price vs Rating')
plt.xlabel('Price')
plt.ylabel('Rating')
plt.show()

"""### 1. Why did you pick the specific chart?

I used a scatter plot to visualize the relationship between the 'Price' and 'rating' columns.

### 2. What is/are the insight(s) found from the chart?

It seems price above  $15 there is no lower rating.

### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

The gained insight regarding the absence of lower ratings for apps priced above $15 can potentially create a positive business impact. It suggests that higher-priced apps tend to have higher ratings, indicating that users may perceive these apps as having higher quality, value, or features.

## Chart - 7
"""

# Chart - 7 visualization code
sns.barplot(data=play_store_data,x='Content Rating',y='Price')
plt.show()

"""### 1. Why did you pick the specific chart?

I used bar chart in the 'Content Rating' and 'Price' columns to visualize trends and comparisons.

### 2. What is/are the insight(s) found from the chart?

Received information about the number of apps with a content rating 'Everyone above 10+' who pays more for apps.

### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

This insight can be leveraged by the client to develop and promote high-quality, premium apps targeting users who are willing to invest in a safe and family-friendly app experience.

## Chart - 8
"""

# Chart - 8 visualization code
sns.scatterplot(data=play_store_data,x='Price',y='Installs',hue='Content Rating')
plt.title("Price and Age wise Installs")
plt.show()

"""### 1. Why did you pick the specific chart?

I used Scatter Plot to find out the relationship between 'Price'and 'Installs' by age .

### 2. What is/are the insight(s) found from the chart?

It seems that offering apps for free or at a lower price point can lead to a higher number of installs, indicating a potential larger user base.

### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

While offering apps for free or at lower prices can increase the number of installs, there is a potential negative growth factor to consider. When the price of an app increases, the number of installs decreases. This suggests that users may be more hesitant to download or purchase apps at higher price points.

## Chart - 9
"""

# Chart - 9 visualization code
sns.boxplot(data=play_store_data,x='Content Rating',y='Rating')
plt.title('Age wise Rating')
plt.show()

"""### 1. Why did you pick the specific chart?

I used Box plot to get a quick visual summary of the variability of rating by age .

### 2. What is/are the insight(s) found from the chart?

That “Everyone” category has the highest number of ratings in the lower percentiles as compared to the other categories.And The median values are all comparable.

### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

The gained insights regarding the variability of ratings by age, as observed through the box plot, can potentially create a positive business impact. Understanding that the "Everyone" category has a higher number of ratings in the lower percentiles suggests that there is a larger user base within this category, indicating a broader market reach.

## Chart - 10
"""

# Chart - 10 visualization code
sns.boxplot(data=play_store_data,x='Type',y='Rating')
plt.title("Type wise Rating")
plt.show()

"""### 1. Why did you pick the specific chart?

I used box plots to get a quick visual summary of the variability of ratings by type in the dataset.

### 2. What is/are the insight(s) found from the chart?

Box plot shows that the median rating for paid apps is slightly higher than that of free apps.

### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

The higher median rating for paid apps indicates that users who are willing to pay are generally satisfied with the app's performance. This finding can be beneficial for revenue generation. Positive ratings can attract more users to purchase the paid app, leading to increased downloads and revenue.

## Chart - 11
"""

# Chart - 11 visualization code
play_store_data.groupby(['Updated Month'])['Rating'].mean().plot()
plt.title("Month Wise Rating")
plt.show()

"""### 1. Why did you pick the specific chart?

I used line plot to track changes in the 'Rating' column over time.

### 2. What is/are the insight(s) found from the chart?

Observed that there are high ratings during mid-month periods.

### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

If the high ratings occur consistently during mid-month periods, it suggests the presence of seasonal patterns or specific events that positively influence user ratings. Gained insights from the line plot can help businesses identify these patterns and leverage them to create targeted marketing campaigns or promotions during those periods

## Chart - 12
"""

# Chart - 12 visualization code
sns.scatterplot(data=play_store_data,x='Rating',y='Installs',hue='Type')
plt.title("Type Wise Rating and Installs")
plt.show()

"""### 1. Why did you pick the specific chart?

I used Scatter Plot to visualize the relationship between 'Rating' and 'Installs' variables.

### 2. What is/are the insight(s) found from the chart?

High-rated free apps have low installs.

### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

High-rated free apps have low installs, it suggests that there might be a mismatch between the user experience and the value proposition of the app.

## Chart - 13
"""

# Chart - 13 visualization code
play_store_data.groupby(['Updated Month'])['Installs'].mean().plot()
plt.title("Month Wise Installs")
plt.show()

"""### 1. Why did you pick the specific chart?

I used line plot to track changes in the 'Installs' column over time.

### 2. What is/are the insight(s) found from the chart?

The high installs during the mid month could indicate a seasonal trend or event that drives increased demand for the apps.

### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

Increased installs during the mid month can translate into higher revenue potential.

## Chart - 14 - Correlation Heatmap
"""

# Correlation Heatmap visualization code
corr_df = play_store_data.corr()

sns.heatmap(corr_df,annot=True)
plt.title('Correlation Heatmap')
plt.show()

"""### 1. Why did you pick the specific chart?

I used correlation heatmap to displays the correlation between multiple variables.

### 2. What is/are the insight(s) found from the chart?

Using a correlation heatmap, visualize multiple correlation and draw several inferences, for example, reviews and price being inversely related (-0.073) and so on.

### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

Reviews and price being inversely related: This insight implies that as the price of a product increases, the number of reviews tends to decrease. From a business perspective, this could indicate that higher-priced products may have a smaller customer base or face higher barriers to adoption.

## Chart - 15 - Pair Plot
"""

# Pair Plot visualization code
sns.pairplot(play_store_data)
plt.title('Pair Plot')
plt.show()

"""### 1. Why did you pick the specific chart?

I used pair plot because it allows us to plot pairwise relationships between variables.

### 2. What is/are the insight(s) found from the chart?

Using a pair-plot, visualize multiple scatter plots and draw several inferences, for example, price and rating having very weak trend, reviews and price being inversely related and so on.

### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

Price and rating having a very weak trend: This insight may suggest that price does not strongly influence the rating of a product. In terms of business impact, this could mean that setting higher prices does not necessarily result in higher ratings.

## **5. Solution to Business Objective**

Target the Everyone category: Since most of the apps belong to the Everyone category, it indicates a larger potential user base. The client can focus on developing and promoting apps that cater to this category, ensuring they meet the requirements and interests of a wide range of users.

Emphasize popular genres: Tools, Entertainment, and Education are the top three genres that people use. The client can consider developing apps in these genres to align with user preferences and increase the likelihood of app adoption.

Optimize pricing strategy: Removing outliers in the Price column and focusing on apps below $30 suggests that the client should consider a pricing strategy that keeps the prices within a reasonable range. Offering apps for free or at lower price points can lead to a higher number of installs and potentially attract a larger user base.

Enhance user experience: With the ratings skewed towards higher ratings, it indicates that users generally have a positive perception of the apps. However, it's essential to ensure that the apps meet or exceed user expectations to maintain positive reviews and encourage app engagement. Continuously improving the user experience, addressing user feedback, and providing regular updates can contribute to positive business growth.

Consider mid-month promotions: The observation of high ratings and increased installs during mid-month periods suggests a potential seasonal trend or event that drives increased demand. The client can leverage this insight by planning targeted promotions, special offers, or updates during these periods to further boost app downloads and user engagement.

Utilize correlation insights: The correlation heatmap and pair-plot analysis provide valuable insights into the relationships between variables. For example, the inverse relationship between reviews and price suggests that higher-priced apps may receive fewer reviews. The client can consider adjusting pricing strategies to encourage more reviews and feedback, which can positively impact app visibility and user trust.

Monitor and analyze content rating preferences: Understanding the preferences of users who pay more for apps in the 'Everyone above 10+' category can provide insights into their specific needs and expectations. This information can guide the client in developing targeted marketing campaigns, optimizing app features, or exploring potential opportunities for monetization within this user segment.

# **Conclusion**

The majority of apps in the dataset belong to the Everyone category, indicating a larger potential user base.

Tools, Entertainment, and Education are the top three genres that people use.

Removing outliers and focusing on apps priced below $30 suggests that the client should consider a pricing strategy that keeps prices within a reasonable range.

The ratings distribution is skewed towards higher ratings, indicating that users generally have a positive perception of the apps.

The observation of high ratings and increased installs during mid-month periods suggests a potential seasonal trend or event that drives increased demand.

### ***Hurrah! You have successfully completed your EDA Capstone Project !!!***
"""