from pytest import ExitCode
from playsound import playsound


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    if exitstatus == ExitCode.TESTS_FAILED:
        playsound(r'tests\sounds\glass-shatter.wav')
    else:
        playsound(r'tests\sounds\ok.wav')


def pytest_keyboard_interrupt(excinfo):
    pass
