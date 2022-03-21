""" module to parse the markdown """ # add the module doc string
import re


def parse(markdown: str):
    """ parse the markdown """ # add the class doc string
    lines = markdown.splitlines() # change split('\n') to splitlines()
    res = ''
    in_list = False
    in_list_append = False
    for i in lines:
        if re.match('###### (.*)', i) is not None:
            i = '<h6>' + i[7:] + '</h6>'
        elif re.match('##### (.*)', i) is not None:
            i = '<h5>' + i[6:] + '</h5>'
        elif re.match('#### (.*)', i) is not None:
            i = '<h4>' + i[5:] + '</h4>'
        elif re.match('### (.*)', i) is not None:
            i = '<h3>' + i[4:] + '</h3>'
        elif re.match('## (.*)', i) is not None:
            i = '<h2>' + i[3:] + '</h2>'
        elif re.match('# (.*)', i) is not None:
            i = '<h1>' + i[2:] + '</h1>'
        mark = re.match(r'\* (.*)', i)
        if mark:
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                curr = mark.group(1)
                mark1 = re.match('(.*)__(.*)__(.*)', curr)
                if mark1:
                    curr = mark1.group(1) + '<strong>' + \
                        mark1.group(2) + '</strong>' + mark1.group(3)
                    is_bold = True
                mark1 = re.match('(.*)_(.*)_(.*)', curr)
                if mark1:
                    curr = mark1.group(1) + '<em>' + mark1.group(2) + \
                        '</em>' + mark1.group(3)
                    is_italic = True
                i = '<ul><li>' + curr + '</li>'
            else:
                is_bold = False
                is_italic = False
                curr = mark.group(1)
                mark1 = re.match('(.*)__(.*)__(.*)', curr)
                if mark1:
                    is_bold = True
                mark1 = re.match('(.*)_(.*)_(.*)', curr)
                if mark1:
                    is_italic = True
                if is_bold:
                    curr = mark1.group(1) + '<strong>' + \
                        mark1.group(2) + '</strong>' + mark1.group(3)
                if is_italic:
                    curr = mark1.group(1) + '<em>' + mark1.group(2) + \
                        '</em>' + mark1.group(3)
                i = '<li>' + curr + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        mark = re.match('<h|<ul|<p|<li', i)
        if not mark:
            i = '<p>' + i + '</p>'
        mark = re.match('(.*)__(.*)__(.*)', i)
        if mark:
            i = mark.group(1) + '<strong>' + mark.group(2) + '</strong>' + mark.group(3)
        mark = re.match('(.*)_(.*)_(.*)', i)
        if mark:
            i = mark.group(1) + '<em>' + mark.group(2) + '</em>' + mark.group(3)
        if in_list_append:
            i = '</ul>' + i
            in_list_append = False
        res += i
    if in_list:
        res += '</ul>'
    return res
