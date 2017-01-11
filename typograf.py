import re

NON_BREAKING_SPACE = '\u00A0'
NON_BREAKING_HYPHEN = '\u2011'
rules = (
    # replace hyphens to dashes
    (r'(?<= )-(?= )', r'—'),
    # replace dashes to hyphens in phone number
    (r'(?<=\d)—(?=\d)', r'-'),
    # replace quotes ' or " to «»
    (r'([\'"])(.*?)(\1)', r'«\2»'),
    # remove unnecessary line breaks
    (r'\r\n', r'\n'),
    (r'\n{2,}', r'\n'),
    (r'\n[ ]+\n', r'\n'),
    (r'\s+$', r''),
    # remove unnecessary spaces
    (r'[ \t]{2,}', r' '),
    (r'[ \t]+\n', r'\n'),
    # non-breaking hyphen between the number and the abbreviation
    (r'(\d+)(-?)([а-яА-Яa-zA-Z])', r'\1{}\3'.format(NON_BREAKING_HYPHEN)),
    # non-breaking space between the number and word
    (r'(\d+)( )+([а-яА-Яa-zA-Z])', r'\1{}\3'.format(NON_BREAKING_SPACE)),
    # non-breaking space between the short-word and word
    (r'(\b[а-яА-Яa-zA-Z]{1,3})( +)(\b[а-яА-Яa-zA-Z]+)', r'\1{}\3'
     .format(NON_BREAKING_SPACE)),
)


def typograf(text):
    for pattern, replace in rules:
        text = re.sub(pattern, replace, text)
    return text
