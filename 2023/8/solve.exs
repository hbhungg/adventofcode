file = "input.txt"
  |> File.read!
  |> String.split("\n", trim: true)

[ ins | data ] = file
ins = ins
data = data
  |> Enum.map(&Regex.scan(~r/\w+/, &1))
  |> Enum.reduce(%{}, fn x, acc -> 
    [[k] | v] = x
    v = v 
      |> List.flatten
    v = %{l: Enum.at(v, 0), r: Enum.at(v, 1)}
    Map.put(acc, k, v)
  end)

defmodule Camel do
  def traverse(_, curr, _, _) when curr == "ZZZ", do: 0
  def traverse(g, curr, ins, i) do
    x = Map.get(g, curr)
    ii = String.at(ins, i)
    curr = case ii do
      "R" -> Map.get(x, :r)
      "L" -> Map.get(x, :l)
    end
    1 + Camel.traverse(g, curr, ins, rem(i+1, String.length(ins)))
  end
end
IO.inspect ins
IO.inspect data
IO.inspect Camel.traverse(data, "AAA", ins, 0)
