import sys

font = dict()
normal = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?."
reverse="ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz∀qƆpƎℲפHIſʞ˥WNOԀQɹS┴∩ΛMX⅄Z¿˙"

for i in range(len(normal)):
    font[normal[i]] = reverse[i]

txt = sys.argv[1]
out = ""
for i in range(len(txt)):
    if txt[i] in font:
        out += font[txt[i]]
    else:
        out += txt[i]

print(out[::-1])

