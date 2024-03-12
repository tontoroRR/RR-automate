from pytest import ExitCode
from playsound import playsound


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    if exitstatus == ExitCode.TESTS_FAILED:
        playsound('tests\\sounds\\glass-shatter.wav')

def pytest_keyboard_interrupt(excinfo):
    # todo: doesn't work
    playsound('tests/sounds/glass-shatter.wav')
