import os
from dataclasses import replace

text = "Zdvk#wkh#glvkhv$"

print("".join(chr(ord(t) - 3) for t in text))