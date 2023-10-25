import sys


def longestRun(input):
    if not input == '':
        chars = {}
        for idx, c in enumerate(str(input)):
            if not c in chars.keys():
                chars.update({str(c):1})
            else:
                if idx == 0 or input[idx-1] == input[idx]:
                    chars[str(c)] += 1
        return max(chars.values())
    else:
        return 0


if __name__ == '__main__':
    input = ' '.join(sys.argv[1:])
    print(longestRun(input))
