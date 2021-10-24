/*function viewId(){
    var first2 = document.getElementById("unique1").value.toString();
};

butt.onclick = function() {
    var val = document.getElementById('elem1').value;
    document.getElementById('str').innerHTML=val.toString();
};*/

function viewDiv(e){
    e.preventDefault()
    document.getElementById("recommend__book1__name").style.display = "block";
    document.getElementById("recommend__book2__name").style.display = "block";
    document.getElementById("recommend__book3__name").style.display = "block";
    document.getElementById("recommend__book4__name").style.display = "block";
    document.getElementById("recommend__book5__name").style.display = "block";
    document.getElementById("text-area").style.display = "block";
    /*viewId();*/
    var first2 = document.getElementById("unique1").value.toString();
    $.ajax({
        url: "http://0.0.0.0:8081/lib/"+first2,
        method: "GET",
        success: function(resp) {console.log(resp)}
})
};



/*
$.ajax({
    url: "http://0.0.0.0:8080/lib/" + first2,
    method: "GET",
    success: function(resp) {console.log(resp)}
})*/
