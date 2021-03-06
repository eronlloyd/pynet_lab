# Week 2 Exercises

## 1. Python Libraries
a. Make sure that you have PySNMP and Paramiko installed in the lab (i.e.
enter the Python shell and test 'import pysnmp', and 'import paramiko').

   b. Determine which version of PySNMP and Paramiko are installed. dir(pysnmp)
and dir(paramiko) should be helpful here.

c. Write a simple Python module that contains one function that prints
'hello' (module name = my_func.py). Do a test where you import my_func into a
new Python script. Test this using the following contexts:
* my_func.py is located in the same directory as your script
* my_func.py is located in some random subdirectory (not the same directory as your script)
* my_func.py is located in ~/applied_python/lib/python2.7/site-packages/

## 2. telnetlib
a. Write a script that connects using telnet to the pynet-rtr1 router. Execute
the 'show ip int brief' command on the router and return the output. Try to do
this on your own (i.e. do not copy what I did previously). You should be able
to do this by using the following items:

    telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    remote_conn.read_until(<string_pattern>, TELNET_TIMEOUT)
    remote_conn.read_very_eager() remote_conn.write(<command> + '\n')
    remote_conn.close()

## 3. telnetlib (optional - challenge question)
Convert the code that I wrote here to a class-based solution (i.e. convert over
from functions to a class with methods).

## 4. SNMP Basics
a. Create an 'SNMP' directory in your home directory using
    ```
    $ mkdir SNMP
    $ cd SNMP```

b. Verify that you can import the snmp_helper library. This is a small library
that I created to simplify aspects of PySNMP.
    ```$ python
    Python 2.7.5 (default, Feb 11 2014, 07:46:25)
    [GCC 4.8.2 20140120 (Red Hat 4.8.2-13)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    >>> import snmp_helper```

c. Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2) and
prints out both the MIB2 sysName and sysDescr.
