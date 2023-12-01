defmodule Extractor do
  def number_ext(line) do
    pattern = ~r/[0-9]/
    first = Regex.run(pattern, line) |> hd() || ""
    last = Regex.run(pattern, String.reverse(line)) |> hd() || ""
    first <> last |> String.to_integer()
  end

  # Is there a better way to do this?
  # There seems to be no Regex "backward" search first occurance
  # This is a very hacky way to do a reverse search
  @number_mapping %{
  "one" => "1", "two" => "2", "three" => "3", 
  "four" => "4", "five" => "5", "six" => "6", 
  "seven" => "7", "eight" => "8", "nine" => "9"
  }

  @rev_number_mapping %{
  "eno" => "1", "owt" => "2", "eerht" => "3", 
  "ruof" => "4", "evif" => "5", "xis" => "6", 
  "neves" => "7", "thgie" => "8", "enin" => "9"
  }

  def number_word_ext(line) do
    pattern = ~r/[0-9]|one|two|three|four|five|six|seven|eight|nine/
    rev_pattern = ~r/[0-9]|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin/
    first = Regex.run(pattern, line) |> hd() |> (&Map.get(@number_mapping, &1, &1)).() || ""
    last = Regex.run(rev_pattern, String.reverse(line)) |> hd() |> (&Map.get(@rev_number_mapping, &1, &1)).() || ""
    first <> last |> String.to_integer()
  end
end

contents = "input.txt"
  |> File.read!()
  |> String.split("\n", trim: true)

p1 = contents
  |> Enum.map(&Extractor.number_ext/1)
  |> Enum.reduce(0, &(&1 + &2))

p2 = contents
  |> Enum.map(&Extractor.number_word_ext/1)
  |> Enum.reduce(0, &(&1 + &2))

IO.inspect(p1)
IO.inspect(p2)
