
import pandas as pd
#load nyc weather data
df = pd.read_csv('dataset/nyc_weather.csv')
#display first 5 rows
# print(data.head())
#access specific column with first row
# print(data['EST'].iloc[0])
#access the specific column with all rows
# print(data['EST'])
#accessing first row of the first column
# print(data.iloc[0,0])
#accessing all rows of the first column
# print(data.iloc[:,0])
# accessing whole columns using dataframe attribute style   
# print(df[['EST', 'Temperature', 'WindDirDegrees']])           
#get the max value of temperature
# print(df['Temperature'].max())

#get the dates on which it rained
# print(df['EST'][df['Events'] == 'Rain'])
#increase the temperature by 10 degrees and store in a new column pavan 
# df['Pavan'] = df['Temperature'] + 10    
# print(df)

#get the mean of the windspeed  
# print(df['WindSpeedMPH'].mean())

df.fillna(0, inplace=True)  # Fill NaN values with 0
print(df['WindSpeedMPH'].mean())  # Recalculate mean after filling NaN
