r"""
To test a lightning component:

1. Init the component.
2. call .run()
"""
from LAI_image_to_audio.component import LitImgToAudio
from PIL import Image
import numpy as np
import requests

def test_placeholder_component():
    lai_image_to_audio = LitImgToAudio()
    demo_image_url = 'https://cdn.pixabay.com/photo/2022/07/25/10/19/mountain-7343375_960_720.jpg'
    image = Image.open(requests.get(demo_image_url, stream=True).raw)
    lai_image_to_audio.run(np.asarray(image))
    assert lai_image_to_audio.output_audio_file_path == './speech.wav'
