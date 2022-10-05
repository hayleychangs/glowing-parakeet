window.onload=function(){
    let src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
    fetch(src).then(function(response){
        // console.log(response);
        return response.json(); //將資料用 JSON 的格式詮釋成: 物件和陣列的組合
    }).then(function(data){
        //console.log("最終的資料", data);
        let sight_list=data["result"]["results"]

        //把抓到的資料放到畫面上
        // id: box1-1
        let newDiv = document.createElement("div");
        newDiv.id = "box1-1-pic-container";
        newDiv.className = "box1-pic-container";

        let picStr = sight_list[0].file;
        let pic_position = picStr.indexOf("http", 2)
        let pic = document.createElement("img");
        pic.src = picStr.substring(0,pic_position)
        pic.className ="box1-pic";
        
        let newDivText = document.createElement("div");
        newDivText.id = "box1-1-text";
        newDivText.className = "box1-text";

        let newContent = document.createTextNode(sight_list[0].stitle);

        newDivText.appendChild(newContent);
        newDiv.appendChild(pic);
        document.getElementById("box1-1").appendChild(newDiv);
        document.getElementById("box1-1").appendChild(newDivText);
        
        // id: box1-2
        let newDiv1 = document.createElement("div");
        newDiv1.id = "box1-2-pic-container";
        newDiv1.className = "box1-pic-container";

        let picStr1 = sight_list[1].file;
        let pic_position1 = picStr1.indexOf("http", 2)
        let pic1 = document.createElement("img");
        pic1.src = picStr1.substring(0,pic_position1)
        pic1.className ="box1-pic";
        
        let newDivText1 = document.createElement("div");
        newDivText1.id = "box1-2-text";
        newDivText1.className = "box1-text";

        let newContent1 = document.createTextNode(sight_list[1].stitle);

        newDivText1.appendChild(newContent1);
        newDiv1.appendChild(pic1);
        document.getElementById("box1-2").appendChild(newDiv1);
        document.getElementById("box1-2").appendChild(newDivText1);
    
        function handler(){
            console.log('DOM fully loaded')
        }

        for (let i=2,j=1;i<=9,j<=8;i++,j++){
            let newDiv2 = document.createElement("div");
            newDiv2.id = "box2-"+j+"-pic-container";
            newDiv2.className = "box2-pic-container";

            let picStr2 = sight_list[i].file;
            let pic_position2 = picStr2.indexOf("http", 2)
            let pic2 = document.createElement("img");
            pic2.src = picStr2.substring(0,pic_position2)
            pic2.className ="box2-pic";

            let newDivText2 = document.createElement("div");
            newDivText2.id = "box2-"+j+"-text";
            newDivText2.className = "box2-text";

            let newContent2 = document.createTextNode(sight_list[i].stitle);

            if(window.addEventListener){
                addEventListener('DOMContentLoaded',handler, false);
            
                newDivText2.appendChild(newContent2);
                newDiv2.appendChild(pic2);
                document.getElementById("box2-"+j).appendChild(newDiv2);
                document.getElementById("box2-"+j).appendChild(newDivText2);
            };
        }
    })
}

//document.body.onload = addElement();
//addElement();

// //function addElement1() {}
//     // create a new div element for pic
// const newDiv = document.createElement("div");
// newDiv.id="box1-1-pic-container";
// newDiv.className="box1-pic-container";

// document.getElementById("box1-1").appendChild(newDiv);

// // create a new div element for text
// const newDivText = document.createElement("div");
// newDivText.id="box1-1-text";
// newDivText.className="box1-1-text";

// // and give it some content
// const newContent = document.createTextNode("Hi there and greetings!");
  
// // add the text node to the newly created div
// newDivText.appendChild(newContent);

// //透過 appendChild 將 newDivText 加入至 box1-pic-container
// document.getElementById("box1-1-pic-container").appendChild(newDivText);


// //取得容器
// let box1 = document.getElementById("box1-1");

// //建立新的 div 元素
// let newDiv = document.createElement("div");

// //對新建元素指定屬性
// newDiv.id="pic1-1";
// newDiv.className="box1-pic-container";
// newDiv.style.backgroundColor=blue;

// //建立 textNode 文字結點
// let textNode = document.createTextNode("Hello world")

// //透過 appendChild 將 textNode 加入至 newDiv
// newDiv.appendChild(textNode);

// //透過 appendChild 將 newDiv 加入至 box1
// box1.appendChild(newDiv);
// //document.querySelector(".box1").appendChild(newDiv)