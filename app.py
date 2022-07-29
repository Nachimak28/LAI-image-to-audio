from LAI_image_to_audio import LitImgToAudio
from PIL import Image
import requests
import numpy as np
import lightning as L


class LitApp(L.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        self.LAI_image_to_audio = LitImgToAudio()

    def run(self):
        demo_image_url = 'https://cdn.pixabay.com/photo/2022/07/25/10/19/mountain-7343375_960_720.jpg'
        image = Image.open(requests.get(demo_image_url, stream=True).raw)
        self.LAI_image_to_audio.run(np.array(image))
        print(self.LAI_image_to_audio.output_audio_file_path)
        print(self.LAI_image_to_audio.error_message)


app = L.LightningApp(LitApp())
