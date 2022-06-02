
"""
Dünyada ki insanların mutluluk durumlarını ölçmek dünya mutluluk raporunun önemli bir çalışmasıdır.
Alanında uzman ve söz sahibi insanlar refah ölçümleri ile ulusların ilerlemesini değerlendirmek ve bu raporları nasıl etkili bir şekilde kullanılabileceğini
açıklamaktadır.Raporlar bugün bizlere mutluluk biliminin kişisel ve ulusal varyosyanlarını nasıl açıkladığını gösteriyor.

*Life Ladder:* Alt kısımda 0'dan üstte 10'a kadar numaralandırılmış basamaklara sahip bir merdiven düşünün.
Merdivenin üst kısmı sizin için mümkün olan en iyi hayatı temsil eder ve merdivenin alt kısmı sizin için mümkün olan en kötü hayatı temsil eder.

# Veri Yükleme, Tanıma ve Temizleme
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sbn
sbn.set_palette("RdYlGn_r")#matplotlib renk döngüsü->set_palette

world_happiness_report = pd.read_csv("world-happiness-report.csv")

world_happiness_report.head(-5)

world_happiness_report.info()

world_happiness_report.describe()

world_happiness_report.isnull().sum()

world_happiness_report = world_happiness_report.dropna()

world_happiness_report.describe()

"""# Verinin Korelasyonunu Alma"""

world_happiness_report.corr()

world_happiness_report.corr()["Healthy life expectancy at birth"].sort_values()

kolerasyon = world_happiness_report[['Life Ladder', 'Log GDP per capita','Social support', 'Healthy life expectancy at birth',
       'Freedom to make life choices', 'Generosity',
       'Perceptions of corruption']]

plt.figure(figsize=(20, 8))
sbn.heatmap(kolerasyon.corr(),annot = True,  cmap='RdYlGn_r', mask=np.triu(np.ones_like(kolerasyon.corr())));
plt.title('Correlations between factors', fontsize=20, fontweight='bold', pad=20);

"""# Verilerin Görserller ile karşılaştırılması

"""

plt.figure(figsize=(12, 6))
sbn.regplot(x='Life Ladder', y='Generosity', data=world_happiness_report);
plt.title('Correlation between Life Ladder and Generosity', fontsize=20, fontweight='bold', pad=20);

"""Yolsuzluk algısı ve merdiven puanının zayıf bir şekilde ilişkili olduğunu görebiliriz. Çoğu veri noktası yüksek yolsuzluk algısına sahiptir."""

plt.figure(figsize=(12, 6))
sbn.regplot(x='Life Ladder', y='Log GDP per capita', data=world_happiness_report);
plt.title('Correlation between Life Ladder and Log GDP per capita', fontsize=20, fontweight='bold', pad=20);

plt.figure(figsize=(12, 6))
sbn.regplot(x='Healthy life expectancy at birth', y='Log GDP per capita', data=world_happiness_report, ci=None);
plt.title('Correlation between Healthy life expectancy at birth and Log GDP per capita', fontsize=20, fontweight='bold', pad=20);

world_happiness_report_2021 = pd.read_csv('world-happiness-report-2021.csv')
world_happiness_report_2021.head(20)

world_happiness_report_2021.describe()

plt.figure(figsize=(35,10))
sbn.barplot(data=world_happiness_report_2021,x="Country name",y="Ladder score")
plt.xticks(rotation=90) 
plt.show()

plt.figure(figsize=(35,10))
sbn.barplot(data=world_happiness_report_2021.head(8),x="Country name",y="Ladder score")
plt.xticks(rotation=90) 
plt.show()

fig, ax = plt.subplots(figsize=(10,10))
sbn.boxplot(y="Regional indicator", x="Ladder score", data=world_happiness_report_2021, orient="h", ax=ax)

plt.figure(figsize = (16,8))
plt.xticks(rotation=90)
sbn.lineplot(x="Country name", y = "Ladder score", data = world_happiness_report_2021[world_happiness_report_2021['Regional indicator']== 'Southeast Asia'],marker='o',label='Southeast_Asia')
sbn.lineplot(x="Country name", y = "Ladder score", data = world_happiness_report_2021[world_happiness_report_2021['Regional indicator']== 'South Asia'],marker='o',label='South_Asia')
sbn.lineplot(x="Country name", y = "Ladder score", data = world_happiness_report_2021[world_happiness_report_2021['Regional indicator']== 'East Asia'],marker='o',label='East_Asia',color='b')
sbn.lineplot(x="Country name", y = "Ladder score", data = world_happiness_report_2021[world_happiness_report_2021['Regional indicator']== 'North America and ANZ'],marker='o',label='North America and ANZ',color='g')
sbn.lineplot(x="Country name", y = "Ladder score", data = world_happiness_report_2021[world_happiness_report_2021['Regional indicator']== 'Commonwealth of Independent States'],marker='o',label='Commonwealth of Independent States',color='y')
plt.grid(color='r', linestyle='-', linewidth=2)
plt.show()

plt.figure(figsize = (16,8))
plt.xticks(rotation=90)
sbn.lineplot(x="Country name", y = "Ladder score", data = world_happiness_report_2021[world_happiness_report_2021['Regional indicator']== 'Central and Eastern Europe'],marker='o',label='Central and Eastern Europe')
sbn.lineplot(x="Country name", y = "Ladder score", data = world_happiness_report_2021[world_happiness_report_2021['Regional indicator']== 'Latin America and Caribbean'],marker='o',label='Latin America and Caribbean',color='r')
sbn.lineplot(x="Country name", y = "Ladder score", data = world_happiness_report_2021[world_happiness_report_2021['Regional indicator']== 'Sub-Saharan Africa'],marker='o',label='Sub-Saharan Africa',color='y')
sbn.lineplot(x="Country name", y = "Ladder score", data = world_happiness_report_2021[world_happiness_report_2021['Regional indicator']== 'Western Europer'],marker='o',label='Western Europe')
sbn.lineplot(x="Country name", y = "Ladder score", data = world_happiness_report_2021[world_happiness_report_2021['Regional indicator']== 'Middle East and North Africa'],marker='o',label='Middle East and North Africa',color='b')
plt.grid( linestyle='-', linewidth=2)
plt.show()



Germany_1 = world_happiness_report_2021[world_happiness_report_2021['Country name'] == 'Germany'].reset_index(drop=True) 
Germany_1 = Germany_1.drop(['Regional indicator','Ladder score',"Standard error of ladder score","upperwhisker","lowerwhisker",
            "Logged GDP per capita","Healthy life expectancy","Ladder score in Dystopia","Explained by: Log GDP per capita","Explained by: Social support"
            ,"Explained by: Healthy life expectancy","Explained by: Freedom to make life choices","Explained by: Generosity",
            "Explained by: Perceptions of corruption","Dystopia + residual"
            ], axis = 1)
Germany_1 = Germany_1.fillna(0,inplace=True)

Germany_2 = world_happiness_report[world_happiness_report['Country name'] == 'Germany']
Germany_2

Germany = pd.concat([Germany_1, Germany_2])
Germany.reset_index(drop=True, inplace=True)
Germany.rename(columns = {'year':'Year'}, inplace=True)
Germany

plt.figure(figsize=(18, 6))
sbn.lineplot(x='Year', y='Life Ladder', data=Germany, marker='o', markersize=10);
sbn.set_style('whitegrid')
sbn.despine(left=True)
plt.title('Germany\'s ladder score over the years', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Years Of Germany')
plt.show()

plt.figure(figsize=(18, 6))
sbn.lineplot(x='Year', y='Log GDP per capita', data=Germany, marker='o', markersize=10);
sbn.set_style('whitegrid')
sbn.despine(left=True)
plt.title('Germany\'s Log GDP per capita over the years', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('years')
plt.show()

plt.figure(figsize=(18, 6))
sbn.lineplot(x='Year', y='Social support', data=Germany, marker='o', markersize=10);
sbn.set_style('whitegrid')
sbn.despine(left=True)
plt.title('Germany\'s Social support over the years', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Year')
plt.show()

plt.figure(figsize=(18, 6))
sbn.lineplot(x='Year', y='Healthy life expectancy at birth', data=Germany, marker='o', markersize=10);
sbn.set_style('whitegrid')
sbn.despine(left=True)
plt.title('Germany\'s Healthy life expectancy at birth over the years', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Year')
plt.show()

