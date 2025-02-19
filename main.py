import pandas as pd
import matplotlib.pyplot as plt

csv_file = '59068.csv'
delimiter = ';'

data = pd.read_csv(csv_file) #, delimiter=delimiter)

data = data.head()

df = pd.DataFrame(data, columns=["Total Nacional", "Sexo", "Edad", "Periodo", "Total"])
