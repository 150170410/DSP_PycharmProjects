
import argparse


parser = argparse.ArgumentParser(description='Run a Selenium test')
parser.add_argument('--browser_name',
                    dest='browser_name',
                    help='Browser to run tests on.',
                    choices=['Chrome'],
                    required=True)
parser.add_argument('--webdriver_path',
                    dest='webdriver_path',
                    help='Path to webdriver executable.',
                    required=True)
parser.add_argument('--webdriver_path_type',
                    dest='webdriver_path_type',
                    help='Type of path to use when determining webdriver_path.',
                    choices=['absolute', 'relative'],
                    default='relative')
parser.add_argument('--browser_version',
                    dest='browser_version',
                    help='Selenium test browser version.',
                    default='latest')
parser.add_argument('--test_dir',
                    dest='test_dir',
                    help='Path to directory containing tests. '
                         '(path type is based on value of --test_dir_path_type which defaults to relative)',
                    default='')
parser.add_argument('--test_dir_path_type',
                    dest='test_dir_path_type',
                    help='Type of path to use when determining test_dir location.',
                    choices=['absolute', 'relative'],
                    default='relative')
parser.add_argument('--results_dir',
                    dest='results_dir',
                    help='Path to directory to read/write results from/to.'
                         '(path type is based on value of --results_dir_path_type which defaults to relative)',
                    default='results')
parser.add_argument('--results_dir_path_type',
                    dest='results_dir_path_type',
                    help='Type of path to use when determining results_dir location.',
                    choices=['absolute', 'relative'],
                    default='relative')
parser.add_argument('--test_suites',
                    dest='test_suites',
                    help='Comma-separated test directories.')
parser.add_argument('--test_types',
                    dest='test_types',
                    help='Comma-separated list of test types to run (Ex: "Smoke", "Guide-Discovery")')
parser.add_argument('--pattern',
                    dest='pattern',
                    default='*test*.py',
                    help='Regular expression to filter which file patterns to regard as tests.')
parser.add_argument('--show_previous_results',
                    action='store_true',
                    help='Whether to combine the results of previous test runs for display at the end.')
parser.add_argument('--base_url',
                    dest='base_url',
                    help='Base url to use for tests.',
                    default='localhost:8080')
args = parser.parse_args()



def run_tests(start_dir, pattern, top_level_dir):
    print("Im from run_tests")