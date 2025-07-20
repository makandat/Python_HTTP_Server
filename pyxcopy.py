#!/usr/bin/python3
#  再帰的にファイルをコピーする。xcopy.py v1.0.1
import glob, sys, os, shutil

# コピー
def xcopy(src, dest):
  # 指定したフォルダまたはワイルドカードのファイル一覧を再帰的に取得する。
  srcp = src + "/**"
  sitems = glob.glob(srcp, recursive=True)
  for i in range(0, len(sitems)):
    sitems[i-1] = sitems[i-1].replace("\\", "/")

  # コピー先のフォルダが存在しない場合は作成する。
  if os.path.isdir(dest) == False:
    os.mkdir(dest)
    ditems = []
  else:
    # コピー先のフォルダが存在する場合、ファイル一覧を再帰的に取得する。
    destp = dest + "/**"
    ditems = glob.glob(destp, recursive=True)
    for i in range(0, len(ditems)):
      ditems[i-1] = ditems[i-1].replace("\\", "/")

  # コピー元のファイルをコピー先にコピーする。
  finished = []
  for item in sitems:
    # コピー先またはフォルダ作成先
    destp = dest + item[len(src):]
    try:
      # コピー先に同じ名前のファイルが存在するか？
      idx = ditems.index(destp)
    except:
      idx = -1
    if idx >= 0:
      # コピー先に存在する場合、コピー先がファイルかチェック
      dfile = ditems[idx]
      if os.path.isfile(dfile):
        # 日付をチェックし新しい場合は何もせず次の項目へ。
        sst = os.stat(item)
        dst = os.stat(dfile)
        if sst.st_mtime <= dst.st_mtime:
          finished.append(destp)  # コピーが終わったかスキップしたものを finished リストに追加。
        else:
          shutil.copyfile(item, destp)
          finished.append(destp)  # コピーが終わったかスキップしたものを finished リストに追加。
      else:
        # フォルダの場合はなにもしない。
        pass
    else:
      # コピー先に存在しない場合
      if os.path.isdir(item) and destp != f"{dest}/":
        # フォルダなら作成する。
        if os.path.exists(destp) == False:
          os.makedirs(destp)
      else:
        # ファイルならコピーする。
        if os.path.isfile(item):
          shutil.copyfile(item, destp)
          finished.append(destp)  # コピーが終わったかスキップしたものを finished リストに追加。
  return finished
      
  # 余分なファイルがコピー先にあるかチェックする。
  def sync_delete(dest, finished):
    items = glob.glob(dest + separator + "**", recursive=True)
    for item in finished:
      items.remove(item)  # finished に入っている項目をコピー先項目から削除
    items.remove(dest + separator)  # コピー先フォルダ自体
    if len(items) > 0:
      # コピー先にスキップもコピーもされなかったファイル
      for item in items:
        # これらのファイルを削除
        for item in items:
          if os.path.isfile(item):
            os.remove(item)
    return