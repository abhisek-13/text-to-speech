import asyncio
import gradio as gr
from src.model import tts_model

# gradio interface
def gradio_interface(text,voice,rate,pitch):
  audio,warning = asyncio.run(tts_model.text_to_speech(text,voice,rate,pitch))
  return audio,warning

# gradio application
async def gradio_app():
  
  voices = await tts_model.extract_voices()
  
  app = gr.Interface(
    fn = gradio_interface,
    inputs=[
      gr.Textbox(label="Input Text",lines=10),
      gr.Dropdown(choices = [""] + list(voices.keys()),label="Select Voice",value=""),
      gr.Slider(minimum=-50,maximum=50,value=0,label="Speech Rate (%)",step=1),
      gr.Slider(minimum=-20,maximum=20,value=0,label="Pitch (Hz)",step=1)
    ],
    outputs=[
      gr.Audio(label="Generated Audio",type="filepath"),
      gr.Markdown(label='Warning',visible=False)
    ],
    title="Edge TTS Text-to-Speech",
      description="Convert text to speech using Microsoft Edge TTS Model.",
        analytics_enabled=False,
        allow_flagging=False
  )
  return app
  
if __name__ == "__main__":
  demo = asyncio.run(gradio_app())
  demo.launch()
