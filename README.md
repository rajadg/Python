Python
======

**Python samples and utils**

----

Contains multiple python projects:
- Some projects are **utilities** and *re-usable*.
- Some projects are simple **samples** *for learning*.
 
  - **PySamples**
    - Contains sample python code used for target practice
    - Will keep adding more code
    - Currently available
      - **windows dialog** using *Qt4* framework
  - **PyUtils**
    - Contains utility code for re-use
    - Will keep adding more utility code
    - Currently available
      - **Developer** package
        - **JsonSerializer** serializes a given python object in json format
        - **test** package : contains code to test *JsonSerializer* class
        - *Example*

          ```python
          from Developer.JsonSerializer import JsonSerializer
          serializer = JsonSerializer('    ', True, True)
          print 'json data => ' +serializer.var_to_json('myObj', myObj, 2)
          ```



-----
