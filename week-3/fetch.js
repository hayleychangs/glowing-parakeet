window.onload=function(){
    let src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
    fetch(src).then(function(response){
        // console.log(response);
        return response.json(); //將資料用 JSON 的格式詮釋成: 物件和陣列的組合
    }).then(function(data){
        //console.log("最終的資料", data);
        let sightList=data["result"]["results"]

        //把抓到的資料放到畫面上
        // id: box1-1
        let newDiv = document.createElement("div");
        newDiv.id = "box1-1-pic-container";
        newDiv.className = "box1-pic-container";

        let picStr = sightList[0].file;
        let picPosition = picStr.indexOf("http", 2)
        let pic = document.createElement("img");
        pic.className ="box1-pic";
        pic.src = picStr.substring(0,picPosition)
        
        let newDivText = document.createElement("div");
        newDivText.id = "box1-1-text";
        newDivText.className = "box1-text";

        let newContent = document.createTextNode(sightList[0].stitle);

        newDivText.appendChild(newContent);
        newDiv.appendChild(pic);
        document.getElementById("box1-1").appendChild(newDiv);
        document.getElementById("box1-1").appendChild(newDivText);
        
        // id: box1-2
        let newDiv1 = document.createElement("div");
        newDiv1.id = "box1-2-pic-container";
        newDiv1.className = "box1-pic-container";

        let picStr1 = sightList[1].file;
        let picPosition1 = picStr1.indexOf("http", 2)
        let pic1 = document.createElement("img");
        pic1.src = picStr1.substring(0,picPosition1)
        pic1.className ="box1-pic";
        
        let newDivText1 = document.createElement("div");
        newDivText1.id = "box1-2-text";
        newDivText1.className = "box1-text";

        let newContent1 = document.createTextNode(sightList[1].stitle);

        newDivText1.appendChild(newContent1);
        newDiv1.appendChild(pic1);
        document.getElementById("box1-2").appendChild(newDiv1);
        document.getElementById("box1-2").appendChild(newDivText1);
    

        for (let i=0,j=1;i<=sightList.length-2,j<=sightList.length-2;i++,j++){
            let newDiv3 = document.createElement("div");
                newDiv3.id = "box2-"+j;
                newDiv3.className = "box2"
            document.getElementById("section2").appendChild(newDiv3);
        }

        function handler(){
            console.log('DOM fully loaded')
        }

        for (let i=2,j=1;i<=sightList.length-2,j<=sightList.length-2;i++,j++){
            let newDiv2 = document.createElement("div");
                newDiv2.id = "box2-"+j+"-pic-container";
                newDiv2.className = "box2-pic-container";

            let picStr2 = sightList[i].file;
            let picPosition2 = picStr2.indexOf("http", 2)
            let pic2 = document.createElement("img");
                pic2.src = picStr2.substring(0,picPosition2)
                pic2.className ="box2-pic";

            let newDivText2 = document.createElement("div");
                newDivText2.id = "box2-"+j+"-text";
                newDivText2.className = "box2-text";

            let newContent2 = document.createTextNode(sightList[i].stitle);

            if(window.addEventListener){
                addEventListener("DOMContentLoaded",handler, false);
            
                newDivText2.appendChild(newContent2);
                newDiv2.appendChild(pic2);
                document.getElementById("box2-"+j).appendChild(newDiv2);
                document.getElementById("box2-"+j).appendChild(newDivText2);
            }
        }
    })  
}

let currentItems = 8;
let btn = document.getElementById('btn');

        btn.addEventListener('click', function(){
            let boxes = [...document.querySelectorAll(".box2")];
            for (let i=currentItems;i<currentItems+8;i++ ){
                boxes[i].style.display = "block";
            }
            currentItems +=8;
            if(currentItems>=boxes.length){
                btn.style.display = "none";
            }
        })