print("nhập các dòn văn bản { nhập done để end):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
    #chuyển thành chữ in hoa và ra màn hình
    print("\nCacs dòng đã nhập sau khi thành in hoa:")
    for line in lines:
        print(lines.upper())
        