defmodule Day7 do
  def solve() do
    lines = File.stream!("puzzle.txt")
      |> Stream.map(&String.trim/1)
      |> Enum.to_list()

    n = String.length(Enum.at(lines, 0))

    start_idx = Enum.at(lines, 0)
      |> String.graphemes()
      |> Enum.find_index(&(&1 == "S"))

    init_beams = %{start_idx => "|"}
    init_ans = 0

    {_f_beams, f_ans} =
      Enum.reduce(lines, {init_beams, init_ans}, fn line, {beams_above, acc_ans} ->
        Enum.reduce(0..(n - 1), {%{}, acc_ans}, fn idx, {next_row, cur_ans} ->
          cur_char = String.at(line, idx)
          has_beam = Map.has_key?(beams_above, idx)

          if has_beam do
            cond do
              cur_char == "^" ->
                updated_next = cond do
                  idx == 0 -> Map.put(next_row, 1, "|")
                  idx == n - 1 -> Map.put(next_row, n - 2, "|")
                  true -> next_row |> Map.put(idx - 1, "|") |> Map.put(idx + 1, "|")
                end
                {updated_next, cur_ans + 1}

              cur_char == "." or cur_char == "S" ->
                {Map.put(next_row, idx, "|"), cur_ans}

              true ->
                {next_row, cur_ans}
            end
          else
            {next_row, cur_ans}
          end
        end)
      end)

    f_ans
  end
end

IO.puts Day7.solve()
