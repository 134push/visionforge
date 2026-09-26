from PIL import Image
import numpy as np
import torch 

print(torch.__version__)
image = Image.open("images/dog/dog1.jpg")

pixels = np.array(image)

print("NumPy type:", type(pixels))
print("NumPy shape:", pixels.shape)

tensor = torch.tensor(pixels)

## Neural network calculationsમાં decimal values જોઈએ.
tensor = torch.tensor(pixels, dtype=torch.float32)
print("Before normalization:", tensor[100, 100])
tensor = tensor / 255.0
print("After normalization:", tensor[100, 100])
print("Data type:", tensor.dtype)


print("Tensor type:", type(tensor))
print("Tensor shape:", tensor.shape)

print("Pixel:", tensor[100, 100])

# pytorch expect data in this format (Batch, Channels, Height, Width) not (Height, Width, Channels)
tensor = tensor.permute(2, 0, 1)
# PyTorch models expect (Batch, Channels, Height, Width)
print("Permuted Tensor shape (Batch, Channels, Height, Width):", tensor.shape)