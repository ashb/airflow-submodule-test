===============================================
Testing python submodules for Airflow providers
===============================================

To build the packages::

   python ./setup.py main bdist_wheel
   python ./setup.py gcp bdist_wheel



To install::

   pip install --find-links ./dist/ 'notairflow'
   pip install --find-links ./dist/ 'notairflow[gcp]'


Test that the code from both init files is run::

   $ python -c 'import notairflow.providers.gcp, notairflow; notairflow.greet()'

..

   | /Users/ash/code/python/airflow-submodule-test/notairflow/__init__.py module level code running
   | /Users/ash/code/python/airflow-submodule-test/notairflow/providers/gcp/__init__.py module level code running
   | Hello
