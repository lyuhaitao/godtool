# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['LhtFile', 'NepalModel', 'NepalDataset']

# Cell
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset
import torchvision.models as TM

# Cell
class LhtFile:
    '''
    capsulate the file name and file path
    '''
    def __init__(self,fileName, filePath):
        self.file_name = fileName
        self.file_path = filePath

# Cell
class NepalModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = TM.resnet34(pretrained=True)
        self.fc2 = nn.Linear(1000,2)
    def forward(self,x):
        x = F.relu(self.encoder(x))
        x = torch.sigmoid(self.fc2(x))
        return x

# Cell
class NepalDataset(Dataset):
    def __init__(self, ds, train=True, transform=None):
        data = [i['data'] for i in ds]
        categories = [i['category_id'] for i in ds]
        self.data = data
        self.categories = categories
        self.train = train
        self.transform = transform
    def __len__(self):
        return len(self.data)
    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()
        d = self.data[idx]
        #
        if self.transform:
            d = self.transform(d)
        #
        t = self.categories[idx]
        t = np.array(t,dtype=np.int64)
        t = torch.from_numpy(t)
        rtn = (d,t)
        return rtn

