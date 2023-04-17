# password-strength-checker
Created a password strength checker using a combination of hashing algorithms and password policies using various Python pretrained models and APIs:

Choose a hashing algorithm: There are many hashing algorithms available, but for this project, we will use SHA-256. Python has a built-in hashlib library that can be used to generate SHA-256 hashes.

Set up password policies: Password policies are a set of rules that define the strength of a password. For example, password length, the inclusion of uppercase and lowercase letters, numbers, and symbols. You can use a Python library like password_strength to set up password policies.

Generate hash of the password: Once the user enters the password, generate the SHA-256 hash of the password using the hashlib library.

Compare the generated hash with a list of known compromised passwords: There are many databases available online that store hashes of known compromised passwords. You can use the haveibeenpwned API to check if the generated hash matches with any known compromised password hashes.

Evaluate password strength based on password policies: Check the password against the password policies set up in step 2. The password strength can be evaluated based on the number of policies the password satisfies.

Provide feedback to the user: Finally, provide feedback to the user based on the strength of the password. If the password is strong, let the user know that it's a good password. If it's weak, provide suggestions on how to improve the password.
