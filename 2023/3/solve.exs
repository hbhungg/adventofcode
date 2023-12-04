file = "test.txt"
  |> File.read!()
  |> String.split("\n", trim: true)

IO.inspect file
data = file
  |> Enum.map(&Regex.scan(~r/[^.\d]/, &1, return: :index) |> List.flatten())
  |> Enum.filter(&(!Enum.empty?(&1)))
  |> Enum.map(fn l -> 
    Enum.map(l, fn pos -> 
      {x, y} = pos
      IO.puts x
    end)
  end)
  # |> Enum.map(Enum.at(file, 2))
  # |> Enum.map(
  # |> Enum.map(&Regex.scan(~r/\d+/, &1, return: :index))
  # |> Enum.chunk_every(3, 1)

IO.inspect data
