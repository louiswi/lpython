#!/usr/bin/python
import xml.sax.saxutils
import sys
def main():
    maxwidth,format = process_options()
    if maxwidth is not None:
        print_start()
        count = 0
        while True:
            try:
                line = input()
                if count == 0:
                    color = "lightgreen"
                elif count % 2:
                    color = 'white'
                else:
                    color = 'lightyellow'
                print_line(line,color,maxwidth,format)
                count += 1
            except EOFError:
                break
        print_end()

def print_start():
    print("<table border='1'>")

def print_end():
    print("</table>")

def print_line(line,color,maxwidth,format):
    print("<tr bgcolor='{0}'>".format(color))
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",","")
            try:
                x = float(number)
                print("<td align='right'>{0:{1}}</td>".format(x,format))
            except ValueError:
                field = field.title()
                field = field.replace("And","and")
                if len(field) <= maxwidth:
                    field = xml.sax.saxutils.escape(field)
                else:
                    field = "{0}...".format(xml.sax.saxutils.escape(field[:maxwidth]))
                print("<td>{0}</td>".format(field))
    print("</tr>")
def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in '\' "':
            if quote is None:    #quote start
                quote = c
            elif quote == c:    # quote end
                quote = None
            else:
                field += c  #other quote insiude quoted string
            continue
        if quote is None and c == ',':  #end of a field 
            fields.append(field)
            field = ""
        else:
            field += c
    if field:
        fields.append(field)     #add the last field 
    return fields
def process_options():
    format = '.0f'
    maxwidth = 100
    maxwidth_arg = 'maxwidth='
    format_arg = 'format='
    for arg in sys.argv[1:]:
        if arg in ['-h','--help']:
            print("""\
                    usage:
                    csv2html.py [maxwidth=int] [format=str] < infile.csv >
                    outfile.html

                    maxwidth is an optional integer; if specified, it sets the
                    maximum
                    number of characters that can be output for string fields,
                    otherwise a default of {0} characters is used.

                    format is the format to use for numbers; if not specified
                    it
                    defaults to "{1}".""".format(maxwidth, format))
            return None,None
        elif arg.startswith(maxwidth_arg):
            try:
                maxwidth = int(arg[len(maxwidth_arg):])
            except ValueError:
                pass
        elif arg.startswith(format_arg):
            format = arg[len(format_arg):]
    return maxwidth,format


                       
            


main()
main
