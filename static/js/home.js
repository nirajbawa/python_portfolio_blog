
    // h1 text animation


   var list = ["s","su","sup","supe","super","super w","super we","super web"]

  var a =  setInterval(fun, 700)

   var i = -1

    function fun(){
        i= i+1
     
        document.getElementById("h1").innerText = list[i] 

        if (i==7) {
   
            i=0
            clearInterval(a)
        }    
        
}

fun();


// p animation

// best web solution in <br>cheap price

var tem = ["b","be","bes","best","best w","best we","best web","best web s","best web so","best web sol", "best web solu","best web solu","best web solut","best web soluti","best web solutio","best web solution","bets web solution i","best web solution in","best web solution in <br> c","best web solution in <br> ch","best web solution in <br> che","best web solution in <br> chea","best web solution in <br> cheap","best web solution in <br> cheape","best web solution in <br> cheaper","best web solution in <br> cheaper p","best web solution in <br> cheaper pr","best web solution in <br> cheaper pri","best web solution in <br> cheaper pric","best web solution in <br> cheaper price"]

var b =  setInterval(fuc, 200)



var t = -1

function fuc(){
t= t+1
   
    document.getElementById("p1").innerHTML= tem[t]

    if (t==29) {
        t=0
        clearInterval(b)
    }    
    
}

fuc();




// skill animations




function skiani(){
document.getElementById("html").style.animation= "niraj 1s ease-in 1 forwards"
document.getElementById("css").style.animation= "niraj2 1s ease-in 1 forwards"
document.getElementById("js").style.animation= "niraj3 1s ease-in 1 forwards"
document.getElementById("python").style.animation= "niraj4 1s ease-in 1 forwards"
document.getElementById("dm").style.animation= "niraj5 1s ease-in 1 forwards"
document.getElementById("wd").style.animation= "niraj6 1s ease-in 1 forwards"
document.getElementById("bg").style.animation= "niraj7 1s ease-in 1 forwards"
document.getElementById("ve").style.animation= "niraj8 1s ease-in 1 forwards"
document.getElementById("gd").style.animation= "niraj9 1s ease-in 1 forwards"
document.getElementById("cw").style.animation= "niraj10 1s ease-in 1 forwards"
document.getElementById("of").style.animation= "niraj11 1s ease-in 1 forwards"
}



function re(){
    var inwidth = window.innerWidth

if(inwidth>=500){
    document.getElementById("html").style.animation= "niraj 1s ease-in 1 forwards"
    document.getElementById("css").style.animation= "niraj2 1s ease-in 1 forwards"
    document.getElementById("js").style.animation= "niraj3 1s ease-in 1 forwards"
    document.getElementById("python").style.animation= "niraj4 1s ease-in 1 forwards"
    document.getElementById("dm").style.animation= "niraj5 1s ease-in 1 forwards"
    document.getElementById("wd").style.animation= "niraj6 1s ease-in 1 forwards"
    document.getElementById("bg").style.animation= "niraj7 1s ease-in 1 forwards"
    document.getElementById("ve").style.animation= "niraj8 1s ease-in 1 forwards"
    document.getElementById("gd").style.animation= "niraj9 1s ease-in 1 forwards"
    document.getElementById("cw").style.animation= "niraj10 1s ease-in 1 forwards"
    document.getElementById("of").style.animation= "niraj11 1s ease-in 1 forwards"
}

}


