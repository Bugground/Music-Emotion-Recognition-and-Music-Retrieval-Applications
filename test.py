from datasets import load_dataset, load_metric
import json

music_info_file = 'D:\PythonDemo\Dataset\static_annotations.csv'
music_data_path = 'D:\PythonDemo\Dataset\ecomusic'

data_files = "D:\PythonDemo\Dataset\TrainDataSet.json"
music_info_file = "D:\PythonDemo\Dataset\songs_info.csv"
datasets = load_dataset("json", data_files=data_files)
input_column_name = "input_music_path"
train_datasets = datasets["train"]
data_sample = datasets["train"].select(range(2))
print(train_datasets)


# for path in datasets["train"].features[output_column_name]:
#     print(path)
