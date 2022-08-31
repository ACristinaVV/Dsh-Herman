from functions import get_data

path = "files/Sales_data.csv"
sales = get_data(path=path, col_names=["Fecha", "Total"], index="Fecha")
