import pytest

from calculator import add, divide, main, multiply, subtract


@pytest.mark.parametrize(
    ("operation", "first", "second", "expected"),
    [
        (add, 2, 3, 5),
        (add, -2, 0.5, -1.5),
        (subtract, 7, 4, 3),
        (subtract, 2, 5, -3),
        (multiply, 3, 4, 12),
        (multiply, -2, 3, -6),
        (divide, 8, 2, 4),
        (divide, 5, 2, 2.5),
    ],
)
def test_arithmetic_operations(operation, first, second, expected):
    assert operation(first, second) == expected


def test_divide_by_zero_raises_error():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(1, 0)


def test_main_handles_invalid_choice_and_runs_operation(monkeypatch, capsys):
    inputs = iter(["9", "1", "2", "3", "5"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(inputs))

    main()

    output = capsys.readouterr().out
    assert "Invalid option" in output
    assert "Add result: 5.0" in output
    assert "Goodbye!" in output


def test_main_handles_invalid_numbers_and_division_by_zero(monkeypatch, capsys):
    inputs = iter(["1", "not a number", "4", "8", "0", "5"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(inputs))

    main()

    output = capsys.readouterr().out
    assert "Please enter valid numbers." in output
    assert "Cannot divide by zero." in output
    assert "Goodbye!" in output