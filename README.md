# LAI_image_to_audio component

This ⚡ [Lightning component](lightning.ai) ⚡ was generated automatically with:

```bash
lightning init component LAI_image_to_audio
```

## To run LAI_image_to_audio

First, install LAI_image_to_audio (warning: this component has not been officially approved on the lightning gallery):

```bash
lightning install component https://github.com/theUser/LAI_image_to_audio
```

Once the app is installed, use it in an app:

```python
from LAI_image_to_audio import TemplateComponent
import lightning as L


class LitApp(L.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        self.LAI_image_to_audio = TemplateComponent()

    def run(self):
        print("this is a simple Lightning app to verify your component is working as expected")
        self.LAI_image_to_audio.run()


app = L.LightningApp(LitApp())
```
