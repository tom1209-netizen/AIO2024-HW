import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, arr):
        exps = torch.exp(arr)
        return exps / exps.sum(dim=0)


class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, arr):
        exps = torch.exp(arr - torch.max(arr))
        return exps / exps.sum(dim=0)


# Testing Softmax
data = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float)
softmax = Softmax()
output = softmax(data)
print(output)

# Testing SoftmaxStable
data = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float)
softmax_stable = SoftmaxStable()
output = softmax_stable(data)
print(output)
