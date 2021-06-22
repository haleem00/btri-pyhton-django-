const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();


window.setTimeout("closeAlert();",3000)

function closeAlert(){
    document.getElementById("message").style.display = "none"
}