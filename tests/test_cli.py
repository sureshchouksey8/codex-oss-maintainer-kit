from oss_maintainer_kit.cli import main


def test_cli_fixture_outputs_text(capsys):
    exit_code = main(["--fixture", "tests/fixtures/sample_items.json", "--codex-prompt"])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Maintainer brief" in captured.out
    assert "Codex prompt" in captured.out
