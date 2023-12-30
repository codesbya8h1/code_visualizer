import os
import webbrowser
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)

# list all models
#models = client.models.list()
#print(models.data[0].id)

# create out completions
#completion = client.completions.create(model="ada", prompt ="Bill gates is a")
#print(completion.choices[0].text)

# image generation with dall-e 2
# image_gen = client.images.generate(prompt="kripya ek husky dog ka photo snow me khelte hue banao",
#                                 n=2,
#                                 size="512x512"
#                                 )

# for img in image_gen.data:
#      webbrowser.open_new_tab(img.url)

# Gwendolyn Brooks Writer's Conference - Keynote Address  (Dr. Donda West)
audio = open("audio/donda.mp3", "rb")
transcript = client.audio.transcriptions.create(model="whisper-1",file=audio)
print(transcript)

