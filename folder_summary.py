# folders_summary.py: 指定したフォルダとそのサブフォルダのファイルの数、サイズの合計、最古と最新のファイルの日付を表示する。
import glob, os, sys, datetime as dt

# 再帰的にサブディレクトリ一覧を得る。
def getSubDirs(folder):
  folder1 = folder + "/**/"
  dirs = glob.glob(folder1, recursive=True)
  return dirs

# タイムスタンプを日付文字列に変換する。
def timeString(time):
  try:
    d = dt.datetime.fromtimestamp(time)
  except:
    return ""
  return d.strftime("%Y/%m/%d %H:%M:%S")
  
# 指定したディレクトリ内のファイル数、ファイルサイズの合計、最古と最新のファイルの日付を返す。
def folderSummary(folder):
  count = 0
  size = 0
  oldest = None
  last = None
  folder1 = folder + "/**"
  for f in glob.glob(folder1):
    count += 1
    size += os.path.getsize(f)
    st = os.stat(f)
    if oldest is None:
      oldest = st.st_mtime
    if last is None:
      last = st.st_mtime
    if oldest > st.st_mtime:
      oldest = st.st_mtime
    if last < st.st_mtime:
      last = st.st_mtime
  return (count, size, oldest, last)

# 指定したフォルダのサブフォルダの要約を得る。
def getSummary(folder):
  summary = list()
  subdirs = getSubDirs(folder)
  for p in subdirs:
    path = p.replace("\\", "/")
    a = folderSummary(p)
    count = a[0]
    size = "{:,}".format(a[1])
    oldest = timeString(a[2])
    last = timeString(a[3])
    summary.append((path, count, size, oldest, last))
  return summary    


# main
if __name__ == "__main__":
  if len(sys.argv) == 1:
    print("コマンドパラメータにフォルダを指定してください。\n")
    exit(1)
  folder = sys.argv[1]
  if not os.path.isdir(folder):
    print("フォルダが存在しないか、正しくありません。\n")
    exit(1)
  subdirs = getSubDirs(folder)
  for p in subdirs:
    path = folder + p
    a = folderSummary(p)
    count = a[0]
    size = a[1]
    try:
      oldest = timeString(a[2])
      last = timeString(a[3])
      print(path, count, size, oldest, last)
    except:
      print(path)
  print("終わり。")
