from torch.utils.data import Dataset
from PIL import Image
import os
from torchvision import transforms
from torch.utils.data import DataLoader 


class VisionDataset(Dataset):

    def __init__(self, folder, transform=None):
        self.images = []
        self.labels = []
        self.transform = transform

        # 0 -> cat, 1 -> dog
        for label, category in enumerate(os.listdir(folder)):

            category_path = os.path.join(folder, category)

            for file in os.listdir(category_path):

                image_path = os.path.join(category_path, file)

                self.images.append(image_path)
                self.labels.append(label)

    def __len__(self):
        return len(self.images)

    def __getitem__(self, index):

        image = Image.open(self.images[index]).convert("RGB")

        if self.transform:
            image = self.transform(image)

        label = self.labels[index]

        return image, label


transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])


dataset = VisionDataset("images", transform)

print("Number of images:", len(dataset))

image, label = dataset[0]

print("Image shape:", image.shape)
print("Label:", label)