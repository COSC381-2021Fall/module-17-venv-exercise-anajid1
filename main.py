import pyjokes
import emoji
import numpy as np

print(pyjokes.get_joke())
print(emoji.emojize(':grinning_face_with_smiling_eyes:'))

a = np.arange(6)
a2 = a[np.newaxis, :]
print(a2.shape)