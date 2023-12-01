const {readFileSync, promises: fsPromises} = require('fs');
const contents = readFileSync("input.txt", "utf-8");
const arr = contents.split(/\r?\n/);

const type = {
  "A": 0, // Rock
  "B": 1, // Paper
  "C": 2, // Scissor
  "X": 0,
  "Y": 1,
  "Z": 2,
}

function pmodulo(a, n) {
  return ((a % n) + n) % n
}
// True if p1 win p2
function play(p1, p2) {
  if (p1 == p2) return null
  tt = pmodulo((p1-p2), 3)
  if (tt < 3/2) {
    return true
  } return false
}

let score = 0
for (let i=0;i<arr.length;i++) {
  console.log(arr[i])
  p1 = type[arr[i][0]]
  p2 = type[arr[i][2]]
  outcome = play(p2, p1)
  score += p2 + 1
  if (outcome == true) {
    score += 6
  } else if (outcome == null) {
    score += 3
  }
}
console.log(score)



