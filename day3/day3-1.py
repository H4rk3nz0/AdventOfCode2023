import sys, re

lines = open(sys.argv[1]).read().split('\n')

right_nums = []

def final_check(nums,span,res,i):
    occurrence = range(span[0],span[1])
    for x in res:
        if (span[0]-1 == x[0]) or (span[1]+1 == x[1]):
            right_nums.append(int(nums[i]))
        elif (x[0] in occurrence) or (x[1] in occurrence):
            right_nums.append(int(nums[i]))

def check_line(res1, res2, res3, spans, nums):
    for i,span in enumerate(spans):
        final_check(nums,span,res1,i)
        final_check(nums,span,res2,i)
        final_check(nums,span,res3,i)

def match_line(line1, line2, line3):

    # Get span and numbers out of current Working line1
    spans = [x.span() for x in re.finditer(r'[0-9]{1,4}', line1)] 
    nums = [x.group() for x in re.finditer(r'[0-9]{1,4}', line1)]

    # Get the symbol locations 
    res1 = [x.span() for x in re.finditer(r"([^0-9.])", line1)] # Working Line
    res2 = [x.span() for x in re.finditer(r"([^0-9.])", line2)] # Line Above
    res3 = [x.span() for x in re.finditer(r"([^0-9.])", line3)]

    check_line(res1,res2,res3,spans,nums)

control = 0

while control < len(lines):
    if control == (len(lines)-1):
        line1, line2, line3 = (lines[control], lines[control-1], '.' * len(lines[control]))
        match_line(line1,line2,line3)
        break
    if  control == 0:
        line1, line2, line3 = (lines[control], '.' * len(lines[control]), lines[control+1])
        match_line(line1,line2,line3)
    else:
        line1, line2, line3 = (lines[control], lines[control-1], lines[control+1])
        match_line(line1,line2,line3)
    control+=1

print(right_nums)
print(sum(right_nums))