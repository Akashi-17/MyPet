// script.js

var textField = document.getElementById('text-field');
var okButton = document.getElementById('ok-button');

okButton.addEventListener('click', function() {
  // Make a request to your handler endpoint and update the text field with the response
  fetch('/getpetname')
    .then(function(response) {
      return response.text();
    })
    .then(function(data) {
      textField.value = data;
    })
    .catch(function(error) {
      console.log('Error:', error);
    });
});