// scripts.js

var textField = document.getElementById('text-field');
var okButton = document.getElementById('ok-button');
var outputContainer = document.querySelector('.output-container'); // Get the output container element

okButton.addEventListener('click', function() {
	// Get the text from the input field
	var petDescription = textField.value;

	// Create a request object with the parameters
	var request = new Request('/getpetnames', {
	method: 'POST', // Use POST instead of GET
	headers: {
		'Content-Type': 'application/json',
	},
	body: JSON.stringify({ description: petDescription,
						   style: 'sad',
						}),
	});


	fetch(request)
	.then(function(response) {
		return response.json(); 
	})
	.then(function(data) {
		console.log(data);
		display_names(data)
	})
	.catch(function(error) {
		console.error('Fetch error:', error);
	});
});


function display_names(data) {
	// Clear the output container before adding new divs
	outputContainer.innerHTML = '';
	// Loop through the generated names and create a div for each name
	data.names.forEach(function(name) {
	var nameDiv = document.createElement('div');
	nameDiv.textContent = name;
	outputContainer.appendChild(nameDiv);
	});
}
