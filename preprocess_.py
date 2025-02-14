import re
import pandas as pd

char_mappings = {
"٥": "5",
"ڈ": "د",
"ڇ": "چ",
# Persian numbers (will be replaced by english one)
"۰": "0",
"۱": "1",
"۲": "2",
"۳": "3",
"۴": "4",
"۵": "5",
"۶": "6",
"۷": "7",
"۸": "8",
"۹": "9",
".": ".",
# Arabic numbers (will be replaced by english one)
"٠": "0",
"١": "1",
"٢": "2",
"٣": "3",
"٤": "4",
"٥": "5",
"٦": "6",
"٧": "7",
"٨": "8",
"٩": "9",
# Special Arabic Characters (will be replaced by persian one)
"ك": "ک",
"ى": "ی",
"ي": "ی",
"ؤ": "و",
"ئ": "ی",
"إ": "ا",
"أ": "ا",
"آ": "آ",
"ة": "ه",
"ء": "ی",
# Arabic Presentation Forms-A (will be replaced by persian one)
"ﭐ": "ا",
"ﭑ": "ا",
"ﭖ": "پ",
"ﭗ": "پ",
"ﭘ": "پ",
"ﭙ": "پ",
"ﭞ": "ت",
"ﭟ": "ت",
"ﭠ": "ت",
"ﭡ": "ت",
"ﭺ": "چ",
"ﭻ": "چ",
"ﭼ": "چ",
"ﭽ": "چ",
"ﮊ": "ژ",
"ﮋ": "ژ",
"ﮎ": "ک",
"ﮏ": "ک",
"ﮐ": "ک",
"ﮑ": "ک",
"ﮒ": "گ",
"ﮓ": "گ",
"ﮔ": "گ",
"ﮕ": "گ",
"ﮤ": "ه",
"ﮥ": "ه",
"ﮦ": "ه",
"ﮪ": "ه",
"ﮫ": "ه",
"ﮬ": "ه",
"ﮭ": "ه",
"ﮮ": "ی",
"ﮯ": "ی",
"ﮰ": "ی",
"ﮱ": "ی",
"ﯼ": "ی",
"ﯽ": "ی",
"ﯾ": "ی",
"ﯿ": "ی",
# Arabic Presentation Forms-B (will be replaced by persian one)
"ﺀ": "ی",
"ﺁ": "آ",
"ﺂ": "ا",
"ﺃ": "ا",
"ﺄ": "ا",
"ﺅ": "و",
"ﺆ": "و",
"ﺇ": "ا",
"ﺈ": "ا",
"ﺉ": "ی",
"ﺊ": "ی",
"ﺋ": "ی",
"ﺌ": "ی",
"ﺍ": "ا",
"ﺎ": "ا",
"ﺏ": "ب",
"ﺐ": "ب",
"ﺑ": "ب",
"ﺒ": "ب",
"ﺓ": "ه",
"ﺔ": "ه",
"ﺕ": "ت",
"ﺖ": "ت",
"ﺗ": "ت",
"ﺘ": "ت",
"ﺙ": "ث",
"ﺚ": "ث",
"ﺛ": "ث",
"ﺜ": "ث",
"ﺝ": "ج",
"ﺞ": "ج",
"ﺟ": "ج",
"ﺠ": "ج",
"ﺡ": "ح",
"ﺢ": "ح",
"ﺣ": "ح",
"ﺤ": "ح",
"ﺥ": "خ",
"ﺦ": "خ",
"ﺧ": "خ",
"ﺨ": "خ",
"ﺩ": "د",
"ﺪ": "د",
"ﺫ": "ذ",
"ﺬ": "ذ",
"ﺭ": "ر",
"ﺮ": "ر",
"ﺯ": "ز",
"ﺰ": "ز",
"ﺱ": "س",
"ﺲ": "س",
"ﺳ": "س",
"ﺴ": "س",
"ﺵ": "ش",
"ﺶ": "ش",
"ﺷ": "ش",
"ﺸ": "ش",
"ﺹ": "ص",
"ﺺ": "ص",
"ﺻ": "ص",
"ﺼ": "ص",
"ﺽ": "ض",
"ﺾ": "ض",
"ﺿ": "ض",
"ﻀ": "ض",
"ﻁ": "ط",
"ﻂ": "ط",
"ﻃ": "ط",
"ﻄ": "ط",
"ﻅ": "ظ",
"ﻆ": "ظ",
"ﻇ": "ظ",
"ﻈ": "ظ",
"ﻉ": "ع",
"ﻊ": "ع",
"ﻋ": "ع",
"ﻌ": "ع",
"ﻍ": "غ",
"ﻎ": "غ",
"ﻏ": "غ",
"ﻐ": "غ",
"ﻑ": "ف",
"ﻒ": "ف",
"ﻓ": "ف",
"ﻔ": "ف",
"ﻕ": "ق",
"ﻖ": "ق",
"ﻗ": "ق",
"ﻘ": "ق",
"ﻙ": "ک",
"ﻚ": "ک",
"ﻛ": "ک",
"ﻜ": "ک",
"ﻝ": "ل",
"ﻞ": "ل",
"ﻟ": "ل",
"ﻠ": "ل",
"ﻡ": "م",
"ﻢ": "م",
"ﻣ": "م",
"ﻤ": "م",
"ﻥ": "ن",
"ﻦ": "ن",
"ﻧ": "ن",
"ﻨ": "ن",
"ﻩ": "ه",
"ﻪ": "ه",
"ﻫ": "ه",
"ﻬ": "ه",
"ﻭ": "و",
"ﻮ": "و",
"ﻯ": "ی",
"ﻰ": "ی",
"ﻱ": "ی",
"ﻲ": "ی",
"ﻳ": "ی",
"ﻴ": "ی",
"ﻵ": "لا",
"ﻶ": "لا",
"ﻷ": "لا",
"ﻸ": "لا",
"ﻹ": "لا",
"ﻺ": "لا",
"ﻻ": "لا",
"ﻼ": "لا",
}
class preprocess:

    def tlt(cls,intab,txt):
        return txt.translate({ord(k):v for k,v, in zip(intab,outtab)})
    def clean(self,text):
        
        intab='۱۲۳۴۵۶۷۸۹۰١٢٣٤٥٦٧٨٩٠'
        outtab='12345678901234567890'
        translation_table = str.maketrans(intab, outtab)
        text = text.translate(translation_table)
        text = re.findall(r"[\dA-Za-z._]+|[^\dA-Za-z\W]+",text,re.UNICODE)
        text = ' '.join(word for word in text)
        
        text = re.sub(r"(\d{2})+\s?(\d{2})+\s?(\d{2})",r'date = \1-\2-\3',text)
        text = re.sub(r"(\d{2})+\s?(\d{2})",r'time = \1-\2',text)
        
        text = re.sub(r"""(\d{2})+\s?([\u0600-\u06FF])+\s?(\d{3})+\s?([\u0600-\u06FF])+\s?(\d{2})""",r' ',text)
        text = re.sub(r"""(\d{2})+\s?([\u0600-\u06FF])+\s?(\d{3})+\s?(\d{2})""",r' ',text)
        text = re.sub(r"""(\d{2})+\s?([\u0600-\u06FF])+\s?(\d{2})+\s?(\d{3})""",r' ',text)
        text = re.sub(r"""(\d{2})+\s?([\u0600-\u06FF])+\s?(\d{3})+\s?(\d{3})""",r' ',text)
        text = re.sub(r"""(\d{2})+\s?(\d{2})+\s?([\u0600-\u06FF])+\s?(\d{3})""",r' ',text)
        text = re.sub(r"""(\d{2})+\s?([\u0600-\u06FF])+\s?(\d{2})""",r' ',text)
        text = re.sub(r"""(\d{3})+\s?([\u0600-\u06FF])+\s?(\d{2})""",r' ',text)
        text = re.sub(r"""(\d{2})+\s?([\u0600-\u06FF])+\s?(\d{3})""",r' ',text)
        text = re.sub(r"""(\d{2})+\s?([\u0600-\u06FF])+\s?(\d{3})""",r' ',text)
        text = re.sub(r"""(\d{2})+\s?(\d{3})""",r' ',text)
        
        text = re.findall(r"\w+|[^\w\s]", text, re.UNICODE)
        text = ' '.join(word for word in text)

        text = re.sub("[0-9]{6,}","##",text)

        text = re.sub(r"[0-9]+\s*[\w]{,6}\s*[0-9]+\s*[\w]*\s*[0-9]+", " ",text ).strip()
        text = re.sub("\d+[\/]\d+[\/]\d+"," ",text)
        text = re.sub("\d+:\d+"," ",text)


        text = "".join([char_mappings[xx] if xx in char_mappings else xx for xx in text])
        text = re.sub(r"\s+", " ", text)  # remove more than one white spaces with space
        text = re.sub("^\." , " " , text)
        text = re.sub("\d+", " " , text)
        text = re.sub("\." , " " , text)
        text = re.sub("[\+\-\–\*\/\#\$\%\^\(\)\<\>|,\[\]\{\}«»《》?:]","",text)
        text = re.sub("[َُِّ]","",text)
    
        text = re.sub(r"[" + 'ّ'  + 'ٌ' + 'ـ' + 'َ' + 'ِ' + 'ٕ'  + 'ٍ' + 'ُ' + 'ْ' + "]", '', text)
        text = re.sub(r"-", '', text)


        
        
        
        text = re.sub('\r?\n','.',text)
        text = re.sub(r"-{3}",'',text)
        text = re.sub(r"-{2}",'',text)
        text = re.sub(r"""\s*\.{3,}""",u'.',text)
        text = re.sub(r"""\s*\.{2,}""",u'.',text)
        text = re.sub(r"""\s+(ن؟می)\s+""",r'\1',text)
        text = re.sub(r"""(!){2,}""",r'\1',text)
        text = re.sub(r"""(/ ){2,}""",'',text)
        text = re.sub(r"""( /){2,}""",'',text)
        text = re.sub(r"""(//){2,}""",'',text)
        text = re.sub(r"""(/){2,}""",'',text)
        text = re.sub(r"""(؟){2,}""",r'\1',text)
        text = re.sub(r"""_+""","",text)
        text = re.sub(r"""[ ]+""",r' ',text)
        text = re.sub(r"""([\n]+)[\t]*""",r'\1',text)
        text = re.sub(r"([0-9]+(\.[0-9]+)?)", r" \1 ",text).strip()
        text = re.sub("[0-9]{6,}","##",text)
        text = re.sub("  "," ",text)
        text = text.strip()
        return text
    
    
     