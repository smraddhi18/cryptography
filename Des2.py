from math import perm


def padToX(binaryNum, X):
    while len(binaryNum) < X:
        binaryNum = '0' + binaryNum
    return binaryNum

def splitBitByN(bits, step):
    bitSplits = []
    for i in range(len(bits)//step):
        bitSplits.append(bits[(i * step):((i+1) * step)])
    return bitSplits

def makeReadable(bits, step):
    readableBit = ""
    count = 1
    for i in bits:
        if count % step == 1:
            readableBit += f' {i}'
        else:
            readableBit += i
        count += 1
    return readableBit[1:]

#main functions
def createSubkeys(originalKey):
    PC1 = [57, 49, 41, 33, 25, 17, 9,
           1, 58, 50, 42, 34, 26, 18,
           10, 2, 59, 51, 43, 35, 27,
           19, 11, 3, 60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15,
           7, 62, 54, 46, 38, 30, 22,
           14, 6, 61, 53, 45, 37, 29,
           21, 13, 5, 28, 20, 12, 4]

    perm56 = "" 
    for i in range(len(PC1)):
        perm56 += originalKey[PC1[i]-1]

    currentC = perm56[:28] 
    currentD = perm56[28:] 
    concatenatedPairs = []
    numOfLeftShifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    for i in numOfLeftShifts:
        currentC = currentC[i:] + currentC[:i]
        currentD = currentD[i:] + currentD[:i]
        concatenatedPairs.append(currentC + currentD)

    PC2 =[14,  17,  11,  24,  1,  5, 
          3,  28,  15,  6,  21,  10,  
          23,  19,  12,  4,  26,  8,  
          16,   7,  27,  20,  13,  2,  
          41,  52,  31,  37,  47,  55,  
          30,  40,  51,  45,  33,  48,  
          44,  49,  39,  56,  34,  53,  
          46,  42,  50,  36,  29,  32]

    keys = []
    for currentCandD in concatenatedPairs: 
        perm48 = ""
        for i in range(len(PC2)):
            perm48 += currentCandD[PC2[i]-1]
        keys.append(perm48)
    
    return keys

def SBoxes(bitSplit, Snum):

    bitsShrink6To4 = []
    S1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
          [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8], 
          [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0], 
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

    S2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10], 
          [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5], 
          [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15], 
          [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

    S3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8], 
          [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1], 
          [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7], 
          [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]

    S4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15], 
          [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9], 
          [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4], 
          [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]

    S5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9], 
          [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6], 
          [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14], 
          [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]

    S6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11], 
          [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8], 
          [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6], 
          [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]

    S7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1], 
          [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6], 
          [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2], 
          [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]

    S8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7], 
          [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2], 
          [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8], 
          [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

    SMap = {1 : S1,
        2: S2,
        3: S3,
        4: S4,
        5: S5,
        6: S6,
        7: S7,
        8: S8
        }

    S = SMap[Snum]

    row = int((bitSplit[0] + bitSplit[5]), 2)
    column = int(bitSplit[1:5], 2)
    
    return padToX(bin(S[row][column])[2:], 4)

def XORBinaryStrings(string1, string2):

    if (len(string1) != len(string2)):
        raise "Strings must be of equal length to XOR"
    xorOutput = ""
    xorMap = {
    ('0', '0'): '0', ('0', '1'): '1', ('1', '0'): '1', ('1', '1'): '0'
    }
    for bit in range(len(string1)):
        xorOutput += xorMap[(f'{string1[bit]}', f'{string2[bit]}')]
    return xorOutput
    
def fFunction(right, keyN):

    expansionTable = [32, 1, 2, 3, 4, 5,
                      4, 5, 6, 7, 8, 9,
                      8, 9, 10, 11, 12, 13,
                      12, 13, 14, 15, 16, 17,
                      16, 17, 18, 19, 20, 21,
                      20, 21, 22, 23, 24, 25,
                      24, 25, 26, 27, 28, 29,
                      28, 29, 30, 31, 32, 1]
    expansionOfRight = ""
    for i in range(len(expansionTable)):
        expansionOfRight += right[expansionTable[i]-1]
    
    xorMap = {
        ('0', '0'): '0', ('0', '1'): '1', ('1', '0'): '1', ('1', '1'): '0'
        }
    XORExpansionAndKey = ""
    for bit in range(len(keyN)):

        XORExpansionAndKey += xorMap[(f'{keyN[bit]}', f'{expansionOfRight[bit]}')]

    bitSplits = splitBitByN(XORExpansionAndKey, 6)
   

    shrink48to32 = "" 
    for i in range(len(bitSplits)):
        shrink48to32 += SBoxes(bitSplits[i], i+1)
    
    P = [16, 7, 20, 21,
        29, 12, 28, 17,
         1, 15, 23, 26,
         5, 18, 31, 10,
          2, 8, 24, 14,
          32, 27, 3, 9,
         19, 13, 30, 6,
         22, 11, 4, 25]

    permutatedSBoxes = ""
    for i in range((len(P))):
        permutatedSBoxes += shrink48to32[P[i]-1]

    return permutatedSBoxes

def encodeData(plainText, key):

    plainText = padToX(bin(int(plainText, 16))[2:], 64)
    key = padToX(bin(int(key, 16))[2:], 64)
    keys = createSubkeys(key) 
    #Initial Permutation
    mPermutated = ""
    IP = [58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6,
          64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17,  9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7]
    for i in range(len(IP)):
        mPermutated += plainText[IP[i]-1]

    left = mPermutated[:32] 
    right = mPermutated[32:] 
    
    for i in range(16):
        rightBefore = right
        leftBefore = left
        right = XORBinaryStrings(leftBefore, fFunction(rightBefore, keys[i]))
        left = rightBefore
    R16permL16 = right + left

    IPInverse = [40, 8, 48, 16, 56, 24, 64, 32,
                 39, 7, 47, 15, 55, 23, 63, 31,
                 38, 6, 46, 14, 54, 22, 62, 30,
                 37, 5, 45, 13, 53, 21, 61, 29,
                 36, 4, 44, 12, 52, 20, 60, 28,
                 35, 3, 43, 11, 51, 19, 59, 27,
                 34, 2, 42, 10, 50, 18, 58, 26,
                 33, 1, 41,  9, 49, 17, 57, 25]
    finalPermutation = ""
    for i in range(len(IPInverse)):
        finalPermutation += R16permL16[IPInverse[i]-1]
    
    return hex(int(finalPermutation, 2))


def main():
    
    plainText = input("Enter a hexadecimal plain text message: ")
    key = input("Enter a hexadecimal key: ")
    print("Encrypted output using DES Encryption:", encodeData(plainText, key))
    
if __name__ == "__main__":
    main()