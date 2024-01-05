class User {
    constructor(username, email, password) {
      this._username = username; // The underscore is a common convention to indicate a private property.
      this._email = email;
      this._password = password;
    }
  
    // Getter for username
    get username() {
      return this._username;
    }
  
    // Setter for username
    set username(newUsername) {
      // You can add validation if necessary
      this._username = newUsername;
    }
  
    // Getter for email
    get email() {
      return this._email;
    }
  
    // Setter for email
    set email(newEmail) {
      // Here you could also add validation for email format
      this._email = newEmail;
    }
  
    // Getter for password
    get password() {
      // Normally you wouldn't have a getter for passwords for security reasons.
      // It's here for the sake of completeness.
      return this._password;
    }
  
    // Setter for password
    set password(newPassword) {
      // Add validation and perhaps password hashing
      this._password = newPassword;
    }
  }
  
  // Using the user class
  const user = new User('JaneDoe', 'jane@example.com', 'password123');
  console.log(user.username);  // JaneDoe
  
  // Changing username with setter
  user.username = 'JaneSmith';
  console.log(user.username);  // JaneSmith
  
  // Attempt to directly access property (ill-advised due to underscore convention)
  console.log(user._username);