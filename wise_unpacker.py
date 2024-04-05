import re

def wise(w, i, s, e):
    if w and not i and not s and not e:
        decoded_data = ''
        for index in range(0, len(w), 2):
            decoded_data += chr(int(w[index:index+2], 36))
        return decoded_data

    index1 = 0
    index2 = 0
    index3 = 0
    list1 = []
    list2 = []

    while True:
        if index1 < 5:
            list2.append(w[index1])
        elif index1 < len(w):
            list1.append(w[index1])
        index1 += 1

        if index2 < 5:
            list2.append(i[index2])
        elif index2 < len(i):
            list1.append(i[index2])
        index2 += 1

        if index3 < 5:
            list2.append(s[index3])
        elif index3 < len(s):
            list1.append(s[index3])
        index3 += 1

        if len(w) + len(i) + len(s) + len(e) == len(list1) + len(list2) + len(e):
            break

    part1 = ''.join(list1)
    part2 = ''.join(list2)
    index2 = 0
    result = []

    for index1 in range(0, len(list1), 2):
        offset = -1
        if ord(part2[index2]) % 2:
            offset = 1
        result.append(chr(int(part1[index1:index1+2], 36) - offset))
        index2 += 1
        if index2 >= len(list2):
            index2 = 0

    return ''.join(result)


def recursively_extract(code):
    '''Handles for multiple nested w,i,s,e funcs'''
    extracted = []
    all_matches = re.findall(r"\('(\w*)','(\w*)','(\w*)','(\w*)'\)", code)
    for packed in all_matches:
        data = wise(*packed)
        if "w,i,s,e" in data:
            extract = recursively_extract(data)
            extracted.extend(extract)
        else:
            extracted.append(data)
    return extracted


if __name__ == "__main__":
    wise_code = input("input minified 'w,i,s,e' function: ")
    unpacked = "".join(recursively_extract(wise_code))
    print(unpacked)
