/* Given 2 arrays, create a function that let's a user know (true/false) whether these two arrays contain any common items 
    For example: const array = ['a','b','c','x'];
                const array = ['z','y','i']; 
                should return false */

array1 = ['a', 'b', 'c', 'x'];
array2 = ['z', 'c', 'i'];
const trueFalse = (array1, array2) => {
    for (let i = 0; i < array1.length; i++) {
        for (let j = 0; j < array2.length; j++) {
            if (array1[i] === array2[j]) {
                return true;
            }
        }
    }
    return false;
}
console.log(trueFalse(array1, array2));