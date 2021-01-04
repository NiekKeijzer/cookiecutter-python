import subprocess


COMMANDS = [
    ('git', 'init'),
    ('poetry', 'install'),
    ('poetry', 'run', 'pre-commit', 'install')
]


def main():
    for cmd in COMMANDS:
        subprocess.run(cmd)


if __name__ == '__main__':
    main()
