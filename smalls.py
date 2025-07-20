#!/usr/bin/env python3
#  smalls.py v.1.3.2
import os
from PIL import Image, ImageFilter

# 縮小画像のサイズを計算する。
def getImageSize(im, size) :
  imgw = im.size[0]
  imgh = im.size[1]
  if imgw > imgh:
    # 横長の時
    nw = size
    nh = size * imgh // imgw
  else:
    # 縦長の時
    nw = size * imgw // imgh
    nh = size
  return (nw, nh)


def small(folder, savepath, size):
  # 指定されたフォルダ内の画像ファイル一覧を得る。
  files = os.listdir(folder)
  if not os.path.exists(savepath):
    os.mkdir(savepath)
  i = 0
  for f in files:
    path = folder + "/" + f
    ext = os.path.splitext(path)[1]
    # 拡張子をチェック
    if (ext == ".jpg" or ext == ".png"):
      im = Image.open(path)
      im = im.convert('RGB')
      newsize = getImageSize(im, size)
      if im.size[0] > newsize[0] or im.size[1] > newsize[1] :
        newim = im.resize(newsize, Image.Resampling.LANCZOS)
      else:
        newim = im
      newPath = savepath + "/" + f
      newPath = newPath.replace(".png", ".jpg")
      newim.save(newPath)
      i += 1
    else:
      pass
  return i

if __name__ == "__main__":
  import sys
  if len(sys.argv) < 3:
    print("Usage: smalls.py folder savepath [size=1600]")
  elif len(sys.argv) < 4:
    small(sys.argv[1], sys.argv[2], 1600)
  else:
    size = int(sys.argv[3])
    small(sys.argv[1], sys.argv[2], size)
  print("Done")
