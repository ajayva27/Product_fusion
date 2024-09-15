Overview
This is a Django-based project featuring an API for user authentication and organization management. The project includes functionalities for user sign-up, sign-in, role management, and organization membership.

Features
User Authentication: Users can sign up and sign in. Passwords are hashed for security.
Organization Management: Users can create and manage organizations. Each user can be associated with multiple organizations.
Role Management: Users can be assigned different roles within organizations.
Member Management: Includes functionality to invite, delete, and update members' roles.

API Endpoints
Sign Up: Create a new user and an associated organization.
Sign In: Authenticate users and return JWT tokens.
Reset Password: Feature to reset user passwords.
Invite Member: Invite a new member to an organization.
Delete Member: Remove a member from an organization.
Update Member Role: Update the role of a member within an organization.

Configuration
Update the DATABASES section in settings.py with your MySQL database credentials.

Testing
Use Postman to test the API endpoints. Ensure the server is running at http://127.0.0.1:8000.

License
This project is licensed under the MIT License. See the LICENSE file for details.
