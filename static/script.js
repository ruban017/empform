function calculateAge() {
  const dob = new Date(document.getElementById("dob").value);
  const currentYear = new Date().getFullYear();
  const age = currentYear - dob.getFullYear();
  document.getElementById("age").value = age;
}

function submission() {
  alert("Form submitted Successfully!!!")
}