x, min_v, max_v = [float(val) for val in input().split()]
norm = (x - min_v) / (max_v - min_v)
print(f"{norm:.2f}")