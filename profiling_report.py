import pandas as pd
from ydata_profiling import ProfileReport

data = pd.read_csv("melb_data.csv")
data = data.drop(['Suburb', 'Address', 'SellerG', 'Date'], axis=1)
data = data.drop(['BuildingArea', 'YearBuilt'], axis=1)
profile = ProfileReport(data, title='Testando o Profile Report')

profile.to_file("test_profile_report3.html")
