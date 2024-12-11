from gtts import gTTS

# Text for the RPG character
text = []
text.append("Reactor online! Systems online! Weapons online! All systems nominal.")
text.append("Transition complete. Activating stealth protocols. Engaging emission dampeners and sensor masking. All non-essential systems powering down.")
text.append("Pending communications detected. Displaying messages now.")
text.append("Wreckage identified. Data cores and black box detected. Hull integrity compromised. Manual retrieval is not advised.")
text.append("Hostile elements detected. Immediate intervention required.")
text.append("Hostiles closing fast. Captain, what are your orders?")
# Generate the audio using gTTS
count = 0
for item in text:
    tts = gTTS(item, lang='en', tld='com.au')  # Using a female voice style from Australia
    audio_file_path = f"text{count}.mp3"
    tts.save(audio_file_path)
    count += 1
