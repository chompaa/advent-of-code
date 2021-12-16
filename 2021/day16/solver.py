from math import prod

with open("input.txt") as f:
  bin_line = "".join(bin(int(c, 16))[2:].zfill(4) for c in f.readlines()[0])


def parse(line):
  version = int(line[0:3], 2)
  type_id = int(line[3:6], 2)

  if type_id == 4:
    num = ""
    # split the line into chunks of 5
    line = [line[i + 6:i + 11] for i in range(0, len(line), 5)]

    for idx, bits in enumerate(line):
      num += bits[1:]

      if bits[0] == "0":
        break

    return {
        "version": version,
        "type_id": type_id,
        "sub_pkts": [],
        "size": (idx * 5) + 11,
        "dec_value": int(num, 2),
    }

  else:
    len_type_id = int(line[6])

    if len_type_id == 0:
      sub_pkts = []
      start = 22

      while sum(pkt["size"] for pkt in sub_pkts) < int(line[7:22], 2):
        sub_pkts.append(parse(line[start:]))
        start += sub_pkts[-1]["size"]

    else:
      sub_pkts = []
      start = 18

      while len(sub_pkts) < int(line[7:18], 2):
        sub_pkts.append(parse(line[start:]))
        start += sub_pkts[-1]["size"]

    return {
        "version": version,
        "type_id": type_id,
        "sub_pkts": sub_pkts,
        "size": start,
    }


pkt = parse(bin_line)


# part 1

def sum_versions(pkt):
  return sum(sum_versions(p) for p in pkt["sub_pkts"]) + pkt["version"]


print(sum_versions(pkt))


# part 2

def op(pkt):
  match pkt["type_id"]:
    case 0:
      return sum(op(p) for p in pkt["sub_pkts"])
    case 1:
      return prod(op(p) for p in pkt["sub_pkts"])
    case 2:
      return min(op(p) for p in pkt["sub_pkts"])
    case 3:
      return max(op(p) for p in pkt["sub_pkts"])
    case 4:
      return pkt["dec_value"]
    case 5:
      return op(pkt["sub_pkts"][0]) > op(pkt["sub_pkts"][1])
    case 6:
      return op(pkt["sub_pkts"][0]) < op(pkt["sub_pkts"][1])
    case 7:
      return op(pkt["sub_pkts"][0]) == op(pkt["sub_pkts"][1])


print(op(pkt))
