import pylint.lint
from pylint.reporters.text import TextReporter

def analyze_code(files):
    pylint_reports = []
    for file in files:
        # Initialize Pylint linter
        linter = pylint.lint.PyLinter()
        
        # Load Pylint plugins
        linter.load_default_plugins()
        
        # Analyze the file
        linter.check(file)

        # Generate detailed report
        reporter = TextReporter()
        pylint_output = linter.generate_reports([reporter])
        
        pylint_reports.append((file, pylint_output))
    return pylint_reports
