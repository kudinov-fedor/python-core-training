from setuptools import setup, find_packages
from setuptools.command.install import install


class ClassTriggeredOnInstall(install):

    user_options = install.user_options + [
        ('flag', None, 'Some flag'),
        ('param1=', None, 'Some param')
    ]

    def initialize_options(self):
        install.initialize_options(self)
        self.flag = None
        self.param1 = None

    def finalize_options(self):
        install.finalize_options(self)

    def run(self):
        install.run(self)
        if self.flag:
            print("flag is True")
            self.do_smth()

    def do_smth(self):
        print(self.param1)


if __name__ == '__main__':
    setup(
        name="name",
        version="1.0.0.0",
        author="fkudinov",
        description="My Great Package",
        include_package_data=True,
        packages=find_packages(),
        install_requires=[
            'pytest==7.2.1'
        ],
        extras_require={
            'extra1': ['requests'],
            'test': ['pytest==7.0.1', 'pytest-mock==3.6.1', 'flake8==4.0.1'],
        },
        cmdclass={
            'install': ClassTriggeredOnInstall,
        }
    )
