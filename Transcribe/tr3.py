"""Asynchronously transcribes the audio file specified by the gcs_uri."""
from google.cloud import speech
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"d:\UPES\Project\translation project\Local_to_GCP\upheld-beach-360516-95be0c166639.json"

def transcribe_gcs(gcs_uri):
       
       
    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=44100,
        audio_channel_count=2,
        language_code="en-US",
    )

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=120)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u"Transcript: {}".format(result.alternatives[0].transcript))
        print("Confidence: {}".format(result.alternatives[0].confidence))
        
def main():
    print("waiting for function...")
    link="gs://flac_file111/how-to-speak-so-that-people-want-to-listen-julian-treasure_RRYwKciD.flac"
    transcribe_gcs(link)
    
if __name__== "__main__" :
    main()