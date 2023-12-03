import re


def extract_numbers_and_symbols(content):
    numbers = []
    symbols = {}
    for index, line in enumerate(content):
        for match in re.finditer("([0-9]+)", line):
            number = {'value': int(match.group(1)), 'start': match.span()[0], 'end': match.span()[1], 'line': index}
            numbers.append(number)
        for match in re.finditer("([\*\&\@\/\+\-\%\$\=\#]{1})", line):
            key = str(index) + "," + str(match.span()[0])
            symbols[key] = match.group(1)
    return numbers, symbols

def extract_keys_of_number(number):
    keysToTests = [str(number['line'] - 1) + "," + str(column) for column in range(number['start'] - 1, number['end'] + 1)]
    keysToTests += [str(number['line']) + "," + str(column) for column in range(number['start'] - 1, number['end'] + 1)]
    keysToTests += [str(number['line'] + 1) + "," + str(column) for column in range(number['start'] - 1, number['end'] + 1)]
    return keysToTests

def part1(content):
    sum = 0
    numbers, symbols = extract_numbers_and_symbols(content)
    for number in numbers:
        keysToTests = extract_keys_of_number(number)
        for key in keysToTests:
            if key in symbols:
                sum += number['value']
        
    return sum

def part2(content):
    sum = 0
    numbers, symbols = extract_numbers_and_symbols(content)
    for symbol in symbols:
        if symbols[symbol] == "*":
            relatedNumbers = []
            for number in numbers:
                keysToTests = extract_keys_of_number(number)
                if symbol in set(keysToTests):
                    relatedNumbers.append(number)
            if len(relatedNumbers) == 2:
                sum += relatedNumbers[0]['value'] * relatedNumbers[1]['value']
    return sum