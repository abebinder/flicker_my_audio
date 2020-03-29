from progress.bar import ChargingBar
from pydub import AudioSegment


def led(original_audio_path, interval_size_ms, export_file_name, stop_here=10000):
    print("importing")
    original_audio = AudioSegment.from_mp3(original_audio_path)
    new_audio = original_audio[:1]  # initialize new AudioSegment that is the first 1 ms of audiofile. (using AudioSegment constructor didnt work)
    quiet = True
    stop_here = min(stop_here, len(original_audio))
    bar = ChargingBar('Mixing Audio', max=stop_here // interval_size_ms)
    for ms in range(interval_size_ms, stop_here, interval_size_ms):
        slice = original_audio[ms - interval_size_ms: ms]
        if quiet:
            slice -= 100  # mix 100 decibals lower than current volume
        new_audio = new_audio + slice  # append slice to new audido file
        quiet = not quiet  # cycle between quiet and nonquiet sections
        bar.next()
    bar.finish()
    print("exporting")
    new_audio.export(export_file_name, format="mp3")
