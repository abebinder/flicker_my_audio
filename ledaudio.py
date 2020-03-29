import pydub;
from pydub import AudioSegment


def led(originalsong, interval_size_ms, percent_on, exportname, stop_here=10000):
    print("importing")
    song = AudioSegment.from_mp3(originalsong)
    newSong = song[:1]
    print("starting slicing")
    quiet = True
    for ms in range(interval_size_ms, stop_here, interval_size_ms):
        print(ms)
        slice = song[ms-interval_size_ms: ms]
        if quiet:
            slice-=100
        newSong = newSong +slice
        quiet=not quiet
    print("exporting")
    newSong.export(exportname, format="mp3")


