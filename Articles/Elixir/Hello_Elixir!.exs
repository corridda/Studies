# Hello Elixir!
# https://levelup.gitconnected.com/hello-elixir-c7e49f7624e8

defmodule Cards do
	
	def create_deck do
	  cards = ["Ace", "Two", "Three", "Four", "Five"]
	  suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
	  for suit <- suits, card <- cards do
		"#{card} of #{suit} "
	  end
	end
	
	def save(deck, file_name) do
	  binary = :erlang.term_to_binary(deck)
	  File.write(file_name, binary)
	end
	
	def load(file_name) do
	  case File.read(file_name) do
		{:ok, binary} ->  :erlang.binary_to_term(binary)
		{:error, _reason} -> "That file does not exist"
	  end
	end
	
end