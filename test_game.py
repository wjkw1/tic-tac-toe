"""Unit testing the utility python class
    """
import pytest
from game import Game

import sys
sys.path.insert(0, './')


def test_init_game():
    game1 = Game()
    assert game1.state == [0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert game1.completed == False

def test_game_check_slot_available():
    game1 = Game([0, 0, 0, 0, 0, 0, 0, 0, 0])
    assert game1.check_slot_available()
    assert not game1.check_game_won()

    game2 = Game([1, 1, 1, 2, 2, 1, 2, 2, 1])
    assert not game2.check_slot_available()
    assert game2.check_game_won()
    

def test_insert_token():
    game1 = Game()
    game1.insert_token(0, 1)
    assert game1.state == [1, 0, 0, 0, 0, 0, 0, 0, 0]
    game1.insert_token(1, 2)
    assert game1.state == [1, 2, 0, 0, 0, 0, 0, 0, 0]
    game1.insert_token(2, 1)
    assert game1.state == [1, 2, 1, 0, 0, 0, 0, 0, 0]
    game1.insert_token(3, 2)
    assert game1.state == [1, 2, 1, 2, 0, 0, 0, 0, 0]
    game1.insert_token(4, 1)
    assert game1.state == [1, 2, 1, 2, 1, 0, 0, 0, 0]
    game1.insert_token(5, 2)
    assert game1.state == [1, 2, 1, 2, 1, 2, 0, 0, 0]
    game1.insert_token(6, 1)
    assert game1.state == [1, 2, 1, 2, 1, 2, 1, 0, 0]
    game1.insert_token(7, 2)
    assert game1.state == [1, 2, 1, 2, 1, 2, 1, 2, 0]
    game1.insert_token(8, 1)
    assert game1.state == [1, 2, 1, 2, 1, 2, 1, 2, 1]
    

def test_check_game_won():
    game2 = Game([1, 1, 1, 2, 2, 1, 2, 2, 1])
    assert game2.check_game_won()

    game1 = Game([0, 0, 0, 0, 0, 0, 0, 0, 0])
    assert not game1.check_game_won()
    game1.insert_token(0, 1)
    assert not game1.check_game_won()
    game1.insert_token(1, 2)
    assert not game1.check_game_won()
    game1.insert_token(2, 1)
    assert not game1.check_game_won()
    game1.insert_token(3, 2)
    assert not game1.check_game_won()
    game1.insert_token(4, 1)
    assert not game1.check_game_won()
    game1.insert_token(5, 2)
    assert not game1.check_game_won()
    game1.insert_token(6, 1)
    assert game1.check_game_won()

def test_insert_token_input_valid():
    game1 = Game([0, 0, 0, 0, 0, 0, 0, 0, 0])
    # test inserting the token is wrong
    with pytest.raises(TypeError):
        assert game1.insert_token(0, 'WICKED')
    with pytest.raises(ValueError):
        assert game1.insert_token(0, 3)

    # test the pos is wrong
    with pytest.raises(ValueError):
        assert game1.insert_token(-1, 1)
    with pytest.raises(ValueError):
        assert game1.insert_token(9, 1)
    with pytest.raises(TypeError):
        assert game1.insert_token("WICKED", 1)
