## ChromeDriver mods

A modified version of ChromeDriver which does not check for the version of Chrome
that it is attempting to start and attach to. There are no guarantees that this
will not cause other problems, but it gets rid of the problem wherein Appium,
especially, cannot automate Chrome on an Android device because of version
incompatibility.

Try using this version of ChromeDriver (either by replacing the `build/chromedriver/mac/chromedriver`
binary in your Appium directory, or by setting the `chromedriver-executable` server
argument to the full path to the file in the `bin` directory of this repository)
if you are getting errors such as:

```shell
info: [debug] Spawning chromedriver with: /Users/isaac/code/appium/build/chromedriver/mac/chromedriver
info: [debug] [CHROMEDRIVER] Starting ChromeDriver (v2.11.298611 (d1120fdf51badec2f7b63a96e19a58d4783de84d)) on port 9515
Only local connections are allowed.
info: [debug] Making http request with opts: {"url":"http://127.0.0.1:9515/wd/hub/session","method":"POST","json":{"sessionId":null,"desiredCapabilities":{"chromeOptions":{"androidPackage":"com.android.chrome","androidDeviceSerial":"emulator-5554"}}}}
error: Chromedriver create session did not work. Status was 200 and body was {"sessionId":"4af7d0c1c67f143dc130b0e679ed4643","status":13,"value":{"message":"unknown error: Chrome version must be >= 36.0.1985.0\n  (Driver info: chromedriver=2.11.298611 (d1120fdf51badec2f7b63a96e19a58d4783de84d),platform=Mac OS X 10.9.5 x86_64)"}}
info: [debug] Cleaning up appium session
error: Failed to start an Appium session, err was: Error: Did not get session redirect from Chromedriver
info: [debug] Error: Did not get session redirect from Chromedriver
    at null.<anonymous> (/Users/isaac/code/appium/lib/devices/android/chromedriver.js:222:12)
    at Request._callback (/Users/isaac/code/appium/lib/devices/common.js:121:5)
    at Request.self.callback (/Users/isaac/code/appium/node_modules/request/request.js:121:22)
    at Request.EventEmitter.emit (events.js:98:17)
    at Request.<anonymous> (/Users/isaac/code/appium/node_modules/request/request.js:985:14)
    at Request.EventEmitter.emit (events.js:117:20)
    at IncomingMessage.<anonymous> (/Users/isaac/code/appium/node_modules/request/request.js:936:12)
    at IncomingMessage.EventEmitter.emit (events.js:117:20)
    at _stream_readable.js:920:16
    at process._tickDomainCallback (node.js:459:13)
info: [debug] Responding to client with error: {"status":33,"value":{"message":"A new session could not be created. (Original error: Did not get session redirect from Chromedriver)","origValue":"Did not get session redirect from Chromedriver"},"sessionId":null}
info: <-- POST /wd/hub/session 500 73343.079 ms - 214
```
