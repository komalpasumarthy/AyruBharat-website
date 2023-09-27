let subscribeForm = document.getElementById("subscribeForm");

let nameElement = document.getElementById("name");
let nameErrMsg = document.getElementById("nameErrMsg");

let emailElement = document.getElementById("email");
let emailErrMsg = document.getElementById("emailErrMsg");

let ageElement = document.getElementById("age");
let ageErrMsg = document.getElementById("ageErrMsg");

let symptomsElement = document.getElementById("symptoms");
let symptomsErrMsg = document.getElementById("symptomsErrMsg");

let subscribeBtn = document.getElementById("subscribeBtn");

nameElement.addEventListener("blur", function(event) {
    if (event.target.value === "") {
        nameErrMsg.textContent = "Required*";
    } else {
        nameErrMsg.textContent = "";
    }
});

emailElement.addEventListener("blur", function(event) {
    if (event.target.value === "") {
        emailErrMsg.textContent = "Required*";
    } else {
        emailErrMsg.textContent = "";
    }
});
ageElement.addEventListener("blur", function(event) {
    if (event.target.value === "") {
        ageErrMsg.textContent = "Required*";
    } else {
        ageErrMsg.textContent = "";
    }
});

symptomsElement.addEventListener("blur", function(event) {
    if (event.target.value === "") {
        symptomsErrMsg.textContent = "Required*";
    } else {
        symptomsErrMsg.textContent = "";
    }
});


subscribeForm.addEventListener("submit", function(event) {
    event.preventDefault();
});