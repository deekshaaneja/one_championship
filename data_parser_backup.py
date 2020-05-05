import pandas as pd
import os

FILEPATH = os.path.join(os.getcwd(),"data.csv")


dataframe = pd.DataFrame(pd.read_csv(FILEPATH, sep = ",", header = 0))
dataframe['Floor Access DateTime'] = pd.to_datetime(dataframe['Floor Access DateTime'])
dataframe_sorted = dataframe.sort_values(by='Floor Access DateTime')
dataframe_grouped = dataframe.groupby(['Person Id']).agg({"Floor Access DateTime" : "last", "Floor Level" : "last", "Building" : "last"})

