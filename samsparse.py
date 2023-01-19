import textgrid
import os
import pandas as pd

filelist_path  ="/usr/src/app/uberduck_local/ml/filelist.txt"
data = pd.read_csv(filelist_path, sep="|", header=None, index_col = None)
files = os.listdir("/tmp/asdf_output")
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