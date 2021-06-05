document.addEventListener("DOMContentLoaded", function(event) {

    var thumbnailElement = document.getElementById("smart_thumbnail");
       thumbnailElement.className="";

    thumbnailElement.addEventListener("click", function() {
        alert("I saw you click!");      // write here                                
    });



    if (thumbnailElement.className == "") {
        thumbnailElement.addEventListener("click", function() {
            alert("Imagen small ");
            thumbnailElement.className="small";

   });
    }
        else {

            thumbnailElement.addEventListener("click", function() {
                alert("Imagen Big ");
                thumbnailElement.className="";

            });
        }







});


