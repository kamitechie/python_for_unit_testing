import pytest
import exercises


def test_exercise_reverse_name():
    assert exercises.exercise_reverse_name("John Smith") == "htimS nhoJ"
    assert exercises.exercise_reverse_name("ANNA TAO") == "OAT ANNA"


def test_exercise_file_ext():
    assert exercises.exercise_file_ext('main.py') == 'py'
    assert exercises.exercise_file_ext('file.png') == 'png'
    assert exercises.exercise_file_ext('FILE.html') == 'html'


