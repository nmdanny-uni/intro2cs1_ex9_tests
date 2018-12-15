import tempfile
import json
from subprocess import Popen, PIPE

# These don't test the 'game' class itself(as there isn't much to test),
# they test the entire game

PYTHON_PROC_ARGS = ["python", "../game.py"]


def create_car_config(cars_dict):
    with tempfile.NamedTemporaryFile(delete=False) as file:
        file.write(bytes(json.dumps(cars_dict), 'UTF-8'))
        return file.name


def assert_finishes_with_moves(cfg_file, moves):
    """
    Ensures that the game finishes after consuming all given moves(no more and no less)

    :param cfg_file: Path to a car_config.json file
    :param moves: List of strings in the form "R,r" and such
    """
    proc_args = PYTHON_PROC_ARGS + [cfg_file]
    # hacky way of determining if the game terminates after exactly all moves
    # were given:

    # first, we expect an EOF error, as we haven't won yet and the game should ask for another step.
    failing_moves = "\n".join(moves[:-1])
    _out, err = Popen(proc_args, text=True, stdin=PIPE, stderr=PIPE).communicate(failing_moves)
    assert "EOF" in err, "Game terminated too early, before all valid moves were given. "

    # now, we expect no error(graceful termination of the game) after all valid moves have been given.
    success_moves = "\n".join(moves)
    _out, err = Popen(proc_args, text=True, stdin=PIPE, stderr=PIPE).communicate(success_moves)
    assert len(err) == 0, "Game did not terminate successfully after giving all valid moves."


def test_valid_simple():
    cars = {
        "R": [2,[3,0],1],
        "O": [3,[1,4],0]
    }

    cfg_file = create_car_config(cars)
    assert_finishes_with_moves(cfg_file, ["O,u"] + ["R,r"] * 6)

