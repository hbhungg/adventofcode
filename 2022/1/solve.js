const {readFileSync, promises: fsPromises} = require('fs');
const contents = readFileSync("input.txt", "utf-8");
const arr = contents.split(/\r?\n/);


let m = 0
let sum_curr = 0

for (let i=0;i<arr.length;i++) {
  curr = arr[i]
  // If new line
  if (curr != "") {
    sum_curr += parseInt(curr)
  // If Int
  } else {
    if (sum_curr > m) {
      m = sum_curr
    }
    sum_curr = 0
  }
}


console.log(m)


