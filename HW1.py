from nltk import pos_tag
from nltk import word_tokenize
from nltk import bigrams

def compareWordTypes(text1,text2,norm):
    token1 = word_tokenize(text1)
    token2 = word_tokenize(text2)
    pos1 = pos_tag(token1)
    pos2 = pos_tag(token2)
    count=0                 
    for i in pos1:
        for j in pos2:
            if i==j :
                count+=1
                break
    if norm == "N":
        return count
    elif norm == "Y":
        return count/((len(token1)+len(token2))/2)

def compareBigramTypes(text1,text2,norm):
    token1 = word_tokenize(text1.strip())
    token2 = word_tokenize(text2.strip())
    pos1 = pos_tag(token1)
    pos2 = pos_tag(token2)
    count=0
    for i in bigrams(pos1):
        for j in bigrams(pos2):
            if i==j:
                count+=1
                break
    if norm == "N":
        return count
    elif norm == "Y":
        return count/((len(text1)+len(text2))/2)

def plagiarismDetector(file1, file2, type, norm, threshold):
    f1=open(file1,'r')
    f2=open(file2,'r')
    text1= f1.read()
    text2= f2.read()
    div=word_tokenize(text1.strip())
    if type == "U":
        prob = compareWordTypes(text1,text2,norm)
    elif type == "B":
        prob = compareBigramTypes(text1,text2,norm)
    if norm == "N" :
        prob/=len(div)
    print("The probability of plagiarizm is: ",prob)
    if prob <= threshold :
        print("The contents are not plagiarized")
    else:
        print("The contents are plagiarized")