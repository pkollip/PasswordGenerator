var submit = document.getElementById("submit")

submit.onclick = function(){
    var length = document.getElementById("length").value;
    var symbols = document.getElementById("symbols").value;
    var digits = document.getElementById("digits").value;
    var lowercase = document.getElementById("lowercase").value;
    var uppercase = document.getElementById("uppercase").value;

    if (length <= 0) {
        var text = "Not a valid length value!";
        var new_para = document.createElement("p");
        var new_text = document.createTextNode(text);
        new_para.appendChild(new_text);
        document.body.appendChild(new_para);
    }
}