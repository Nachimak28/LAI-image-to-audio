import subprocess
import numpy as np
from PIL import Image, ImageOps
from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer

class ImageToAudio:
    def __init__(self):
        self.output_audio_file_path = ''
        self.error_message = ''
        self.max_length = 16
        self.num_beams = 4
        self.gen_kwargs = {"max_length": self.max_length, "num_beams": self.num_beams}
        self.model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
        self.feature_extractor = ViTFeatureExtractor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
        self.tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

    def _get_image_caption(self, image_np_array):
        try:
            # convert the image to pillow format
            image = Image.fromarray(image_np_array).convert('RGB')
            image = ImageOps.exif_transpose(image) #managing the exif of the image
            pixel_values = self.feature_extractor(images=[image], return_tensors="pt").pixel_values
            # pixel_values = pixel_values.to(device)
            output_ids = self.model.generate(pixel_values, **self.gen_kwargs)
            preds = self.tokenizer.batch_decode(output_ids, skip_special_tokens=True)
            preds = [pred.strip() for pred in preds]
            return preds[0]
        except Exception as e:
            self.error_message = str(e)
            return None

    def _generate_audio_from_caption(self, caption_text_string):
        if isinstance(caption_text_string, str) and caption_text_string.strip() != '':
            target_path = './speech.wav'
            cmd = f'tts --text "{caption_text_string}" --out_path {target_path}'
            subprocess.run(cmd, shell=True)
            return target_path
        else:
            self.error_message = 'Cannot process this string'
        return None

    def predict(self, image_np_array):
        if isinstance(image_np_array, np.ndarray):
            # generate image caption
            caption = self._get_image_caption(image_np_array)
            if caption != None:
                # generate the audio
                self.output_audio_file_path = self._generate_audio_from_caption(caption)
                self.error_message = None
        else:
            self.output_audio_file_path = None
            self.error_message = 'Invalid image Data type'

img_to_audio_obj = ImageToAudio()