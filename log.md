### 7/25/2025 - 1:50pm
I'd like to use textual inversion, because it seems like a pretty neat technique with concepts I have a good familiarity with. I won't go into too much detail, but basically you have a pre-trained autoencoder and stable diffusion platform and then a textual embedding network. Then with a few images of your reference target/object you're able to create unique text embeddings associated with that target/object that then give the desired output through the autoencoder and stable diffusion network. Essentially the only thing that changes is the representation of the text vector. I referenced this paper https://arxiv.org/abs/2208.01618, and use notebookLM to work it.

Anyway, the first step to doing this is to generate our reference images. I'm going to do some experimentation with this by donwloading and using SDXL - welcome to the wide open world of Stable Diffusion. This stable diffusion network is this paper: https://huggingface.co/papers/2307.01952

Quick Builder's log while things are installing
- Running on WSL Ubutu 22.something
- setup a new venv
- installing torch torchvision and torchaudio `pip3 install torch torchvision torchaudio`
- installed diffusers and transformers `pip install diffusers["torch"] transformers`
- installed invisible-watermark also `pip install invisible-watermark`

Logging off for the day: It was pretty easy to run, and it basically just gets to the prompting. There's a lot of detail in all the calls and everything so I'll have to look into that next. The example.py runs well, but the images are leaving something to be desired in terms of what's capable of realism. I'll try the refiner pipeline next though and that should help.
