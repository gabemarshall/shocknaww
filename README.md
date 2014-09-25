shocknaww
=========

Simple script to check for CVE-2014-6271

### Example Usage

```
./shocknaww.py http://foo.bar/cgi-bin/foo
```

### Sample vulnerable environment

From the parent directory, run the following.

```
python -m CGIHTTPServer
```

Now use shocknaww against your localhost test server.

```
./shocknaww.py http://127.0.0.1:8000/test.py
```
