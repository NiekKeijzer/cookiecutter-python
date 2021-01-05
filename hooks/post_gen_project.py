import os
import subprocess


COMMANDS = [
    ('git', 'init'),
    ('poetry', 'install'),
    ('poetry', 'run', 'pre-commit', 'install'),
    ('git', 'add', '.'),
    ('git', 'commit', '-m', 'Initial commit 👶')
]


def create_gitea_repo() -> None:
    import giteapy
    import yaml

    config_file = os.path.expanduser('~/.tea/tea.yml')
    with open(config_file) as in_file:
        yaml_config = yaml.safe_load(in_file)

    if not isinstance(yaml_config, dict) or \
            'logins' not in yaml_config or \
            len(yaml_config['logins']) == 0:
        raise RuntimeError(f'Missing or invalid Tea config file {config_file}')

    if len(yaml_config['logins']) == 1:
        login = yaml_config['logins'][0]
    else:
        raise RuntimeError("Multiple Tea logins found")

    config = giteapy.Configuration()
    config.host = login['url']
    if not config.host.endswith('/api/v1'):
        config.host += '/api/v1'
    config.api_key['access_token'] = login['token']

    client = giteapy.ApiClient(config)
    admin = giteapy.AdminApi(client)

    repo = giteapy.CreateRepoOption(
        name='{{ cookiecutter.project_name }}',
        description='{{ cookiecutter.project_description }}',
        private='{{ cookiecutter.license }}'.lower() == 'proprietary',
        auto_init=False,
    )

    resp = admin.admin_create_repo(login['name'], repo)
    COMMANDS.append(
        ('git', 'remote', 'add', 'origin', resp.clone_url),
    )


def main() -> None:
    if '{{ cookiecutter.create_repo }}'.lower() == 'y':
        create_gitea_repo()

    for cmd in COMMANDS:
        subprocess.run(cmd)


if __name__ == '__main__':
    main()
