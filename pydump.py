# pydump
def dump(path):
  data = bytes()
  with open(path, "rb") as f:
    data = f.read()
  i = 0
  s = "00000000: "
  s2 = "  "
  for b in data:
    c = chr(b)
    s += "{:02x} ".format(b)
    if int(b) <= 0x20 or int(b) >= 0x80:
      s2 += " "
    elif c.isascii():
      s2 += c
    else:
      s2 += " "
    i += 1
    if i % 16 == 0:
      s += s2
      s += "\n{:08x}: ".format(i)
      s2 = "  "
  if i % 16 > 0:
    s += "   " * (16 - i % 16) + s2
  return s
