function submitForm() {
  alert("Form submitted Succesfully");
  const form = document.getElementById("employeeForm");
  const tableBody = document.querySelector("#employeeTable tbody");

  // Create a new row in the table
  const newRow = tableBody.insertRow(tableBody.rows.length);

  // Define an array to store values for the cells
  const cellValues = [];

  // Add values to the array
  for (let i = 0; i < form.elements.length - 2; i++) {
    const inputValue = form.elements[i].value;
    cellValues.push(inputValue);
  }
  // Use insertCell method to add cells with values to the row
  for (const value of cellValues) {
    const cell = newRow.insertCell();
    cell.textContent = value;
  }
}
function resetForm() {
  const formm = document.getElementById("employeeForm");
  formm.reset();
}
function calculateAge() {
  const dob = new Date(document.getElementById("dob").value);
  const currentYear = new Date().getFullYear();
  const age = currentYear - dob.getFullYear();
  document.getElementById("age").value = age;
}

function calculateExp() {
  const jn = new Date(document.getElementById("joiningDate").value);
  const currentYear = new Date().getFullYear();
  const exp = currentYear - jn.getFullYear();
  document.getElementById("experience").value = exp;
}
