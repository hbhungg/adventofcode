file = "input.txt"
  |> File.read!
  |> String.split("\n", trim: true)

data = file
  |> Enum.map(&Regex.scan(~r/\d+/, &1))

data1 = for {a, b} <- Enum.zip(Enum.at(data, 0), Enum.at(data, 1) || []), do: {String.to_integer(hd(a)), String.to_integer(hd(b))}

data2 = data
  |> Enum.map(fn x -> Enum.join(x) |> String.to_integer end)
  |> List.to_tuple

defmodule Win do
  def race(record) do
    record 
      |> Enum.reduce(1, fn {t, d}, p ->
        p * Enum.reduce(1..t, 0, fn val, acc ->
          if val * (t - val) > d, do: acc + 1, else: acc
        end)
      end)
    end
end

IO.inspect Win.race(data1)
IO.inspect Win.race([data2])
