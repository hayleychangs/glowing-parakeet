//要求一: 函式與流程控制
function calculate(min, max, step){
    let n=min;
    let m=max;
    let s=step;
    let result=0;
    while(n<=m){
        result=result+n;
        n=n+s;
    }
    console.log(result)
}
calculate(1, 3, 1);
calculate(4, 8, 2);
calculate(-1, 2, 2);
  
//要求二：JavaScript 物件與陣列 
function avg(data){
    let sum=0;
    let p=0;
    if(typeof data !== 'undefined'){
        let mydata=data.employees;
    
        for(let i=0;i<mydata.length;i++){
            if (mydata[i].manager==false){
                sum=sum+mydata[i].salary;
                p+=1;
            }   
        }
    let avg=sum/p
    console.log(avg)
    }
}
avg({                     
        "employees":[          
            {                   
                "name":"John",
                "salary":30000,
                "manager":false
            },
            {
                "name":"Bob",
                "salary":60000,
                "manager":true
            },
            {
                "name":"Jenny",
                "salary":50000,
                "manager":false
            },
            {
                "name":"Tony",
                "salary":40000,
                "manager":false
            }
    ]
}); // 呼叫 avg 函式

//要求三：完成以下函式，最後能印出程式中註解所描述的結果。

function func(a){
    return Mul
    function Mul(b,c){
        let result=(b*c)+a
        console.log(result)
        return Mul
    }
}
func(2)(3, 4); // 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5); // 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9); // 你補完的函式能印出 -3+(2*9) 的結果 15
    // 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果
    

//要求四：
function maxProduct(nums){
    let result = nums[0] * nums[1];
    for (let i=0;i<nums.length;i++){
        for (let j=0;j<nums.length;j++)
            if (nums[i]*nums[j]>result & nums[i] != nums[j]){
                result=nums[i]*nums[j]
            }
    }
    console.log(result)
}
maxProduct([5, 20, 2, 6]) // 得到 120
maxProduct([10, -20, 0, 3]) // 得到 30
maxProduct([10, -20, 0, -3]) // 得到 60
maxProduct([-1, 2]) // 得到 -2
maxProduct([-1, 0, 2]) // 得到 0 或 -0
maxProduct([5, -1, -2, 0]) // 得到 2
maxProduct([-5, -2]) // 得到 10

//要求五：
function twoSum(nums, target){
    let list=nums;
    let t=target;
    let r=[];
    for(let n=0,m=1;m<list.length;m++){
        if(list[n]+list[m]==t){
            r.push((list.indexOf(list[n])))
            r.push((list.indexOf(list[m])))
            return r
        }
    }
}
let result=twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9
    

//要求六 ( Optional )：
function maxZeros(nums){
    // let a=0;
    // let repeated_time=0;
    // for (let i=0;i<nums.length;i++){
    //     if (i==0){
    //         repeated_time+=1;
    //         // a=Math.max(repeated_time, a);
    //     }else if(i !==0){
    //         a=Math.max(repeated_time, a);
    //         repeated_time=0;
    //     }
        
    // console.log(a)
    // }
    // }
    let a=0
    let count = 0
    for(let i = 0; i < nums.length; i++){
        if(nums[i] === 0){
            count += 1;
            if (count>a){
                a=count+=1;
            }else(nums[i]===1);{
                count=0;
            }
        }else(nums[i]===1);{
            count=0;
        }  
        }
    // }
    console.log(a)
}
maxZeros([0, 1, 0, 0]); // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
// maxZeros([1, 1, 1, 1, 1]); // 得到 0
// maxZeros([0, 0, 0, 1, 1]) // 得到 3