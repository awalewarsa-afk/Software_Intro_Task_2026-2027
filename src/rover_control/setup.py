from setuptools import find_packages, setup

package_name = 'rover_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    description='ROS 2 rover joint control',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'manual_control = rover_control.manual_control:main',
            'dance = rover_control.dance:main',
        ],
    },
)
