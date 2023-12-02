contents =
  "input.txt"
  |> File.read!()
  |> String.split("\n", trim: true)

defmodule Count do
  def count_color(game) do
    game
    |> Enum.map(fn x -> Regex.scan(~r/\b\d+\b\s\w+/, x) |> List.flatten() end)
    |> Enum.map(fn x ->
      Enum.reduce(x, %{}, fn x, acc ->
        [n, c] = String.split(x, " ")
        n = String.to_integer(n)
        Map.update(acc, String.to_atom(c), n, &max(&1, n))
      end)
    end)
  end

  def possible(set) do
    Map.get(set, :red, 0) <= 12 && Map.get(set, :blue, 0) <= 14 && Map.get(set, :green, 0) <= 13
  end
end

p1 =
  contents
  |> Enum.map(&(String.split(&1, ":") |> Enum.at(1)))
  |> Enum.map(&String.split(&1, ";"))
  |> Enum.map(&Count.count_color/1)
  |> Enum.with_index()
  |> Enum.reduce(0, fn { ele, idx }, acc -> 
      if Enum.reduce(ele, true, fn i, a -> a && Count.possible(i) end) do
        acc + (idx + 1) 
      else 
        acc
      end
    end)


IO.inspect(p1)
