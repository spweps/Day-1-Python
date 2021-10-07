// function bookIndex(arr){
//     var range = 0
//     for (var i = 0; i<arr.length; i++){
//         if (arr[i] + 1 == arr[i+1]){
//             while(arr[i] + 1 == arr[i+1]){
//             print (arr[i]);
//         if (arr[i] + 1 != arr[i+1])
//             print (null)
//         else: 
//             print (arr);
//     }

// }
// console.log(bookIndex([1,3,4,5,7,8,10,12,14,15,16,17]))

function bookIndex(arr){
    var grouped = "";
    var start = arr[0];
    var end = arr[0];
    for(var i=1; i <= arr.length; i++){
        if(arr[i] == end + 1){
            end = arr[i];
        }
        else if (start == arr[i-1]){
            grouped += ${start}, ;
            start = arr[i];
            end = arr[i];
        }
        else {
            grouped += ${start}-${end}, ;
            start = arr[i];
            end = arr[i];
        }
    }
    grouped = grouped.slice(0, grouped.length-2);
    return grouped;
}

console.log(bookIndex([1,3,4,5,7,8,10,12,14,15,16,17]))



var arr = [1,3,4,5,7,8,10,12,14,15,16,17]

function bookIndex(arr) {
    var answer = [];
    for (var i = 0; i < arr.length; i++) {
        if (arr[i]+1 == arr[i+1]) {
            var start = arr[i];
            while(arr[i]+1 == arr[i+1])
                i++;
            var end = arr[i];
            answer.push(start + "-" + end);    
        }
        else{
            answer.push(arr[i]);
        }
        }
        var finalstring = answer.join(',');
        return finalstring
    } 

console.log(bookIndex(arr));