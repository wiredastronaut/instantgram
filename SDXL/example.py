import os
import torch

from diffusers import StableDiffusionXLPipeline, StableDiffusionXLImg2ImgPipeline


path = os.path.abspath(os.path.join('data', 'SDXL'))
pipeline = StableDiffusionXLPipeline.from_single_file(
    os.path.join(path, "sd_xl_base_1.0.safetensors"), torch_dtype=torch.float16
).to("cuda")
refiner = StableDiffusionXLPipeline.from_single_file(
    os.path.join(path, "sd_xl_refiner_1.0.safetensors"), torch_dtype=torch.float16,
    text_encoder_2=pipeline.text_encoder_2,
    vae = pipeline.vae,
).to("cuda")

prompt = "A photo-realistic photo of a happy bald man"
latent_images = pipeline(prompt=prompt, num_inference_steps=40, denoising_end=0.8, output_type="latent").images
image = refiner(prompt=prompt, num_inference_steps=40, denoising_start=0.8, image=latent_images).images[0]
image.save(os.path.join(path, "image.png"))

