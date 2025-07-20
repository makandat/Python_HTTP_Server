import glob, os

# 指定したフォルダ内のオブジェクト再帰的に検索する。v1.40 asstr=True にした。
def listFilesRecursively(dir:str, wildcard:str="*", asstr=True) -> list :
  diru8 = dir.encode('utf-8')
  list = glob.glob(diru8 + b"/**/" + wildcard.encode('utf-8'), recursive=True)
  result = []
  for item in list :
    if os.path.isfile(item) :
      if asstr :
        item = item.decode('utf-8')
      result.append(item)
  return result
