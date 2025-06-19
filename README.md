# password-manager

## What is this?
A little project to gain more experience with:
- Database connections with Python
- Password hashing and basic encryption
- GUI design using [customtkinter](https://github.com/TomSchimansky/CustomTkinter)
- Git and version control

This tool is made just for **educational purposes** and I do **not intend** it to be used as a secure password storage solution for real-world sensitive data.

## How to use?

User is prompted with login window which asks for inputs:
- username
- database password
- master password

### First-time setup

On the first use, master password is hashed (using bcrypt) and stored into the database and checked against the stored hash for authentication on subsequent launches. This way the master password is not visible or stored in plain text in any point during the process. Program creates salt as well on the first launch. These both happen only once and the values are stored in their own respective tables.

### Subsequent launches

On every login, a key is derived from the user-prompted master password and the generated salt. The key is used to encrypt the stored passwords. Every password that is stored is randomly generated before encryption and the encrypted password is stored with the site it is used on into a Postgres database.

### Password handling

1. Every password is randomly generated from ASCII letters, digits and punctuation.
2. Password is encrypted with AES-GCM:
    - A **key** is derived from the master password and salt using 'PBKDF2HMAX':
      - Hash function: SHA-256
      - Output length: 32 bytes
      - Iterations: 100,000
    - A random **nonce** is generated and used for each encryption 
3. cyphertext and the nonce are both stored into the Postgres database along with the associated site




