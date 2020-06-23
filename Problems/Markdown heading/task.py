def heading(char_string, level=1):
    char = "#"
    if level <= 1:
        return char + " " + char_string
    if level >= 6:
        return (6 * char) + " " + char_string
    return (level * char) + " " + char_string
