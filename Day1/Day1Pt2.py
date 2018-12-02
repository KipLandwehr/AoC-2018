import fileinput

frequency = 0

freq_list = []

while frequency not in freq_list:
    for line in fileinput.input():
        freq_list.append(frequency)
        frequency += int(line)
        if frequency in freq_list:
            print(frequency)
            break
        
fileinput.close()