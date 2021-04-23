
from indicnlp.syllable import syllabifier

w='अनुच्छेद'

lang='hi'

print(''.join(syllabifier.orthographic_syllabify(w,lang)))