
Net-SNMP off-by-one stack overflow



Tested with latest version https://github.com/net-snmp/net-snmp
```
static u_char  *
smux_open_process(int fd, u_char * ptr, size_t * len, int *fail)
{
	...
	string_len = SMUXMAXSTRLEN;
[1]    if ((ptr = asn_parse_string(ptr, len, &type, (u_char *) descr,
                                &string_len)) == NULL) {
        DEBUGMSGTL(("smux", "[smux_open_process] descr parse failed\n"));
        *fail = TRUE;
        return ((ptr += *len));
    }
[2]    descr[string_len] = 0;

	...
}
```

string_len could be set to max value on line #1,
it will lead to off-by-one overflow on line #2


How to reproduce:
```
1. add the following lines to snmpd.conf
smuxpeer .1.3.6.1.2.1.14 password
smuxsocket 192.168.1.40

2. run t1.py
$ ./t1.py
```

asan log attached.
