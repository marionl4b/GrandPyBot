let form = document.querySelector("form");
let chat = document.getElementById("chat");

function addUserBubble(){
    // set user message into a bubble of the chat section
    let userRow = document.createElement("div");// set new user chat row
    userRow.classList.add("row", "user-message", "align-items-end");
    let userCol1 = document.createElement("div");// set new col for bubble
    userCol1.classList.add("col-10");
    let userCol2 = document.createElement("div");// set new col for avatar
    userCol2.classList.add("col-2", "text-left");
    let userAvatar = document.createElement("img");
    userAvatar.classList.add("avatar");
    userAvatar.setAttribute("src", "/static/images/avatar_user.png");
    userAvatar.setAttribute("alt", "User Avatar");
    let userBubble = document.createElement("div");// set new user bubble
    userBubble.classList.add("bubble");
    let userP = document.createElement("p");// set user message
    userP.textContent = form.elements.usermsg.value;
    // console.log(userMessage);

    userBubble.appendChild(userP); //add new user message to DOM
    userCol1.appendChild(userBubble);
    userCol2.appendChild(userAvatar);
    userRow.appendChild(userCol1);
    userRow.appendChild(userCol2);
    chat.appendChild(userRow);
}

function addGpbBubble(message){
    // set grandPyBot message into a bubble of the chat section
    let gpbRow = document.createElement("div");// set new gpb chat row
    gpbRow.classList.add("row", "gpb-message", "align-items-start");
    let gpbCol2 = document.createElement("div");// set new col for bubble
    gpbCol2.classList.add("col-10");
    let gpbCol1 = document.createElement("div");// set new col for avatar
    gpbCol1.classList.add("col-2", "text-right");
    let gpbAvatar = document.createElement("img");
    gpbAvatar.classList.add("avatar");
    gpbAvatar.setAttribute("src", "/static/images/avatar_gpb.png");
    gpbAvatar.setAttribute("alt", "GrandPyBot Avatar");
    let gpbBubble = document.createElement("div");// set new gpb bubble
    gpbBubble.classList.add("bubble");
    let gpbP = document.createElement("p");// set gpb message
    gpbP.textContent = message;
    // console.log(gpbMessage);

    gpbBubble.appendChild(gpbP); //add new gpb message to DOM
    gpbCol1.appendChild(gpbAvatar);
    gpbCol2.appendChild(gpbBubble);
    gpbRow.appendChild(gpbCol1);
    gpbRow.appendChild(gpbCol2);
    chat.appendChild(gpbRow);
}

addGpbBubble("Bonjour Poussin, qu'est ce que je peux faire pour toi?");

function ajaxPost(url, data, success, error, progress){
    progress(true);
    let xhr = new XMLHttpRequest();
    xhr.open("POST", url);
    xhr.setRequestHeader("content-type", "application/json; charset=UTF-8");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4){
            if (xhr.status >=200 && xhr.status < 300){
                success(data);
                progress(false);
            }else{
                error(xhr.status, xhr.statusText)
            }
        }
    };
    xhr.send((data));
}

document.getElementById("ajaxButton").addEventListener("click", function () {
    let usermsg = document.getElementById("textUserMessage").value;
    let data = JSON.stringify({userMessage: usermsg});
    ajaxPost("/index", data, success, error, progress);

    function success(data) {
        addUserBubble();
        console.log(data);
    }

    function error(err, txt) {
        console.log(err, txt)
    }

    function progress(state) {

    }
});