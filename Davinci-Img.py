import os
import openai
import pyaudio
import wave

openai.api_key = "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"

choice = int(input("1-Text, 2-CreateImg: "))

if choice == 1:
    user_input = input("TExT: ")
    input_maxString = input("String length: ")


    def call_gpt(string, max_string):
        answer = openai.Completion.create(
            model="text-davinci-003",
            prompt=string,
            max_tokens=max_string,
            temperature=0
        )
        return answer.choices[0]["text"]


    print(call_gpt(user_input, int(input_maxString)))

elif choice == 2:
    prompt777 = input("Prompt: ")

    def create_gpt(prompt1):
        image = openai.Image.create(
            prompt=prompt1,
            n=1,
            size="1024x1024"
        )
        return image.data[0]["url"]


    print(create_gpt(prompt777))

elif choice == 3:
    audioFile = "import_audio.mp3"
    chunk = 1024
    FORMAT = pyaudio.paInt16
    channels = 1
    sample_rate = 44100
    record_seconds = 5
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
        audio_file = open("import_audio.mp3", "rb")
        transcript = str(openai.Audio.transcribe("whisper-1", audio_file))
        transcript1 = transcript[17:(len(transcript) - 3)]
        return transcript1


    print(audio_to_text())

else:
    print("None")


