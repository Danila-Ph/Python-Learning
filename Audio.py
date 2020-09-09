from pydub import AudioSegment
import os

source_dir = r"D:\Projects\Learning\Sound_sources"
result_dir = r"D:\Projects\Learning\Sound_results"
frame_rate = 22050
channels = 1
bitrate = "37k"
source_format = "m4a"
result_format = "mp3"
file_list = os.listdir(source_dir)
for file_name in file_list:
    file_name = os.path.join(source_dir, file_name)
    if os.path.isfile(file_name) and file_name.split('.')[-1] == source_format:
        sound = AudioSegment.from_file(file_name, source_format)
        sound = sound.set_frame_rate(frame_rate)
        sound = sound.set_channels(channels)
        sound.export(os.path.join(result_dir, '.'.join(os.path.basename(file_name).split('.')[:-1]) +
                                  '.' + result_format), format=result_format, bitrate=bitrate)
