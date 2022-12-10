let username = document.getElementById("id_username");
let password = document.getElementById("id_password");

document.addEventListener("DOMContentLoaded", loadPlaceholder, false)

function loadPlaceholder(){
    username.placeholder = "Username";
    password.placeholder = "Password";
}