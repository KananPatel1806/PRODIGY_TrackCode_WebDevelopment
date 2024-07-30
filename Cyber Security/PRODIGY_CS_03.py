import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'\d', password) is not None
    special_character_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_character_criteria])

    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_character_criteria:
        feedback.append("Password should include at least one special character.")

    strength = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Very Weak"
    }

    return strength[score], feedback

# Example usage
if __name__ == "__main__":
    password = input("Enter a password to assess its strength: ")
    strength, feedback = assess_password_strength(password)

    print(f"Password Strength: {strength}")
    if feedback:
        print("Feedback:")
        for point in feedback:
            print(f"- {point}")
