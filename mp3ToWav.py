from ffmpy import FFmpeg

import os


# MP3转wav
def audio_transfor(audio_path: str, output_dir: str):
    ext = os.path.basename(audio_path).strip().split('.')[-1]
    if ext != 'mp3':
        raise Exception('format is not mp3')

    result = os.path.join(output_dir, '{}.{}'.format(os.path.basename(audio_path).strip().split('.')[0], 'wav'))
    filter_cmd = '-f wav -ac 1 -ar 16000'
    ff = FFmpeg(executable="D:/ffmpeg/ffmpeg-6.0-essentials_build/bin/ffmpeg.exe",
        inputs={
            audio_path: None}, outputs={
            result: filter_cmd})
    print(ff.cmd)
    ff.run()
    return result


def handle(audio_dir: str, output_dir: str):
    for x in os.listdir(audio_dir):
        audio_transfor(os.path.join(audio_dir, x), output_dir)

handle('D:\MERModel\MERDataSet\DEMADataSet\DEAM_audio\MEMD_audio', './Dataset/DEMADataSet')