import os
import subprocess
import numpy as np
import lightning as L
from PIL import Image, ImageOps
from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer
from utils import img_to_audio_obj


class LitImgToAudio(L.LightningWork):
    def __init__(self) -> None:
        super().__init__()
        self.output_audio_file_path = ''
        self.error_message = None
        self.image_to_audio_obj = img_to_audio_obj

    def run(self, image_np_array):
        self.image_to_audio_obj.predict(image_np_array)
        self.output_audio_file_path = self.image_to_audio_obj.output_audio_file_path
        self.error_message = self.image_to_audio_obj.error_message

