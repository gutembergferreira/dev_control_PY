function CallLoadScreen() {
    document.getElementById('loader-container').style.display = 'flex';
    disableEnterKey();
}

function disableEnterKey() {
    document.addEventListener('keydown', function(event) {
      if (event.key === 'Enter') {
        event.preventDefault();
      }
    });
  }