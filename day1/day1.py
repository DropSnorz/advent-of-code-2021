
def main():
    
    f = open("input.txt", "r")
    content = f.read()
    rawvalues = [int(line.strip()) for line in content.split("\n")]

    values = []
    for index in range(len(rawvalues)):
          values.append(sum(rawvalues[index:index + 3]))

    increased = 0

    for index in range(1, len(values)):
        if values[index] > values[index - 1]:
          increased+=1
        else:
            continue
        
    print(increased)

main()