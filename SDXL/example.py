import os
import torch

from diffusers import StableDiffusionXLPipeline, StableDiffusionXLImg2ImgPipeline


path = os.path.abspath(os.path.join('data', 'SDXL'))
pipeline = StableDiffusionXLPipeline.from_single_file(
    os.path.join(path, "sd_xl_base_1.0.safetensors"), torch_dtype=torch.float16
).to("cuda")
#refiner = StableDiffusionXLPipeline.from_single_file(
#    os.path.join(path, "sd_xl_refiner_1.0.safetensors"), torch_dtype=torch.float16
#).to("cuda")

prompt = "A photo-realistic photo of a bald man"
image = pipeline(prompt=prompt).images[0]
image.save(os.path.join(path, "image.png"))

