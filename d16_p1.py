import sys

bits = [
    int(bit)
    for char in sys.stdin.read().strip()
    for bit in format(int(char, 16), '04b')
]


def popn(data, n):
    return data[:n], data[n:]


def convert(bits):
    return int(''.join(map(str, bits)), 2)


def parse_packet(data):
    version, data = popn(data, 3)
    version = convert(version)
    ptype, data = popn(data, 3)
    ptype = convert(ptype)

    if ptype == 4:
        value = []
        group = [1]
        while group[0] == 1:
            group, data = popn(data, 5)
            value.extend(group[1:])
        value = convert(value)
    else:
        (ltype,), data = popn(data, 1)
        subpackets = []
        if ltype == 0:
            sublen, data = popn(data, 15)
            sublen = convert(sublen)
            subdata, data = popn(data, sublen)
            while subdata:
                packet, subdata = parse_packet(subdata)
                subpackets.append(packet)
        else:
            nsub, data = popn(data, 11)
            nsub = convert(nsub)
            for _ in range(nsub):
                packet, data = parse_packet(data)
                subpackets.append(packet)
        value = subpackets
    return (version, ptype, value), data


def vsum(packet):
    version, ptype, value = packet
    if ptype != 4:
        version += sum(vsum(p) for p in value)
    return version


packet, _ = parse_packet(bits)
print(vsum(packet))
