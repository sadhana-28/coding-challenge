// Lab 8: Email Validation

let email = "user@gmail.com";
let regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.[a-z]{2,}$/;

if (regex.test(email)) {
  console.log("Valid email:", email);
  console.log("Thank you message sent");
} else {
  console.log("Invalid email format");
}
