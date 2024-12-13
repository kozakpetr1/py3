kriteria_oci_10 = ["modré", "zelené", "tyrkysové"]
kriteria_oci_9 = ["hnědé", "černé", "růžové"]

kriteria_vlasy_10 = ["blond", "zrzavé"]
kriteria_vlasy_9 = ["hnědé", "kaštanové"]

oci = "modré"
vlasy = "hnědé"

# kriteria_oci_10 a kriteria_vlasy_10 --> jdu na rande
# kriteria_oci_10 a kriteria_vlasy_9 --> jdu na rande s podmínkou
# kriteria_oci_9 a kriteria_vlasy_10 --> jdu na rande s podmínkou
# kriteria_oci_9 a kriteria_vlasy_9 --> hodně váhám
# pouze jedno, nebo ani jedno --> nikam nejdu

if oci in kriteria_oci_10:
    if vlasy in kriteria_vlasy_10:
        print("Jdu na rande.")
    elif vlasy in kriteria_vlasy_9:
        print("Jdu na rande s podmínkou.")
    else:
        print("Nikam nejdu.")
elif oci in kriteria_oci_9:
    if vlasy in kriteria_vlasy_10:
        print("Jdu na rande s podmínkou.")
    elif vlasy in kriteria_vlasy_9:
        print("Hodně váhám.")
    else:
        print("Nikam nejdu.")
else:
    print("Nikam nejdu.")
    