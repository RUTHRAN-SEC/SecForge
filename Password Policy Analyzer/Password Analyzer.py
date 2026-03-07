import json   # Used to work with JSON files


def load_policy(file):
    # Open the JSON file in read mode
    with open(file, 'r') as f:
        # Load and return JSON data as Python dictionary
        return json.load(f)


def analyze_policy(policy):
    results = []  # List to store analysis results

    # Rule 1: Minimum Length Check
    if policy["min_length"] < 8:
        results.append("Minimum length is less than 8 (Not NIST compliant)")
    else:
        results.append("Minimum length is acceptable")

    # Rule 2: Forced Complexity Check
    # NIST recommends NOT forcing special characters
    if policy["require_special"]:
        results.append("NIST does not recommend forcing special characters")
    else:
        results.append("No forced special characters (Good)")

    # Rule 3: Password Expiry Check
    # Frequent password expiry is discouraged by modern NIST guidelines
    if policy["password_expiry_days"] < 90:
        results.append("Frequent password expiry is not recommended by NIST")
    else:
        results.append("Password expiry policy is acceptable")

    # Rule 4: Passphrase Support Check
    # NIST recommends allowing long passphrases
    if not policy["allow_passphrases"]:
        results.append("Passphrases should be allowed")
    else:
        results.append("Passphrases allowed")

    return results  # Return list of compliance results


def main():
    # Load policy from JSON file
    policy = load_policy(r"C:\Users\heyru\OneDrive\Documents\Python Codes\Password Policy Analyzer\sample company policy.json")
    # Analyze the loaded policy
    results = analyze_policy(policy)

    # Print report header
    print("\nPassword Policy Compliance Report\n")

    # Print each result line
    for r in results:
        print(r)


# Run the program only if executed directly
if __name__ == "__main__":
    main()
