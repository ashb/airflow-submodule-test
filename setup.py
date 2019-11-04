# -*- coding: utf-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.


from setuptools import setup, find_packages, find_namespace_packages

long_description = ''


def do_main_setup():
    setup(
        name='notairflow',
        description='',
        long_description=long_description,
        long_description_content_type='text/markdown',
        license='Apache License 2.0',
        version='1.8.0',
        packages=find_packages(exclude=['tests*', 'notairflow/providers/*']),
        include_package_data=True,
        zip_safe=False,
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Topic :: System :: Monitoring',
        ],
        extras_require={
            'gcp': 'notairflow-providers-gcp',
        },
        test_suite='setup.airflow_test_suite',
        python_requires='>=3.5',
    )

def do_submodule_setup():
    setup(
        name='notairflow-providers-gcp',
        description='',
        long_description=long_description,
        long_description_content_type='text/markdown',
        license='Apache License 2.0',
        version='1.8.0',
        packages=find_namespace_packages(include=['notairflow.providers.gcp', 'notairflow.providers.gcp.*']),
        include_package_data=True,
        zip_safe=False,
        install_requires=['notairflow'],
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Topic :: System :: Monitoring',
        ],
        test_suite='setup.airflow_test_suite',
        python_requires='>=3.5',
    )


if __name__ == "__main__":
    import sys
    if sys.argv[1] == 'main':
        sys.argv[1:] = sys.argv[2:]
        do_main_setup()
    elif sys.argv[1] == 'gcp':
        sys.argv[1:] = sys.argv[2:]
        do_submodule_setup()
    else:
        print("Unknown submodule", sys.argv[1], file=sys.stderr)
        sys.exit(1)
