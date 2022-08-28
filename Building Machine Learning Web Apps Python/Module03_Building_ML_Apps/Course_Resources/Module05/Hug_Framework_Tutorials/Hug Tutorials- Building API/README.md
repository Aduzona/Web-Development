## Building An API,CLI and Package with Hug

### Hug
+  A simple framework for API development that exposes your code in 3 different interface

#### Hug Exposes Your Code as
+ Local Package
+ API
+ CLI

#### Hug uses these decorator to perform such
```python
@hug.local() # ==> For Local Package
@hug.get() # ==> As API
@hug.cli() # ==> As CLI
```

