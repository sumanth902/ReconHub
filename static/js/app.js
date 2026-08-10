console.log("ReconHub Loaded");
document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");

    form.addEventListener("submit", function () {

        document.getElementById("loading").style.display = "block";

    });

});
document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("reconForm");

    if(form){

        form.addEventListener("submit", function(){

            document.getElementById("loading").style.display = "flex";

        });

    }

});