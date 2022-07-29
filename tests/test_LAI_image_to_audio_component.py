r"""
To test a lightning component:

1. Init the component.
2. call .run()
"""
from LAI_image_to_audio.component import LitImgToAudio


def test_placeholder_component():
    messenger = LitImgToAudio()
    messenger.run()
    assert messenger.output_audio_file_path == './speech.wav'
