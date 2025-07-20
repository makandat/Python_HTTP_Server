#!/usr/bin/python3
import os, shutil
from dataclasses import replace

#  pixiv_rename.py ver. 3.0
#    2.2 3桁の数字にも対応
#    2.3 3桁の数字にも対応時のバグ修正
#    2.4 バグ修正
#    3.0 100077085_p0.jpg のように番号が９桁になったので、古いファイルの番号を０を追加して９桁にするようにした。

# 指定されたフォルダの画像ファイルを同じ長さにリネームする。
def rename_files(folder) :
  # 画像ファイル一覧を得る。
  files = os.listdir(folder)
  # 画像ファイルをリネーム
  count = 0
  for fname in files :
    flag = False # 二重リネーム防止
    fpath = folder + "/" + fname.replace("\\", "/")
    ext = os.path.splitext(fpath)[1].lower()
    # 画像ファイルのみを対象にする。
    if ext == ".jpg" or ext == ".png" or ext == ".gif" :
      # ファイル名の '_' より前の長さが 9 桁未満なら 9 桁にする。
      fnpart = fname.split('_')[0]
      naz = 9 - len(fnpart)
      newfname = os.path.dirname(fpath) + "/" + naz * '0' + fname
      ff = fname.split("_")
      try:
        if not (ext in ff[1]) :
          ff[1] += ext
      except:
         pass
      if len(ff) == 3 :
        # 3分割できて 'master' が含まれる場合は 'master..' 部分を削除する。
        fname_old = fname
        fname = ff[0] + '_' + ff[1]
      elif len(ff) != 2 :
        # _ で2分割できない場合(ファイル名の形式が異なる場合)はスキップする。
        continue
      elif newfname != fpath:
        if len(ff) == 2 and len(ff[1]) == 6:
          newfname = newfname.replace("_" + ff[1], "_" + "p0" + ff[1][1:])
        shutil.move(fpath, newfname)
        count += 1
        flag = True
      else :
        # その他の場合は何もしない。(2分割できた場合)
        pass
      # 連続番号部分の形式を確認する。
      sf = ff[1]
      if flag == False and ff[1].startswith('p') :
        if len(ff[1]) == 6 or (len(ff) == 3 and len(ff[1]) == 2) :
          # 連続番号が1桁の場合
          sf = "p0" + ff[1][1:]
          newname = folder.replace("\\", "/") + "/" + '0' * naz + ff[0] + "_" + sf
          shutil.move(fpath, newname)
          count += 1
        elif len(ff) == 3 and len(ff[1]) == 7 :
          # _master1200 があり連続番号が2桁の場合
          newname = folder + "/" + fname
          shutil.move(fpath, newname)
          count += 1
        elif len(ff[1]) == 8 or (len(ff) == 3 and len(ff[1]) == 4) :
          # 連続番号が3桁または連続番号が3桁かつ _master1200 がある場合
          sn = ff[1][1:2]
          if sn == '1' :
            # 連続番号が3桁かつ100番台の場合
            sf = "q" + ff[1][2:4]
            newname = folder + "/" + ff[0] + "_" + sf + ext
            shutil.move(fpath, newname)
            count += 1
          elif sn == '2' :
            # 連続番号が3桁かつ200番台の場合
            sf = "r" + ff[1][2:4]
            newname = folder + "/" + ff[0] + "_" + sf + ext
            shutil.move(fpath, newname)
            count += 1
          else :
            pass
        else :
          pass
    else :
      pass
  return count

if __name__ == "__main__":
  import sys
  if len(sys.argv) > 1:
    rename_files(sys.argv[1])
    print("Done.")
  else:
    print("Specify the folder.")