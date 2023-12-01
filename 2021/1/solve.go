package main

import (
  "fmt"
  "log"
  "bufio"
  "strconv"
  "os")

func main() {
  f, err := os.Open("input.txt")
  if err != nil {
    log.Fatal(err)
  }  
  defer f.Close()
  var lst []int64
  scanner := bufio.NewScanner(f)
  for scanner.Scan() {
    if i, err := strconv.ParseInt(scanner.Text(), 10, 0); err == nil {
      lst = append(lst, i)
    }
  }
 fmt.Println(prob1(&lst))
 fmt.Println(prob2(&lst))
  

}

func prob1(lst *[]int64) (int64) {
  var retval int64 = 0
  for i:=1; i < len(*lst); i++ {
    if (*lst)[i] > (*lst)[i-1] {
      retval += 1
    }
  }
  return retval
}

func prob2(lst *[]int64) (int64) {
  var retval int64 = 0
  for i:=4; i < len(*lst)+1; i++ {
    if sum((*lst)[i-4:i-1]) < sum((*lst)[i-3:i])  {
      retval += 1
    }
  }
  return retval
}

func sum(lst []int64) (int64) {
  var retval int64 = 0
  for _, v := range (lst) {
    retval += v
  }
  return retval
}
