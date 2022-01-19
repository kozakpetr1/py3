alphabet = {
    "A" : "Z", "B" : "J", "C" : "A", "D" : "R", "E" : "S", "F" : "T", "G" : "E", "H" : "O", "I" : "K", "J" : "N",
    "K" : "P", "L" : "X", "M" : "G", "N" : "M", "O" : "B", "P" : "I", "Q" : "D", "R" : "U", "S" : "Q", "T" : "L",
    "U" : "V", "V" : "W", "W" : "F", "X" : "Y", "Y" : "C", "Z" : "H",
}

oText = "SIFROVANITEXTUJAKOUKZAZKAPOUZITISLOVNIKU"
sText = ""
o2Text = ""

print("OT: " + oText)

for val in oText:
    sText += alphabet[val]

for val in sText:
    key = [k for k, v in alphabet.items() if v == val]
    o2Text += key[0]

print("ST: " + sText)
print("OT: " + o2Text)