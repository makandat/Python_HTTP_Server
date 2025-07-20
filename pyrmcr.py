# remove CR (pyrmcr.py)

def removeCR(path):
  fi = open(path, "r")
  lines = fi.readlines()
  fi.close()
  newlines = []
  for line in lines:
    newlines.append(line.replace("\r", ""))
  fo = open(path, "w", encoding="utf-8")
  fo.writelines(newlines)
  fo.close()
  return
