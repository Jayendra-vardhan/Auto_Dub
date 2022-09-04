import speech_recognition as sr				#pip install SpeechRecognition
import os
from pydub import AudioSegment				#pip install pydub
from google.cloud import speech

# # convert mp3 file to wav                                                       
# sound = AudioSegment.from_mp3("transcript.mp3")
# sound.export("transcript.wav", format="wav")


# # transcribe audio file                                                         
# AUDIO_FILE = "transcript.wav"

# # use the audio file as the audio source                                        
# r = sr.Recognizer()
# with sr.AudioFile(AUDIO_FILE) as source:
#     audio = r.record(source)  # read the entire audio file                  

# print("Transcription: " + r.recognize_google(audio))

#code for transcribe a flac file -

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"d:\UPES\Project\translation project\Local_to_GCP\upheld-beach-360516-95be0c166639.json"

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
uri= "gs://flac_file111/how-to-speak-so-that-people-want-to-listen-julian-treasure_RRYwKciD.flac"

audio = speech.RecognitionAudio(uri=uri)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
    sample_rate_hertz=44100,
    audio_channel_count=2,
    language_code="en-US",
    enable_word_confidence=True,                    #for word level confidence
)


operation = client.long_running_recognize(config=config, audio=audio)      # for long audio files

print("Waiting for operation to complete...")
response = operation.result(timeout=180)                                #to create an intrupt if taking more time

# Each result is for a consecutive portion of the audio. Iterate through
# them to get the transcripts for the entire audio file.
for result in response.results:
    # The first alternative is the most likely one for this portion.
    print(u"Transcript: {}".format(result.alternatives[0].transcript))
    print("Confidence: {}".format(result.alternatives[0].confidence))
