from data_manager.manager import load_data
from data_statistics.statistics import get_statistics

data_len = get_statistics()
print(f"В файле {data_len} записей")

data = load_data()
print(f"{data= }")
