function submitForm(){
	// Get the values from the form
	var name = document.getElementById("name").value;
	var age = document.getElementById("age").value;

	// Validate the input
	if (name == "" || age == "") {
		alert("Please enter both your name and age.");
		return;
	}

	// Validate the age
	if (age <= 0) {
		alert("Please enter a valid age.");
		return;
	}

	// Calculate the birth year
	var currentYear = new Date().getFullYear();
	var birthYear = currentYear - age;

	// Display the result
	var resultElement = document.getElementById("result");
	resultElement.innerHTML = "Hello " + name + "! Your birth year is " + birthYear + ".";
}
