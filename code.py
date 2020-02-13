# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns = {'Total' : 'Total_Medals'}, inplace = True)

print (data.head(10))


# --------------
#Code starts here





data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'],'Summer',np.where(data['Total_Summer'] == data['Total_Winter'], 'Both', 'Winter'))
better_event = data['Better_Event'].value_counts().idxmax()

print (better_event)


# --------------
#Code starts here

top_countries = data [['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries = top_countries.drop(top_countries.index[-1])

def top_ten(df,col) :
    country_list = []
    ten = df.nlargest(10,col)
    country_list = list(ten['Country_Name'])
    return country_list

top_10_summer = top_ten (top_countries,'Total_Summer')
top_10_winter = top_ten (top_countries,'Total_Winter')
top_10 = top_ten (top_countries,'Total_Medals')
print (top_10)
print (top_10_summer)
print (top_10_winter)

common = list ([i for i in top_10_summer if i in (top_10 and top_10_winter)])
print (common)




# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
#print (summer_df)
summer_df.plot.bar(x= 'Country_Name',y = 'Total_Summer')
winter_df.plot.bar(x= 'Country_Name',y = 'Total_Winter')
top_df.plot.bar(x= 'Country_Name',y = 'Total_Medals')
#inter_df[['Country_Name','Total_Winter']].plot(kind = 'bar')
#top_df[['Country_Name','Total_Medals']].plot(kind = 'bar')

plt.show()


# --------------
#Code starts here

summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax()]['Country_Name']
print (summer_country_gold,summer_max_ratio)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax()]['Country_Name']
print (winter_country_gold,winter_max_ratio)

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax()]['Country_Name']
print (top_country_gold,top_max_ratio)


# --------------
#Code starts here

data_1 = data[:-1]

data_1['Total_Points'] = data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']

most_points = data_1['Total_Points'].max()
best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']

print (best_country,most_points)


# --------------
#Code starts here

best = data.loc[data['Country_Name']==best_country,:]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked = True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation = 45)
plt.show()


