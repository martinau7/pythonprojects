import openai

import speech_recognition as sr
import pyttsx3

# Initialize OpenAI API
openai.api_key = "Enter your OpenAI API key here"
# Initialize the text to speech engine 
engine = pyttsx3.init()


def transcribe_audio_to_text(filename):
    recogizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recogizer.record(source)
    try:
        return recogizer.recognize_google(audio)

    except:
        print("Skipping unknown error")


def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"]


def speak_text(text):
    engine.say(text)
    engine.runAndWait()


def main():
    while True:
        # Wait for the user to say "Hello"
        print("Say 'Hello' to start recording your question: ")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "hello":
                    # Record the audio from the default microphone
                    filename = "input.wav"
                    print("Ask your question: ")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())

                    # Transcribing audio to text
                    text = transcribe_audio_to_text(filename)
                    if text:
                        print(f"Your question was:  {text}")

                        if text.lower() == "shut down":
                            print("Goodbye!")
                            break  # End the program if user says "shutdown"

                        # Generating the response
                        response = generate_response(text)
                        print(f"A.I. says:  {response}")
            except Exception as e:

                print("An error occurred : {}".format(e))


if __name__ == "__main__":
    main()
