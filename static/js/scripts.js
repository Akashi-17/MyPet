// scripts.js

var textField = document.getElementById('text-field');
var okButton = document.getElementById('ok-button');
var output_text_elem = document.querySelector('.output_text'); // Get the output container element

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
	output_text_elem.textContent = data.names;
};

