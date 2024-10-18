import pytest
from tkupchyn.homework_04.hashing_algorithm import group_words_by_checksum


words_list = [
    "Apple", "Journey", "River", "Cloud", "Tree", "Wisdom", "Ocean", "Freedom", "Candle", "Horizon",
    "Breeze", "Mountain", "Rain", "Silence", "Memory", "Shadow", "Feather", "Stone", "Light", "Forest",
    "Time", "Flame", "Dream", "Echo", "Star", "Harmony", "Desert", "Window", "Whisper", "Leaf",
    "Sky", "Snow", "Thunder", "Path", "Mirror", "Fire", "Sand", "Reflection", "Galaxy", "Sunset",
    "Moon", "Riverbank", "Rose", "Glow", "Meadow", "Flight", "Spark", "Shell", "Horizon", "Ink",
    "Jewel", "Pulse", "Wave", "Cliff", "Compass", "Lantern", "Cave", "Island", "Frost", "Glow",
    "Flame", "Dew", "Bird", "Petal", "Scent", "Thunder", "Wave", "Lantern", "Rainfall", "Forest",
    "Ocean", "Stream", "Breeze", "Firefly", "Twilight", "Stream", "Drift", "Vision", "Compass", "Shore",
    "Mist", "Pebble", "Rainstorm", "Starfall", "Echo", "Reflection", "Stone", "Mist", "Flower", "Sunrise",
    "Valley", "Peak", "Horizon", "Rainforest", "Shadow", "Song", "Silence", "Meadow", "Twilight", "Dream", "cat", "tac"
]


@pytest.mark.parametrize("list_of_words, groups_to_divide, word, group_contains_word",
                         (
                                 (words_list, 6, 'Cave', 5),
                                 (words_list, 3, 'Path', 0),
                                 (words_list, 10, 'Candle', 7),
                         ))
def test_group_words_by_checksum(list_of_words, groups_to_divide, word, group_contains_word):
    assert word in group_words_by_checksum(list_of_words, groups_to_divide)[group_contains_word]
