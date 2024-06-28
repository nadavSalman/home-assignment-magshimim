
def letter_combinations(digits):
    if not digits:
        return []

    digit_to_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    

    
    combinations = []
    backtrack(digit_to_letters, digits, 0, [], combinations)
    return combinations

def backtrack(digit_to_letters, digits, index, path, combinations):
    if index == len(digits):
        combinations.append("".join(path))
        return
    
    for letter in digit_to_letters[digits[index]]:
        path.append(letter)
        backtrack(digit_to_letters, digits, index + 1, path, combinations)
        path.pop()


def main():
    digits = "23"
    print(letter_combinations(digits))

if __name__  == '__main__':
    main()