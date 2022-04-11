from textooo import Texto as T


myText = T("What about you?")
print(myText.getS())
myText.replaS("What", "How")
print(myText.getS())