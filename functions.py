def unichrWord(word):
    return [unichr(ord(i)) for i in word]

def ordWord(word):
    return [str(ord(i)) for i in word]

def unichrOrd(ord_list):
    return [unichr(i) for i in ord_list]
