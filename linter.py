from SublimeLinter.lint import PythonLinter, util


class Bandit(PythonLinter):
    cmd = ('bandit@python', '${args}', '-n', '1', '-f', 'txt', '-')
    regex = (
        r'^>>\sIssue:\s\[(?P<code>[B]\d+):.+\]\s(?P<message>.+)$\r?\n'
        r'^.*Severity:\s(?:(?P<error>High)|(?P<warning>(Medium|Low))).*$\r?\n'
        r'^.*Location:.*:(?P<line>\d+)$\r?\n'
    )
    multiline = True
    error_stream = util.STREAM_BOTH
    config_file = ('--ini', '.bandit')
    defaults = {
        'selector': 'source.python'
    }
