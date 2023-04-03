from datasets import load_dataset, load_metric
import json


# 将字典类型数据写入json文件或读取json文件并转为字典格式输出
class FileOperate:
    '''
    需要传入文件所在目录，完整文件名。
    默认为只读，并将json文件转换为字典类型输出
    若为写入，需向dictData传入字典类型数据
    默认为utf-8格式
    '''

    def __init__(self, filepath, filename, way='r', dictData=None, encoding='utf-8'):
        self.filepath = filepath
        self.filename = filename
        self.way = way
        self.dictData = dictData
        self.encoding = encoding

    def operation_file(self):
        if self.dictData:
            self.way = 'a'
        with open(self.filepath + self.filename, self.way, encoding=self.encoding) as f:
            if self.dictData:
                print(self.dictData)
                f.write(json.dumps(self.dictData, ensure_ascii=False)+','+'\n')
            else:
                if '.json' in self.filename:
                    data = json.loads(f.read())
                else:
                    data = f.read()
                return data


music_info_file = 'D:\PythonDemo\Dataset\static_annotations_averaged_songs_1_2000.csv'
music_data_path = 'D:\PythonDemo\Dataset\DEMADataSet'

def main():
    music_label = load_dataset("csv", data_files=music_info_file)
    music_label = music_label["train"].shuffle().select(range(300))
    print(music_label)
    for obj in music_label:
        # dict_data = {"input_music_path": music_data_path + '\\' + str(obj['song_id']) + '.wav',
        #           "music_std_arousal": obj['arousal_std'], "music_std_valence": obj['valence_std']}
        dict_data = {"input_music_path": music_data_path + '\\' + str(obj['song_id']) + '.wav',
                                "music_std_arousal": obj['std_arousal']}
        FileOperate(dictData=dict_data, filepath='./Dataset/', filename='ValidationDataSetArousal.json').operation_file()




if __name__ == "__main__":
    main()


# data_files = "D:\PythonDemo\Dataset\TrainDataSetArousal.json"
# music_info_file = "D:\PythonDemo\Dataset\songs_info.csv"
# # datasets = load_dataset("json", data_files=data_files)
# # input_column_name = "input_music_path"
# # train_datasets = datasets["train"]
# # data_sample = datasets["train"].select(range(2))
# # print(data_sample["input_music_path"])


# for path in datasets["train"].features[output_column_name]:
#     print(path)
