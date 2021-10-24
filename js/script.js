function viewDiv(e){
    e.preventDefault()
    document.getElementById("recommend__book1__name").style.display = "block";
    document.getElementById("recommend__book2__name").style.display = "block";
    document.getElementById("recommend__book3__name").style.display = "block";
    document.getElementById("recommend__book4__name").style.display = "block";
    document.getElementById("recommend__book5__name").style.display = "block";
    document.getElementById("text-area").style.display = "block";
};

$.ajax({
    url: "http://0.0.0.0:8080/lib/",
    method: "GET",
    success: function(resp) {console.log(resp)}
})