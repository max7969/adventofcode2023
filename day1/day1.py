def remove_all_chars_which_are_not_numbers(string): 
    return "".join(c for c in string if c.isdigit())

def parse_digits_wrote_as_text(line):
    line = line.replace("one", "o1ne")
    line = line.replace("two", "t2wo")
    line = line.replace("three", "th3ree")
    line = line.replace("four", "fo4ur")
    line = line.replace("five", "fi5ve")
    line = line.replace("six", "s6ix")
    line = line.replace("seven", "se7ven")
    line = line.replace("eight", "ei8ght")
    line = line.replace("nine", "ni9ne")
    return line

def calibrate(content, parseText=False):
    sum = 0
    for line in content:
        if parseText:
            line = parse_digits_wrote_as_text(line)
        line = remove_all_chars_which_are_not_numbers(line)
        value = line[0] + line[-1]
        sum += int(value)
    return sum