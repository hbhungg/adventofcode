use std::fs;

fn main() {
  let content = fs::read_to_string("input.txt")
    .expect("IDK");
  let arr: Vec<&str> = content.split("\n").collect();

  let mut score = 0;
  let mut max_score = 0;

  for i in arr {
    if i.eq("") {
      if max_score < score {max_score = score}
      score = 0
    } else {
      score += i.parse::<i32>().unwrap();
    } 
  }
  println!("{max_score}");
}

