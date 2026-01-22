import edge_tts, asyncio
from moviepy.editor import ImageClip, AudioFileClip

script = open("script.txt").read()

async def voice():
    tts = edge_tts.Communicate(script, "hi-IN-MadhurNeural")
    await tts.save("voice.mp3")

asyncio.run(voice())

audio = AudioFileClip("voice.mp3")
img = ImageClip("https://picsum.photos/1280/720").set_duration(audio.duration)
video = img.set_audio(audio)
video.write_videofile("video.mp4", fps=24)
