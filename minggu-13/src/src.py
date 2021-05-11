import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Name": ["Braund, Mr. Owen Harris",
        "Allen, Mr. William Henry",
        "Bonnell, Miss. Elizabeth"],
    "Age": [22, 35, 58],
    "Sex": ["male", "male", "female"]}
)
print(df)

print(df["Age"])
print(df["Age"].max())
print(df.describe())

print('')
print('')

titanic = pd.read_csv("workshop/titanic.csv")
print(titanic)
print('')
print(titanic.head(8))
print('')
print(titanic.dtypes)
print('')
# save to file
# titanic.to_excel('titanic.xlsx', sheet_name='passengers', index=False)
print(titanic.info())

print('')
print('###############################')

print(titanic.head())
ages = titanic["Age"]
print('')
print(ages.head())
print('')
age_sex = titanic[["Age", "Sex"]]
print(age_sex.head())
print('')
above_35 = titanic[titanic["Age"] > 35]
print(above_35.head())
print('')
class_23 = titanic[titanic["Pclass"].isin([2, 3])]
print(class_23.head())
print('')
class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
print(class_23.head())
print('')
age_no_na = titanic[titanic["Age"].notna()]
print(age_no_na.head())
print('')
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
print(adult_names.head())
print('')
print(titanic.iloc[9:25, 2:5])
titanic.iloc[0:3, 3] = "anonymous"
print(titanic.head())

print('')
print('###############################') 
print('')

air_quality = pd.read_csv("workshop/air_quality_no2.csv",
    index_col=0, parse_dates=True)
print(air_quality.head())
#air_quality.plot()
#air_quality["station_paris"].plot()
# air_quality.plot.scatter(x="station_london", y="station_paris",alpha=0.5)


plt.show()