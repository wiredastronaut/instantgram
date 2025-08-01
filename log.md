### 7/25/2025 - 1:50pm
I'd like to use textual inversion, because it seems like a pretty neat technique with concepts I have a good familiarity with. I won't go into too much detail, but basically you have a pre-trained autoencoder and stable diffusion platform and then a textual embedding network. Then with a few images of your reference target/object you're able to create unique text embeddings associated with that target/object that then give the desired output through the autoencoder and stable diffusion network. Essentially the only thing that changes is the representation of the text vector. I referenced this paper https://arxiv.org/abs/2208.01618, and use notebookLM to work it.

Anyway, the first step to doing this is to generate our reference images. I'm going to do some experimentation with this by donwloading and using SDXL - welcome to the wide open world of Stable Diffusion. This stable diffusion network is this paper: https://huggingface.co/papers/2307.01952

Quick Builder's log while things are installing
- Running on WSL Ubutu 22.something
- setup a new venv
- installing torch torchvision and torchaudio `pip3 install torch torchvision torchaudio`
- installed diffusers and transformers `pip install diffusers["torch"] transformers`
- installed invisible-watermark also `pip install invisible-watermark`

### 8/1/2025 - 2:00pm
didn't do a lot. Looked into auto encoders, the first piece of SDXL as I believe the conditioning on the diffusion occurs through the latent items captured within the encoder. It is something like that - I only got to auto encoders. Auto-encoders have many variations from regularizing, denoising, etc. But really they provide a learned way to get data boiled down to a raw data maniofld. A data manifold being a lower dimension represntation of high dimensional space. The best example I saw was a piece of paper. It exists in 3D space but has a representation of 2D data on it. Anyway that is the key to the autoencoder - it encodes the data to this latent space. The trick to autoencoding is balancing the not being completely just copying the input to the output but still considering the output (ie. not too much regularization). This points to the underlying fact that you want your autoencoder to learn the mapping to actually give you a good representation of your data in a good manifold. Or simply a good distilling of the information to the latent space. These are used in a lot of places as they get to the core of the latent space well.

I am having trouble generating repeated images - I tried getting a strict prompt to use that would be repeated but it didn't work because I had a bug in my code! Also tried to speed things up a notch with some different techniques. Anyway the quest to get 3-5 training images for textual inversion continues. I'd like to eventually publish to instagram honestly, via API on an automated procedure.

