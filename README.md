# password-manager

## What is this?
A little project to gain more experience with:
- Database connections with Python
- Password hashing and basic encryption
- GUI design using customtkinter
- Git and version control

This tool is made just for educational purposes and I do not intend it it to be used as a secure password storage solution for real-world sensitive data.

## How to use?
User is prompted with login window which asks for inputs:
- username
- database password
- master password.

On the first use, master password is hashed (using bcrypt) and stored into the database and checked against the stored hash for authentication on subsequent launches. This way the master password is not visible or stored in plain text in any point during the process.

