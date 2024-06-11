function openSignIn() {
  document.getElementById('signInPopup').style.display = "block";
}

function closeSignIn() {
  document.getElementById('signInPopup').style.display = "none";
}

function openSignUp() {
  document.getElementById('signInPopup').style.display = "none";
  document.getElementById('signUpPopup').style.display = "block";
}

function closeSignUp() {
  document.getElementById('signUpPopup').style.display = "none";
  document.getElementById('signInPopup').style.display = "block";
}

function validatePassword() {
  var password = document.getElementById("newPassword");
  var confirmPassword = document.getElementById("reenterPassword");
  if (password.value != confirmPassword.value) {
      confirmPassword.setCustomValidity("Passwords do not match");
  } else {
      confirmPassword.setCustomValidity('');
  }
}
newPassword.onchange = validatePassword;
reenterPassword.onkeyup = validatePassword;