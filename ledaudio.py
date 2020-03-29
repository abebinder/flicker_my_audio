import pydub;
from pydub import AudioSegment


def led(originalsong, interval_size_ms, percent_on, exportname):
    print("importing")
    song = AudioSegment.from_mp3(originalsong)
    newSong = song[:1]
    print("starting slicing")
    quiet = True
    for ms in range(interval_size_ms, len(song), interval_size_ms):
        print(ms)
        slice = song[ms-interval_size_ms: ms]
        if quiet:
            slice-=6
        newSong = newSong +slice
        quiet=not quiet
    print("exporting")
    newSong.export(exportname, format="mp3")

led("bonnie-tyler-i-need-a-hero-lyrics.mp3", 5000, 50, "secondmashup.mp3" )

