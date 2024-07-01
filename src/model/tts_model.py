import edge_tts
import tempfile
import gradio as gr

# get all the voices
async def extract_voices():
  voices = await edge_tts.list_voices()
  return {f"{v['ShortName']} - {v['Locale']} ({v['Gender']})": v['ShortName'] for v in voices}


# text to speech fuction
async def text_to_speech(text,voice,rate,pitch):
  if not text.strip():
    return None, gr.Warning("Please enter a text to convert.")
  if not voice:
    return None, gr.Warning("Please select a voice.")
  
  voice_short_name = voice.split(" - ")[0]
  rate_str = f"{rate:+d}%"
  pitch_str = f"{pitch:+d}Hz"
  
  communicate = edge_tts.Communicate(text,voice_short_name,rate=rate_str,pitch=pitch_str)
  with tempfile.NamedTemporaryFile(delete=False,suffix=".mp3") as tmp_file:
    tmp_path = tmp_file.name
    await communicate.save(tmp_path)
  
  return tmp_path,None
