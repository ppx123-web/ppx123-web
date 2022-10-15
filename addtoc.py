import sys
import os,fnmatch
import subprocess, time, re

pattern = re.compile(r"^(?P<p1>#+ +)(?P<p2>.+)\n$")
pattern_use = re.compile(r"^(#+ +)\<span.*\>(?P<p3>.+)\</span\>\n$")
pattern_head = r"(---[\s\S]*---[\n]+(\>[^\n]*\n)*)"
pattern_toc = re.compile(r"^[-* \t]+ +\[(?P<p4>.+)\]\(#head[0-9]+\)\n$")
head_sign = re.compile(r"^---\n$")
directory = "writing"
global cnt
cnt = 0
## <span id="head1">运算符()重载与仿函数</span>

def countsharp(head):
    ans = "";
    for ch in head:
        if ch == '#':
            ans += '\t'
        else: break
    return ans[2:]

def addtoc(line):
    global cnt
    cnt = cnt + 1
    match = pattern.match(line)
    toc_text = f"- [{match.group(2)}](#head{cnt})\n"
    new_text = f"{match.group(1)}<span id="+ f"\"head{cnt}\"" + f">{match.group(2)}</span>\n"
    # header = re.sub(pattern, line, new_text)
    # toc = pattern.sub(line, toc_text)
    return [new_text,toc_text]

def modify(file):
    global cnt
    cnt = 0
    filedata = ""
    toc = ""
    with open(f"./{directory}/{file}","r+",encoding="utf8") as f:
        for line in f.readlines():
            if len(pattern_toc.findall(line)) > 0:
                # 当匹配到一条toc时，跳过
                continue;
            elif len(pattern_use.findall(line)) > 0:
                cnt += 1
                filedata += line
                match = pattern_use.match(line).group(2)
                toc += countsharp(line) + f"- [{match}](#head{cnt})\n"
                # 当匹配到一条处理好的header时，创建一条toc
            elif len(pattern.findall(line)) > 0:
                [newline, newtoc] = addtoc(line)
                toc += countsharp(line) + newtoc
                filedata += newline
            else:
                filedata += line
    headcnt = 0
    with open(f"./_posts/{file}","w",encoding="utf-8") as f:
        match = re.match(pattern_head, filedata,re.S | re.M)
        f.write(match.group(1)+'\n')
        f.write(toc + '\n')
        f.write(filedata[len(match.group(1)):])

if __name__=='__main__':
    filenames = []
    print("处理writing文件夹中文件输出到_post")
    if len(sys.argv) == 1:
        filedir = os.listdir(directory)
        for name in filedir:
            if fnmatch.fnmatch(name, "*.md"):
                filenames.append(name)
    else:
        if sys.argv[1] == "bak":
            print("备份到bak文件夹")
            subprocess.call(r"cp ./backup/*.md ./bak/",shell=True)
        for u in range(1,len(sys.argv)):
            filenames.append(sys.argv[u])
    print(f"处理的文件有:{filenames}")
    # input('按回车以确认...')
    for file in filenames:
        modify(os.path.basename(file))
