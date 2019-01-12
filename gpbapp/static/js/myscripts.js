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
    let userMessage = form.elements.usermsg.value;
    userP.textContent = userMessage;
    console.log(userMessage);

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
    let gpbMessage = message;
    gpbP.textContent = gpbMessage;
    console.log(gpbMessage);

    gpbBubble.appendChild(gpbP); //add new gpb message to DOM
    gpbCol1.appendChild(gpbAvatar);
    gpbCol2.appendChild(gpbBubble);
    gpbRow.appendChild(gpbCol1);
    gpbRow.appendChild(gpbCol2);
    chat.appendChild(gpbRow);
}

// Execute call AJAX GET
// takes in parameters URL and callback returned in case of success
// function ajaxGet(url, callback) {
//     let req = new XMLHttpRequest();
//     req.open("GET", url);
//     req.addEventListener("load", function () {
//         if (req.status >= 200 && req.status < 400) {
//             //callback with response
//             callback(req.responseText);
//         } else {
//             console.error(req.status + " " + req.statusText + " " + url);
//         }
//     });
//     req.addEventListener("error", function () {
//         console.error("Erreur réseau avec l'URL " + url);
//     });
//     req.send(null);
// }
//
// ajaxGet("/", function () {
//     addGpbBubble("Bonjour Poussin, qu'est ce que je peux faire pour toi?");
// });
//
// function ajaxForm(url, callback) {
//     let req = new XMLHttpRequest();
//     req.open("POST",url);
//     req.addEventListener("load", function(){
//         if(req.status >= 200 && req.status < 400){
//             callback(req.responseText);
//         }else{
//             console.error(req.status + " " + req.statusText + " " + url);
//         }
//     })
//     req.addEventListener("error", function (){
//         console.error("network error with URL:" + url);
//     });
//     req.send(data);
// }
//
// ajaxForm("/index", function () {
//     form.addEventListener("submit", function (e) {
//         addUserBubble();
//         e.preventDefault();
//     });
// });
jQuery(document).ready(function ($) {
    addGpbBubble("Bonjour Poussin, qu'est ce que je peux faire pour toi?")
    let usermsg = $('#textUserMessage').val();
    $('button').on("click", function () {
        $.ajax({
            url: '/index',
            data: $('form').serialize(),
            type: 'POST',
            success: function (response) {
                console.log(response);
                addUserBubble();
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});