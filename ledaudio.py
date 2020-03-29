import pydub;
from pydub import AudioSegment

print("importing audio")

song = AudioSegment.from_mp3("bonnie-tyler-i-need-a-hero-lyrics.mp3")

ten_seconds = 10 * 1000

first_10_seconds = song[:ten_seconds]

last_5_seconds = song[-10000:]

# boost volume by 6dB
beginning = first_10_seconds + 6

# reduce volume by 3dB
end = last_5_seconds - 3

print("exporting")

(beginning + end).export("mashup.mp3", format="mp3")

def led(originalsong, interval_size_ms, percent_on, exportname):
    newSong = AudioSegment()
    song = AudioSegment.from_mp3(originalsong)
    quiet = True
    for ms in range(interval_size_ms, len(song), interval_size_ms):
        slice = song[ms-interval_size_ms: ms]
        if quiet():
            slice-6
        newSong.append(slice)
        quiet=not quiet
    newSong.export(exportname, format="mp3")

led("bonnie-tyler-i-need-a-hero-lyrics.mp3", 5000, 50, "secondmashup.mp3" )

