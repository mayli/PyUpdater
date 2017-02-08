import logging
import os
import sys
import tarfile
import zipfile
import uuid

from dsdev_utils.system import get_system

log = logging.getLogger()

cmd1 = 'pyupdater pkg -P'
cmd2 = 'pyupdater pkg -S'
home_dir = os.path.dirname(os.path.abspath(__file__))


def build(app):
    cmd = ('pyupdater build -F --clean --path={} '
           '--app-version={} {}'.format(home_dir, app[1], app[0]))
    os.system(cmd)


def extract(filename):
    ext = os.path.splitext(filename)[1]
    if ext == '.zip':
        archive = zipfile.ZipFile(filename, 'r')
    else:
        archive = tarfile.open(filename, 'r:gz')

    archive.extractall()


def main():
    scripts = [('app_restart_01.py', '4.1'), ('app_restart_02.py', '4.2')]

    # In unittest, the upgrade clients are running concurrently, and will have
    # race condition reading/writing files since they share the same
    # update_folder. Let's randomized the company name to avoid that.
    config_path = os.path.join(home_dir, 'client_config.py')
    config_text = open(config_path, 'rt').read()
    config_text = config_text.replace('Digital', 'Digital' + uuid.uuid4())
    open(config_path, 'wt').write(config_text)

    # We use this flag to untar & move our binary to the
    # current working directory
    first = True
    for s in scripts:
        build(s)
        if first:
            if sys.platform == 'win32':
                ext = '.zip'
            else:
                ext = '.tar.gz'

            # Build path to archive
            archive_path = os.path.join('pyu-data', 'new',
                                        'Acme-{}-4.1{}'.format(get_system(),
                                                               ext))

            if not os.path.exists(archive_path):
                sys.exit(1)

            # We extract the Acme binary here. When we call pyupdater pkg -P
            # the Acme binary will be moved to the deploy folder. In our test
            # (test_pyupdater.TestExecution.test_execution_update_*) we
            # move all of the files from the deploy directory to the cwd
            # of the test runner.
            extract(archive_path)

            first = False

        os.system(cmd1)

    os.system(cmd2)


if __name__ == '__main__':
    main()
