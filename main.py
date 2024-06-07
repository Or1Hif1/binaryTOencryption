
def num_to_binary(num, bits):
    bini = ""
    for x in range(0, bits):
        if num >= pow(2, (bits - x - 1)):
            bini += "1"
            num -= pow(2, (bits - x - 1))
        else:
            bini += "0"
    return bini


def text_to_binary(text: str, bits):
    bini = ""
    for x in text:
        bini += num_to_binary(ord(x), bits) + " "
    return bini


def binary_to_num(bini: str):
    count = 0
    power = 0
    for x in range(0, 16):
        if bini[16-x-1] == "1":
            count += pow(2, power)
        power += 1
    return count


def num_to_ascii(num):
    ascii_char = ""
    for num in [num]:
        ascii_char += chr(num)
    return ascii_char


def long_binary_to_text(long_text: str):
    txt = long_text.split()
    print(txt)
    new_text = ""
    for x in txt:
        new_text += str(num_to_ascii(binary_to_num(x)))
    return new_text


def xor(bini: str, num):
    new = num_to_binary(num, 16)
    new_bini = ""
    for i in range(0, len(bini)):
        if new[i] != bini[i]:
            new_bini += "1"
        else:
            new_bini += "0"
    return new_bini


def full_binary_to_xor(bini: str, num):
    txt = bini.split()
    new_bini = ""
    for x in txt:
        new_bini += xor(x, num) + " "
    return new_bini


def main():
    f = open("Text.txt", "r+", encoding="utf-8")
    textfile = str(f.read())
    f.seek(0)
    f.write(long_binary_to_text(full_binary_to_xor(text_to_binary(textfile, 16), 22)))
    f.close()


main()
