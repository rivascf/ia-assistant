from gradio_client import Client, handle_file
import datetime
import time
import pyaudio
import wave

proc_start = req_start = time.time()

client = Client("http://127.0.0.1:7860/")
result = client.predict(
		ref_audio_input=handle_file('.\\audios\\refaudio_female.mp3'),
		ref_text_input="The way you self-analyze, I've always admired it. But at some point, you have to forgive yourself. No one can undo the past.",
		gen_text_input="Hello, darling. How you doing? Today, it's a beautiful night to test my synthetic voice.",
		remove_silence=False,
		cross_fade_duration_slider=0.15,
		speed_slider=1,
		api_name="/basic_tts"
)

# print(result)

req_stop = time.time()

# define stream chunk
chunk = 1024

# open a wav format music
f = wave.open(result[0], "rb")
# instantiate PyAudio
p = pyaudio.PyAudio()
# open stream
stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
				channels=f.getnchannels(),
				rate=f.getframerate(),
				output=True)
# read data
data = f.readframes(chunk)

# play stream
while data:
	stream.write(data)
	data = f.readframes(chunk)

# stop stream
stream.stop_stream()
stream.close()

# close PyAudio
p.terminate()

proc_stop = time.time()
now = datetime.datetime.now()
logfile = f".\\logs\\f5tts_client_{now:%d%m%y}_log.txt"

with open(logfile, "a") as logout:
	logout.write(f"F5TTS[{now:%d-%m%Y %H:%M:%S}]: elapsed: {(proc_stop-proc_start):.2f} seg, req_elapsed: {(req_stop-req_start):.2f} seg \n   output: ({result[0]}, {result[1]}).\n")
