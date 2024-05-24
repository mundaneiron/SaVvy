 function showPopup(imageSrc) {
    var popup = document.getElementById('popup');
    var popupImage = document.getElementById('popup-image');

    popupImage.src = imageSrc;
    popup.style.display = 'flex'; // Use flex to center vertically and horizontally
}

function closePopup() {
    var popup = document.getElementById('popup');
    popup.style.display = 'none';
}