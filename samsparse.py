import textgrid
import os
import pandas as pd

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

filelist_path  ="/usr/src/app/uberduck_local/ml/filelist.txt"
data = pd.read_csv(filelist_path, sep="|", header=None, index_col = None)
files_2 = os.listdir("/tmp/asdf_output")
files = list(data[0])
files = [f"{file.split('/')[-1].split('.')[0]}.TextGrid" for file in files]
files = intersection(files, files_2)
duration_data = []
phoneme_data = []
start_data = []
for file in files:
    start_frames = [0]
    tg = textgrid.TextGrid.fromFile(f"/tmp/asdf_output/{file}")
    intervals = tg[1]
    phonemes = []
    durations = []
    for interval in intervals:
        phonemes.append(interval.__dict__["mark"])
        frame_duration = int(interval.duration()* 80)
        durations.append(str(frame_duration))
        start_frames.append(start_frames[-1] + frame_duration)
    start_frames = [str(start_frame) for start_frame in start_frames[:-1]]
    duration_datum = " ".join(durations)
    phoneme_datum = " ".join(phonemes)
    duration_data.append(duration_datum)
    phoneme_data.append(phoneme_datum)
    start_data.append(" ".join(start_frames))

paths = []
for i, datum in data.iterrows():
    path = datum[0].split("/")[-1]
    paths.append(path)

text_data = list(data[1])
path_data = list(data[0])

fastspeech_data = pd.DataFrame([text_data, start_data, duration_data, phoneme_data, paths]).transpose()
fastspeech_data.iloc[:1].to_csv("/tmp/fastspeech_data.txt", index=None, header = None, sep="|")


fastspeech_data_gimp = fastspeech_data.iloc[6:7].copy()
fastspeech_data_gimp.to_csv("/tmp/fastspeech_data.txt", index=None, header = None, sep="|")




# fastspeech_data_gimp = fastspeech_data.iloc[6:7].copy()
# fastspeech_data_gimp.iloc[0,0] = "gimp"
# fastspeech_data_gimp.iloc[0,4] = fastspeech_data.iloc[5,4]
# fastspeech_data_gimp.iloc[0,1] = fastspeech_data.iloc[5,1]
# fastspeech_data_gimp.iloc[0,2] = fastspeech_data.iloc[5,2]
# fastspeech_data_gimp.iloc[0,3] = fastspeech_data.iloc[5,3]
# fastspeech_data_gimp.to_csv("/tmp/fastspeech_data.txt", index=None, header = None, sep="|")


