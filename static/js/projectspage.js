 // h1 text animation


 var list = ["p","pr","pro","proj","proje","projec","project","projects"]

 var a =  setInterval(fun, 700)

   var i = -1

   function fun(){
       i= i+1
    
       document.getElementById("h21").innerText = list[i] 

       if (i==7) {
  
           i=0
           clearInterval(a)
       }    
       
}

fun();


// p animation

// all projects made by super web

var tem = ["a","al","all","all p","all pr","all pro","all proj","all proje","all proje","all projec","all project","all projects","all projects m","all projects ma","all projects mad","all projects made","all projects made b","all projects made by","all projects made by<br> s","all projects made by<br> su","all projects made by<br> sup","all projects made by<br> supe","all projects made by<br> super","all projects made by<br> super w","all projects made by<br> super we","all projects made by<br> super web"]

var b =  setInterval(fuc, 200)



var t = -1

function fuc(){
   t = t+1
  
   document.getElementById("p12").innerHTML= tem[t]

   if (t==25) {
       t=0
       clearInterval(b)
   }    
   
}

fuc();




    