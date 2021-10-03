$(function(){
   $("#mostrar").click(function(){
       $("#parrafo").show();
   });

   $("#ocultar").click(function(){
        $("#parrafo").hide();
    });

    $("#fadeC").click(function(){
        $("#div1").fadeIn();
        $("#div2").fadeIn("slow");
        $("#div3").fadeIn(3000); 
    });

    $("#animacion").click(function(){
        $("#cuadrado").animate({top: '5px'});
    });

});
