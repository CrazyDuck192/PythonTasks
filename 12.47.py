def check_indent(filename):
    with open(filename) as f:
        used = [(0, '')]
        lines = f.readlines()

        for line in lines:
            stripped_line = line.lstrip()
            indent = len(line) - len(stripped_line)

            if indent > used[-1][0] and used[-1][1] == '':
                print(line)
                return False
            if indent <= used[-1][0] and used[-1][1] == ':':
                print(line)
                return False
            if indent < used[-1][0]:
                while indent < used[-1][0]:
                    used.pop()
                if indent != used[-1][0]:
                    print(line)
                    return False
                if ':' == line.rstrip()[-1]:
                    used.append((indent, ':'))
                else:
                    used.append((indent, ''))
            elif ':' == line.rstrip()[-1]:
                used.append((indent, ':'))
            else:
                used.append((indent, ''))
            print(lines.index(line)+1, indent, used)
                                           
    return True 

if __name__ == '__main__':
    filename = 'exercises/12.47.txt'
    print(check_indent(filename))


        

