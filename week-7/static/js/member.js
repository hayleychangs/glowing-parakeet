function querySubmit(event){
    const user=document.getElementById("username").value;
    let queryResult=document.getElementById("query-result");
    if (user.length==0){
        queryResultClear();
        let newDiv=document.createElement("div");
            newDiv.className="error-msg";
        let errorContent=document.createTextNode("請輸入會員姓名");
        newDiv.appendChild(errorContent);
        queryResult.appendChild(newDiv);
    }else{
        let url=`http://127.0.0.1:3000/api/member?username=${user}`
        fetch(url, {
            methods: "GET",
        })
        .then((response)=>{
            if (response.ok){
                console.log("request successful");
                queryResultClear();
                getResult();
            }else{
                queryResultClear();
                let newDiv=document.createElement("div");
                    newDiv.className="error-msg";
                    newDiv.id="error-msg";
                let errorContent=document.createTextNode("查詢錯誤");
                newDiv.appendChild(errorContent);
                queryResult.appendChild(newDiv);
                throw new Error("Network response was not ok.");
            }
        })
        .catch((error)=>console.log(error));
    }
    event.preventDefault();
}

let getResult=()=>{
    const user=document.getElementById("username").value;
    let queryResult=document.getElementById("query-result");
    let src=`http://127.0.0.1:3000/api/member?username=${user}`;
    fetch(src).then((response)=>{
        if(!response.ok){
            throw new Error("response.statusText");
        }else{
            return response.json()
        }
    })  
    .then((data)=>{
        if (data["data"]!=null){
            let newDiv=document.createElement("div");
                newDiv.className="member-info";
            let infoContent=document.createTextNode(data["data"].name + " (" + data["data"].username + ")" );
            newDiv.appendChild(infoContent);
            queryResult.appendChild(newDiv);
        }else{
            let newDiv=document.createElement("div");
                newDiv.className="error-msg";
                newDiv.id="error-msg";
            let errorContent=document.createTextNode("查無此會員");
            newDiv.appendChild(errorContent);
            queryResult.appendChild(newDiv);         
        }
    })   
    .catch((error)=>{
        console.error(error);
        renameResultClear();
    });
}

let queryResultClear=()=>{
    let element=document.getElementById("query-result");
    element.innerHTML="";
}

let queryForm=document.getElementById("query-form");
queryForm.addEventListener("submit", querySubmit);

function renameSubmit(event){
    const updateName=document.getElementById("update-name").value;
    let renameResult=document.getElementById("rename-result");
    if (updateName.length==0){
        renameResultClear();
        let newDiv=document.createElement("div");
            newDiv.className="error-msg";
        let errorContent=document.createTextNode("請輸入想要更新的姓名");
        newDiv.appendChild(errorContent);
        renameResult.appendChild(newDiv);
    }else{
        let url="http://127.0.0.1:3000/api/member";
        fetch(url, {
            method: "PATCH",
            body: JSON.stringify({
                "name": updateName,
            }),
            headers:{
                "Content-type": "application/json; charset=UTF-8",
            },
        })
        .then(response=>response.json())
        .then((data)=>{
            if (data.ok){
                console.log(data);
                console.log("更新成功");
                renameResultClear();
                let newDiv=document.createElement("div");
                    newDiv.className="rename-successed";
                let successedContent=document.createTextNode("更新成功");
                newDiv.appendChild(successedContent);
                renameResult.appendChild(newDiv);
            }else{
                console.log(data);
                console.log("更新失敗");
                renameResultClear();
                let newDiv=document.createElement("div");
                    newDiv.className="error-msg";
                let failedContent=document.createTextNode("更新失敗");
                newDiv.appendChild(failedContent);
                renameResult.appendChild(newDiv);
            }
        })
        .catch((error)=>{
            console.error("其它錯誤", error);
            renameResultClear();
        })
    }
    event.preventDefault();
}

let renameResultClear=()=>{
    let element=document.getElementById("rename-result");
    element.innerHTML="";
}

let renameForm=document.getElementById("rename-form");
renameForm.addEventListener("submit", renameSubmit);
