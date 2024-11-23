calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    line = string
    string_info = (len(line), line.upper(), line.lower())
    count_calls()
    return string_info


def is_contains(string, list_to_search):
    count_calls()
    string = str(string).lower()
    list_to_search = list(list_to_search)
    for elem in range(len(list_to_search)):
        if string == str(list_to_search[elem]).lower():
            result = True
        else:
            result = False

    return result


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches

print(calls)
