# Random Password Generator

This is a simple Python script that generates a random password of a user-specified length. The password is created using a combination of uppercase letters, lowercase letters, digits, and special characters for enhanced security.

---

## Features
- Generates strong, random passwords.
- Includes uppercase letters, lowercase letters, numbers, and special characters.
- Allows user to specify the desired length of the password.

---

## Prerequisites
- Python 3.12 installed on your system.

---

## How to Use
1. Clone or download the script to your local machine.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script by typing:
   ```bash
   python password_generator.py
   ```
4. Enter the desired password length when prompted.
5. The script will generate and display a random password.

---

## Example
```bash
$ python password_generator.py
Enter the password length: -> 12
Generated Password: %J2f4g#K7Ld9
```

---

## Code Overview
The script uses the `string` and `random` modules to generate passwords. Here's how it works:
1. The script defines character sets for uppercase, lowercase, numbers, and special characters.
2. It combines all these character sets into a single list.
3. The list is shuffled randomly.
4. A password of the specified length is created by selecting characters from the shuffled list.

---

## Customization
You can customize the password generator by:
- Adding or removing character sets (e.g., exclude special characters).
- Modifying the logic to enforce specific password rules (e.g., minimum number of uppercase letters).

---

## License
This project is open source and available under the MIT License.
