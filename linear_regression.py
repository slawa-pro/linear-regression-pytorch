import torch

x = torch.tensor([1.0, 2.0, 3.0])
y = torch.tensor([2.0, 4.0, 6.0]) # y =  2x

w = torch.tensor(0.0, requires_grad=True)
b = torch.tensor(0.0, requires_grad=True)



