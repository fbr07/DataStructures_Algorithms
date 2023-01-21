// What is the Big 0 of the below function?
const anotherFunChallenge = (input) => {
    let a = 5; // 0(1) (Constant Time) because this is only running once we run 
    let b = 10; // 0(1) (Constant Time) because this is only running once we run 
    let c = 50; // 0(1) (Constant Time) because this is only running once we run 
    for (let i = 0; i < input; i++) { // 0(n) (Linear Time) because the number of operations is going to increase to whatever input is because it will loop through input
        let x = i + 1; // 0(n) (Linear Time) because the number of operations is going to increase to whatever input is because it will loop through input
        let y = i + 2; // 0(n) (Linear Time) because the number of operations is going to increase to whatever input is because it will loop through input
        let z = i + 3; // 0(n) (Linear Time) because the number of operations is going to increase to whatever input is because it will loop through input
    }
    for (let j = 0; j < input; j++) { // 0(n) (Linear Time) because the number of operations is going to increase to whatever input is because it will loop through input
        let p = j * 2; // 0(n) (Linear Time) because the number of operations is going to increase to whatever input is because it will loop through input
        let q = j * 2; // 0(n) (Linear Time) because the number of operations is going to increase to whatever input is because it will loop through input
    }
    let whoAmI = "I don't know"; // 0(1) (Constant Time) because this is only running once we run 
}

// Calculate Big 0
/* (4 + 7(n)) = 

    Big 0 = 4 + 7n 
     So now wer have to Remove Constants so we are left with = n

     Big 0 = 0(n) (Linear Time)
*/

// Example # 2
function compressBoxesTwice(boxes, boxes2) {
    boxes.forEach(function(boxes) {
        console.log(boxes);
    })
    boxes2.forEach(function(boxes) {
        console.log(boxes)
        
    });
}

/* Since there are 2 inputs boxes(1) & boxes2(2) and they are different
    we can call boxes(a) & boxes2(b) so Big O will be O(a+b) */