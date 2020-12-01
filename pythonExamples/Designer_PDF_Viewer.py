h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
word = 'abc'

def designerPdfViewer(h, word):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    # Create a dictionary fro key value, where value is high form h
    myDic = {v:h[k] for k, v in enumerate(abc)}
    
    wLen = len(word)
    if wLen == 0:
        return 0
    maxC = 0
    for c in word:
        if myDic[c] > maxC:
            maxC = myDic[c]
    return maxC*wLen

designerPdfViewer(h, word)
