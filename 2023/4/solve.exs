data = "input.txt"
  |> File.read!()
  |> String.split("\n", trim: true)
  |> Enum.map(&String.split(&1, ":") |> List.last())
  |> Enum.map(&String.split(&1, "|"))
  |> Enum.map(fn x -> Enum.map(x, &Regex.scan(~r/\d+/, &1) 
                      |> List.flatten() 
                      |> Enum.map(fn i -> i |> String.replace(~r/\s/, "") |> String.to_integer() end) 
                      |> MapSet.new())
              end)
  |> Enum.map(fn x -> [a, b] = x 
      MapSet.intersection(a, b) |> MapSet.size() 
      # MapSet.intersection(a, b)
  end)

p1 = data
  |> Enum.map(fn x -> if x > 0, do: 2**(x-1), else: x end)
  |> Enum.sum()

p2 = data
  |> Enum.with_index
  |> Enum.map(fn {k,v} -> {v+1, (if k>0, do: Enum.to_list(v+2..v+k+1), else: [])} end) |> Map.new

defmodule SpawnCard do
  def winr(card, _wins, stop) when card >= stop, do: 0
  def winr(card, wins, stop) do
    # IO.inspect card
    Map.get(wins, card)
      |> Enum.map(fn x -> 1 + SpawnCard.winr(x, wins, stop) end)
      |> Enum.sum()
  end
end

# IO.inspect data
# IO.inspect p1
# IO.inspect p2

v = 1..map_size(p2)
  |> Enum.map(&SpawnCard.winr(&1, p2, map_size(p2)))
  |> Enum.sum()
IO.inspect v+map_size(p2)

