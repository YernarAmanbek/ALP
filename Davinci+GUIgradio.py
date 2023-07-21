import openai
import pyaudio
import wave
import gradio as gr
import requests
import shutil

openai.api_key = "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"

def nothing():
    return 0

def call_gpt(string, max_string):
    answer = openai.Completion.create(
        model="text-davinci-003",
        prompt=string,
        max_tokens=max_string,
        temperature=0
    )
    return answer.choices[0]["text"]

def create_gpt(prompt1):
    image = openai.Image.create(
        prompt=prompt1,
        n=1,
        size="1024x1024"
    )
    url = image.data[0]["url"]
    res = requests.get(url,stream = True)
    with open("image01.png", 'wb') as f:
        shutil.copyfileobj(res.raw, f)
    image777 = 'image01.png'
    return image777


def something(text):

    audioFile = "import_audio1.mp3"
    chunk = 1024
    FORMAT = pyaudio.paInt16
    channels = 1
    sample_rate = 44100
    record_seconds = 10
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    output=True,
                    frames_per_buffer=chunk)
    frames = []
    print("Recording...")
    for i in range(int(sample_rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)
    print("Finished recording.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(audioFile, "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(sample_rate)
    wf.writeframes(b"".join(frames))
    wf.close()



    def audio_to_text():
        audio_file = "import_audio1.mp3"
        audio_file = open(audio_file, "rb")
        transcript = str(openai.Audio.transcribe("whisper-1", audio_file))
        transcript1 = transcript[17:(len(transcript) - 3)]

        bomj = transcript1.encode('utf-8').decode('unicode-escape')

        return bomj

    transcrpted_text = audio_to_text()

    def audio_translate():
        audio_file = "import_audio1.mp3"
        audio_file = open(audio_file, "rb")
        translate = openai.Audio.translate("whisper-1", audio_file)
        translate1 = translate['text']

        return translate1

    translated_text = audio_translate()

    return transcrpted_text, translated_text


app1 = gr.Interface(fn = call_gpt, inputs=["text",gr.Slider(0,1000)], outputs="text", theme='freddyaboulton/dracula_revamped')

app2 = gr.Interface(fn = create_gpt, inputs="text", outputs=[gr.Image(shape=(400,400))],theme='gstaff/xkcd')

app3 = gr.Interface(fn = something, inputs=gr.Button(value="none"), outputs=["text","text"],theme='gstaff/xkcd')

demo = gr.TabbedInterface([app1, app2, app3], ["Text", "Image", "Language"])

demo.launch()