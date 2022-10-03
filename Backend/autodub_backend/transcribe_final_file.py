from google.cloud import speech_v1 as speech
import os
import io

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\\Bipul\OneDrive\Desktop\autodub_backend\upheld-beach-360516-6f0235cf6bf9.json"

def speech_to_text(config, audio):
    client = speech.SpeechClient()
    operation = client.long_running_recognize(config=config, audio=audio)       #for long audio files
    response = operation.result(timeout=180)
    print_sentences(response)
    return response

def print_sentences(response):
    for result in response.results:
        best_alternative = result.alternatives[0]
        transcript = best_alternative.transcript
        confidence = best_alternative.confidence
        print("-" * 80)
        print(f"Transcript: {transcript}")
        print(f"Confidence: {confidence:.0%}")
        print_word_offsets(best_alternative)

def print_word_offsets(alternative):
    for word in alternative.words:
        confidence = word.confidence
        start_s = word.start_time.total_seconds()
        end_s = word.end_time.total_seconds()
        word = word.word
        print(f"{start_s:>7.3f} | {end_s:>7.3f} | {word} |{confidence:.0%}")
        with open('transcribe.txt', 'a') as the_file:
            the_file.write(f"{start_s:>7.3f} | {end_s:>7.3f} | {word} |{confidence:.0%}\n")


def transcribe_file():
    #local_file_path=r"C:\Users\DELL\Downloads\What is a gig economy_.MP3"
    local_file_path=r"C:\\Users\\Bipul\\OneDrive\\Desktop\\autodub_backend\\A one minute TEDx Talk for the digital age  Woody Roseland  TEDxMileHigh.mp3"
    config = dict(
        language_code="en-US",
        sample_rate_hertz=44100,
        enable_automatic_punctuation=True,
        enable_word_time_offsets=True,
        audio_channel_count = 2,
        enable_word_confidence=True)
    
    with io.open(local_file_path, "rb") as f:           #import io
        content = f.read()
    audio = {"content": content}
    
    # audio = dict(uri="gs://flac_file111/how-to-speak-so-that-people-want-to-listen-julian-treasure_RRYwKciD.flac")
    
    response = speech_to_text(config, audio)
    print(response)

    x = str(response)
    text_file = open("response.json", "w")
    text_file.write(x)
    text_file.close()
    
transcribe_file()