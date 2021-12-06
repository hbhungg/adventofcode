package main

import (
	"bufio"
	"fmt"
	"log"
	"strings"

	"strconv"
	"os"
)

func main() {
  f, err := os.Open("input.txt")
  if err != nil {
    log.Fatal(err)
  }
  defer f.Close()
  var lst []string
  scanner := bufio.NewScanner(f)
  for scanner.Scan() {
    lst = append(lst, scanner.Text())
  }
  fmt.Println(solve(lst))
}

func solve(lst []string) (int64, int64) {
  var depth1 int64 = 0
  var horiz1 int64 = 0
  var depth2 int64 = 0
  var horiz2 int64 = 0
  var aim int64 = 0
  for _, val := range lst {
    parse := strings.Split(val, " ")
    i, _ := strconv.ParseInt(parse[1], 10, 0) 
    if parse[0] == "forward" { 
      horiz1 += i 
      horiz2 += i
      depth2 += aim * i
    }
    if parse[0] == "down" { 
      depth1 += i 
      aim += i
    }
    if parse[0] == "up" { 
      depth1 -= i 
      aim -= i
    }
  }
  return horiz1 * depth1, horiz2 * depth2
}

