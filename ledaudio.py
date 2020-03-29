from pydub import AudioSegment


def led(originalsong, interval_size_ms, exportname, stop_here=10000):
    print("importing")
    song = AudioSegment.from_mp3(originalsong)
    newSong = song[:1] # initialize new AudioSegment that is the first 1 ms of audiofile. (using AudioSegment constructor didnt work)
    print("mixing audio")
    quiet = True
    stop_here = min(stop_here, len(song))
    for ms in range(interval_size_ms, stop_here, interval_size_ms):
        print(ms)
        slice = song[ms-interval_size_ms: ms]
        if quiet:
            slice-=100 #mix 100 decibals lower than current volume
        newSong = newSong +slice #append slice to new audido file
        quiet = not quiet # cycle between quiet and nonquiet sections
    print("exporting")
    newSong.export(exportname, format="mp3")


