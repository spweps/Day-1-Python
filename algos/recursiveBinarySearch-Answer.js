// Big O Notation!  Quick summary video: https://www.youtube.com/watch?v=g2o22C3CRfU
// O(n) | Lineary Complexity - it takes exactly 1 unit of time per element when looping through an array of items
// O(log n) | Logarithmic Complexity - in a sorted array we can do a binary search where we check whether the 
//    value given is greater than or less than a midway point and we continue cutting the search range in half
//    until we find the value.  This is why the given array must be sorted for this to work

// Here is an example of how the binary search would work
// The array we are searching: arr = [1,2,3,5,7,9,10,11,13,14,15,56,78]
// The value we are looking for:  value = 9

// STEPS:
// [1,2,3,5,7,9,10  |  11,13,14,15,56,78] - Get the array's middle index position
//   Find the halfway point's value. 9 is less than that so we only need to search the left side
// [1,2,3,5  |  7,9,10] - Now we cut the left hand side in half and evaluate the midpoint's value
//   9 is greater than the midpoint's value so we only need to search the right hand side
// [7, | 9,10] - Now, depending on where you split in half, 9 is greater than halfway so we check the right hand side
// [9, | 10] - Get it down to 1 or 2 items, then check to see which one the value is equal to

// Use recursiveBinarySearch(input, target, ?????) to receive a given array of sorted numbers and value to search for
// Return true if the value is found, return false if it is not

// HINTS:  You may want two other parameters, one for the left side (start) of the array and one for the right (end)

// Edge Cases:
// What if it's empty?  What if the value is in the middle?

function recursiveBinarySearch(arr, value, left = 0, right = arr.length - 1) {
    if(left > right) {
        return false
    }
    mid = Math.floor((right+left)/2)

    if(value == arr[mid]) {
        return true;
    }
    if(value < arr[mid]) {
        right = mid - 1 ;
        return recursiveBinarySearch(arr,value,left,right)
    }
    else if(value > arr[mid]) {
        left = mid + 1;
        return recursiveBinarySearch(arr,value,left,right)
    }
}

arr = [1,2,3,5,7,9,10,11,13,14,15,56,78]
console.log(recursiveBinarySearch(arr,10))
console.log(recursiveBinarySearch(arr,78))
console.log(recursiveBinarySearch(arr,111))
console.log(recursiveBinarySearch(arr,999))


/*Other Solutions*/

// function recursiveBinarySearch(num,arr,left=0,right=arr.length) {
//     if(arr.length < 1){
//         return -1
//     }
//     if(right-left > 1){
//         var mid = Math.floor((right+left)/2)

//         if(arr[mid] == num){
//             return mid
//         }
//         if(num < arr[mid]){
//             return recursiveBinarySearch(num,arr,left,mid)
//         }
//         return recursiveBinarySearch(num,arr,mid+1,right)
//     }
//     return arr[left] == num ? left : -1
// }


/*
function recursiveBinarySearch(arr,value,start,end) {
    var midpt = start + Math.floor((end-start)/2)

    if(value==arr[midpt]){
        console.log("equal " + midpt)
        return midpt
    }
    else if(start==end){
        console.log("False")
        return "not found"
    }
    else if(value < arr[midpt]){
        return recursiveBinarySearch(arr,value,start,midpt)
    }
    else{
        return recursiveBinarySearch(arr, value,midpt+1,end)
    }
}

arr = [1,2,3,5,7,9,10,11,13,14,15,56,78]
var result = recursiveBinarySearch(arr,56,0,arr.length)
console.log(result)

*/


/*

var array = [1,2,3,5,7,9,10,11,13,14,15,56,78]

function binarySearch(array, value, counter=0){
    var halfway = Math.floor(array.length/2)
    console.log(`Array: ${array}, Value: ${value}, Counter: ${counter}`)

    if(array[halfway-1] == value && array[halfway] != value){
        return counter + halfway - 1
    }
    if(array[halfway-1] != value && array[halfway] == value){
        return counter + halfway
    }
    if(array.length <= 2){
        if(array[halfway-1] != value && array[halfway] != value){
            return false
        }
    }

    if(array[halfway-1] > value){
        return binarySearch(array.slice(0, halfway), value, counter)
    }
    if(array[halfway] < value){
        counter += halfway
        return binarySearch(array.slice(halfway), value, counter) //slice the last half of array
    }

}


console.log(binarySearch(array, 15))

*/

/*

const recursiveBinarySearch = (arr, val, position, counter) => {
    if(counter == 0)
        return false
    counter == -1 ? counter = Math.floor(arr.length/2) : counter = Math.floor(counter/2)
    if(arr[position+counter] == val)
        return position+counter
    else if (arr[position+counter] < val)
        return recursiveBinarySearch(arr, val, position + counter, counter)
    else
        return recursiveBinarySearch(arr, val, position , counter)
}
console.log(recursiveBinarySearch ([0, 1, 2, 3, 4, 5, 6, 7, 8],95, 0, -1));
console.log(recursiveBinarySearch ([0, 1, 2, 3, 4, 5, 6, 7, 8],-20, 0, -1));
console.log(recursiveBinarySearch ([0, 1, 2, 3, 4, 5, 6, 7, 8],5, 0, -1));
console.log(recursiveBinarySearch ([0, 1, 2, 3, 4, 6, 7, 8],5, 0 ,-1));
console.log(recursiveBinarySearch ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12, 13, 14, 15],1, 0, -1));
console.log(recursiveBinarySearch ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12, 13, 14, 15],4, 0, -1));
console.log(recursiveBinarySearch ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12, 13, 14, 15],7, 0, -1));
console.log(recursiveBinarySearch ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12, 13, 14, 15],12, 0, -1));
console.log(recursiveBinarySearch ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12, 13, 14, 15],15, 0, -1));

*/