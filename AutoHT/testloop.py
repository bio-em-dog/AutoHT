# 测试如何识别loop end
def runList(inputlist):
    listlen=len(inputlist)
    i=-1
    while i < listlen-1:
        i += 1 
        line=inputlist[i].strip().split()    # get str  and  remove \n whitespace  and  split
        if line==[]:    # skip empty line
            continue

        if line[0] == "Loop":
            last_end = listlen - inputlist[::-1].index("End\n") - 1    # last "End" line number
            #print(inputlist[i+1: last_end])
            for j in range(int(line[1])):
                runList(inputlist[i+1: last_end])
            i=last_end
        elif line[0][0]=="#":
            continue
        else:
            print(line)


with open("loop",'r') as f:
    runList(f.readlines())