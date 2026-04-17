import re
html = open('index.html', 'r', encoding='utf-8').read()
imgs = re.findall(r"<img[^>]*src=['\"]([^'\"]+)['\"]", html)
print(f"Total img src values found: {len(imgs)}")
print("First 5:")
for i in imgs[:5]:
    print(" ", i)
