from setuptools import setup
from glob import glob

package_name = 'slambot_visualisation'

setup(
    name=package_name,
    version='0.0.0',
    packages=[],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/display_launch.py']),
        ('share/' + package_name + '/URDF', ['URDF/slambot.urdf']),
        ('share/slambot_visualisation/rviz', glob('rviz/*.rviz')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Peter Wallhead',
    maintainer_email='peter.wallhead@gmail.com',
    description='URDF visualization and robot state publishing for Slambot.',
    license='MIT',
)