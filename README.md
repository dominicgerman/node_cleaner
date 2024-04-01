# node_cleaner

It's a well known fact that `node_modules` folders are some of the heaviest items in the observable universe:

![node_modules black hole meme](https://preview.redd.it/tfugj4n3l6ez.png?auto=webp&s=b8163176d8482d5e78ac631e16b7973a52e3b188)

I wrote this simple command line tool to autmatically delete `node_modules` folders from any project repos on my machine that haven't been updated in over a month.

The program recursively searches for `node_modules` folders within a root directory specified by the user. When a directory contains a `node_modules` folder, the program checks to see if any of the files in that directory have been modified in the past 30 days. If not, it recursively deletes the `node_modules` folder.

The program is run from a bash script and the 'root' directory path is set via an enviornment variable. I set up a cron job to run the script once a week.
