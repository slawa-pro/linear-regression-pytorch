import torch

x = torch.tensor([1.0, 2.0, 3.0])
y = torch.tensor([2.0, 4.0, 6.0]) # y =  2x

w = torch.tensor(0.0, requires_grad=True)
b = torch.tensor(0.0, requires_grad=True)

optimizer = torch.optim.SGD([w, b], lr=0.01)

for epoch in range(100):
    y_pred = w * x + b

    loss = ((y_pred - y)**2).mean()
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        print(f'Epoch {epoch}, w={w.item():.3f}, b={b.item():.3f}, loss={loss.item():.3f}')

print(f'Итог: w={w.item():.3f}, b={b.item():.3f}')