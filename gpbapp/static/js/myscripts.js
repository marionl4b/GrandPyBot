// set user message into a bubble of the tchat user-message section
let form = document.querySelector("form");
let tchat = document.getElementById("tchat");

form.addEventListener("submit", function (e) {

    let userRow = document.createElement("div");// set new user tchat row
    userRow.classList.add("row", "user-message", "align-items-end");
    let userCol1 = document.createElement("div");// set new col for bubble
    userCol1.classList.add("col-11");
    let userCol2 = document.createElement("div");// set new col for avatar
    userCol2.classList.add("col-1");
    let userAvatar = document.createElement("img");
    userAvatar.classList.add("avatar");
    userAvatar.setAttribute("src", "/static/images/avatar_user.png");
    userAvatar.setAttribute("alt", "User Avatar")
    let userBubble = document.createElement("div");// set new user bubble
    userBubble.classList.add("bubble");
    let userP = document.createElement("p");// set user message
    let userMessage = form.elements.usermsg.value;
    userP.textContent = userMessage;

    userBubble.appendChild(userP); //add new user message to DOM
    userCol1.appendChild(userBubble);
    userCol2.appendChild(userAvatar);
    userRow.appendChild(userCol1);
    userRow.appendChild(userCol2);
    tchat.appendChild(userRow);

    console.log(userMessage);
    e.preventDefault(); // reset post data
});
