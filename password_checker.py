import re

def check_password_complexity(password):
    # Criteria for password complexity
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password)
    lowercase_criteria = re.search(r'[a-z]', password)
    number_criteria = re.search(r'\d', password)
    special_criteria = re.search(r'[\W_]', password)

    # Determine password strength
    if length_criteria and uppercase_criteria and lowercase_criteria and number_criteria and special_criteria:
        strength = 'Strong'
    elif length_criteria and (uppercase_criteria or lowercase_criteria) and (number_criteria or special_criteria):
        strength = 'Medium'
    else:
        strength = 'Weak'

    # Feedback for the user
    feedback = {
        'Length': 'Meets requirements' if length_criteria else 'Does not meet requirements',
        'Uppercase Letters': 'Meets requirements' if uppercase_criteria else 'Does not meet requirements',
        'Lowercase Letters': 'Meets requirements' if lowercase_criteria else 'Does not meet requirements',
        'Numbers': 'Meets requirements' if number_criteria else 'Does not meet requirements',
        'Special Characters': 'Meets requirements' if special_criteria else 'Does not meet requirements'
    }

    return strength, feedback

if __name__ == "__main__":
    password = input("Enter a password to check its complexity: ")
    strength, feedback = check_password_complexity(password)
    print(f"Password Strength: {strength}")
    for criteria, result in feedback.items():
        print(f"- {criteria}: {result}")
