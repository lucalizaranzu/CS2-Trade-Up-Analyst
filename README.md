Welcome to the CS2 trade up sniper. There are a few parts to this project that are important to know:

If you wish to run the server yourself, PostgreSQL is required, along with alterante steam accounts. Once you have a database, link it in the csfloatinspect config file. Currently, you can run the bot client without the server because the IP is set to my home server's. Please don't release it to the public.

*EDIT you will not be able to run the server yourself. The config files required are too large to fit into a vocareum submission so Ive removed them.

For EE250 grading, the bulk of this project lives in bot_client/index.js. csfloatinspect is an external library that I modified to fit my needs. This project is designed to be run natively on an RPi, Connect an RGB LED to GPIO pins 17,27, and 22 (R,G,B) for it to work.

You will need to install puppeteer and point the chromepath variable in index.js to have it work correctly.

You MUST use a version of node that is compatible. It is recommended to use version 18.

List of libraries used:

CSFloatInspect
Puppeteer
Steam-User
Axios


Done by Luca Lizaranzu and Riley Milligan