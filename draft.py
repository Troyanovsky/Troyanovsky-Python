import PIL
import PIL.Image
import numpy as np

def processImg(img):
    color = PIL.Image.open(img)
    gray = color.convert('L')
    bw = gray.point(lambda x: 0 if x<128 else 255, '1') #conver into b/w img
    width,height = bw.size
    #conver image into list expression
    lst = list(bw.getdata())
    lst = [lst[i:i+width] for i in range(0, len(lst), width)]
    #identify the start of each row of pixel, calculate the average start point 
    # to get the indentation level of the line
    indent,currentBlock,blankLines = [],[],0
    for i in range(len(lst)):
        try:
            currentBlock.append(lst[i].index(0))
            blankLines = 0
        except:
            blankLines += 1
        if blankLines > 4 and len(currentBlock) > 5:
            indent.append(calculateIndentation(currentBlock))
            blankLines,currentBlock = 0,[]
    bw.save("ocrTemp.jpg")
    return indent

def calculateIndentation(currentBlock):
    stdDev = np.std(currentBlock)
    mean = np.mean(currentBlock)
    processedBlock = []
    #delete the outliers
    for n in currentBlock:
        if abs(n - mean) <= stdDev:
            processedBlock.append(n)
    #calculate the indentation level
    return (sum(processedBlock)//len(processedBlock))//10*10

def percentile(data, percentile):
    size = len(data)
    return data[int(math.ceil((size * percentile) / 100)) - 1]

