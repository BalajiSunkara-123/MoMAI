from modules.speech_to_text import transcribe_audio
from modules.summarizer_pretrained import summarize_text as pretrained_summarize_text
from modules.summarizer_finetuned import summarize_text 
from modules.structure_minutes import structure_minutes


audio_path = "audio/meeting_short.wav"
# audio_path="audio/meeting_telugu.wav"

print(audio_path)

print("Loading Whisper model...")
print("Transcribing audio...")

transcript = transcribe_audio(audio_path)

print("\n--- Transcript ---\n")
print(transcript)

# summary1 = summarize_text(transcript)

# print("\n--- Meeting Summary by a Fine Tuned Model ---\n")
# print(summary1)

# minutes = structure_minutes(summary1)

# print("\n--- Structured Meeting Minutes ---\n")
# print(minutes)


summary2 = pretrained_summarize_text(transcript)

print("\n--- Meeting Summary by a Fine Tuned Model ---\n")
print(summary2)

minutes = structure_minutes(summary2)

print("\n--- Structured Meeting Minutes ---\n")
print(minutes)



