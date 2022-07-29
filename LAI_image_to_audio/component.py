import lightning as L
from .utils import ImageToAudio

image_to_audio_obj = ImageToAudio()


class LitImgToAudio(L.LightningWork):
    def __init__(self) -> None:
        super().__init__()
        self.output_audio_file_path = ''
        self.error_message = None

    def run(self, image_np_array):
        image_to_audio_obj.predict(image_np_array)
        self.output_audio_file_path = image_to_audio_obj.output_audio_file_path
        self.error_message = image_to_audio_obj.error_message
