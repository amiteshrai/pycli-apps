from click.testing import CliRunner

from apps.calculator.main import add


def test_add():
    runner = CliRunner()
    result = runner.invoke(add, "10 20")

    assert result.output == "Adding numbers 10 and 20\nSum is: 30\n"
    assert result.exit_code == 0
