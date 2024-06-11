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

window.onload = function() {
  const popupMessage = document.getElementById('popupMessage');
  if (popupMessage) {
      popupMessage.style.display = 'block';
  }
};

function closePopup() {
  document.getElementById('popupMessage').style.display = 'none';
}