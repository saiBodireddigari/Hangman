def get_percentage(number, round_digits=None):
    number *= 100
    return str(round(number, round_digits)) + '%'
