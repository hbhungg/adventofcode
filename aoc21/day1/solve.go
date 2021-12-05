package main

import (
  "fmt"
  "log"
  "bufio"
  "strconv"
  "os")

func main() {

  var retval int64
  var curr int64

  f, err := os.Open("input.txt")
  if err != nil {
    log.Fatal(err)
  }  
  defer f.Close()

  scanner := bufio.NewScanner(f)
  for scanner.Scan() {
    if i, err := strconv.ParseInt(scanner.Text(), 10, 0); err == nil {
      // fmt.Printf("%d %d\n", i, curr)
      if (i - curr) > 0 {
        retval += 1
      }
      curr = i
    }
  }
  fmt.Printf("%d\n", retval-1)
}

