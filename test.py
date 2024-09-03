import torch
import set2set as s2s
X = torch.randn(2, 5, 10)
import ipdb; ipdb.set_trace()
model = s2s.Set2Set(10, 3, 1)
embedding = model(X)
