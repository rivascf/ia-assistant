from gradio_client import Client, handle_file
import datetime
import time

proc_start = req_start = time.time()
#client = Client("http://127.0.0.1:7860/")
client = Client("http://127.0.0.1:7860/")
text = """
	The paper titled "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control" by Brohan et al. 
	(2023) explores the integration of vision-language models with robotic control systems. The goal of the study is to 
	improve the generalization capabilities and emergent semantic reasoning in robotic tasks by leveraging large-scale 
	pretraining on language and vision-language data from the web."""
text2 = "The RT-2 model aims to bridge this gap by training VLMs to output low-level robotic actions directly. This is achieved by expressing robot actions as text tokens, allowing them to be integrated into the training data alongside natural language tokens. This method, referred to as vision-language-action (VLA) modeling, leverages the extensive pretraining of VLMs on internet-scale data, enabling the model to generalize better and exhibit emergent capabilities such as interpreting novel commands and performing multi-stage reasoning."
audio_file, spec_file = client.predict(
		ref_audio_orig=handle_file(".\\audios\\refaudio_female.mp3"),
		ref_text="The way you self-analyze, I've always admired it. But at some point, you have to forgive yourself. No one can undo the past.",
		gen_text="Hello, darling. How you doing? Today, it's a beautiful night to test my synthetic voice.",
#		gen_text="Hello, dad. How you doing? Today, it's a beautiful night to test my synthetic voice.",
#		gen_text=text,
#		gen_text=text2,
		model="F5-TTS",
		remove_silence=False,
		cross_fade_duration=0.12,
		speed=1.1,
		api_name="/infer"
)

# print(type(result))
# print(result)
req_stop = time.time()

import pyaudio
import wave

# define stream chunk
chunk = 1024

# open a wav format music
f = wave.open(audio_file, "rb")
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
	logout.write(f"F5TTS[{now:%d-%m%Y %H:%M:%S}]: elapsed: {(proc_stop-proc_start):.2f} seg, req_elapsed: {(req_stop-req_start):.2f} seg \n   output: ({audio_file}, {spec_file}).\n")
