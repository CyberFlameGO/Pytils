map = {
    '01': 'a', '1000': 'b', '1010': 'c', '100': 'd', '0': 'e', '0010': 'f', '110': 'g', '0000': 'h',
    '00': 'i', '0111': 'j', '101': 'k', '0100': 'l', '11': 'm', '10': 'n', '111': 'o', '0110': 'p',
    '1101': 'q', '010': 'r', '000': 's', '1': 't', '001': 'u', '0001': 'v', '011': 'w', '1001': 'x',
    '1011': 'y', '1100': 'z',
    '01111': '1', '00111': '2', '00011': '3', '00001': '4', '00000': '5', '10000': '6', '11000': '7', '11100': '8',
    '11110': '9', '11111': '0'
}
INDEX_BREAK = 2


def reverse_map(inmap):
    outmap = {}
    for key in inmap.keys():
        val = inmap[key]
        outmap[val] = key
    return outmap


def map_input(chunks, inmap):
    output = list()
    for chunk in chunks:
        if chunk in inmap.keys():
            output.append(inmap[chunk])
    return output


def raw_to_charset(chunk):
    charset = None
    if charset is None:
        return chunk
    outchunk = ""

    for c in chunk:
        num = ord(c) - ord('0')
        outchunk += charset[num]
    return outchunk


def charset_to_raw(chunk):
    charset = None
    if charset is None:
        return chunk
    outchunk = ""
    for c in chunk:
        index = charset.index(c)
        val = chr(index + ord('0'))
    outchunk += val
    return outchunk


def set_charset(chunks):
    out2 = list()
    for chunk in chunks:
        out2.append(raw_to_charset(chunk))
    return out2


def remove_charset(chunks):
    out2 = list()
    for chunk in chunks:
        out2.append(charset_to_raw(chunk))
    return out2


def split_chunk(string):
    splitted = string.split(INDEX_BREAK)


def morse_dec(string):
    chunks = remove_charset(string)
    split_chunk(string)
    output = map_input(chunks, map)
    return "".join(output)


def morse_enc(string):
    string = string.lower()
    output = map_input(string, reverse_map())
    out2 = set_charset(output)
    return INDEX_BREAK.join(out2)