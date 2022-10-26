function redirect(){
    const number = document.getElementById("integer").value;
    if (number!=""){
        window.location.href="/square/"+number;
    }
}