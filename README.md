# literate-invention
Small python app that allows you to get some info from facebook .json message files

I made it mostly for fun and learning. It is my first app. In theory it should work fine with most languages, but I am not sure.

# It:
  1. Merges all the message files for simplicity's sake
  2. Fixes encoding in merged one(so main, facebook message files are untouched at all)
## Things you can do with this:
  * check how much specified word/sentence occured in your conversation 
  * check how much time you spent on call
  * how you how much messages you exchanged
  
## How do you use it?
  1. First you need to download facebook data.  
    * Go to facebook, **Settings**, **Your Facebook information**, and press **Download your information**.  
    * You need only messages, you don't need to download anything else.  
    * **MOST IMPORTANT THING - use format JSON**, if you will download html it is not going to work.
  2. After you download data, unpack it.
  3. Put the .exe file into message directory of person you want to use it on.
  4. Turn on .exe, it'll take few seconds at most.
  5. If you are in message directory it should instantly give you working directory, but if you want to be sure use **Browse** button.
  6. Press **Merge** and wait until you see "Merged!".
  7. Press **Fix encoding** and wait until you see "Fixed!"
  8. Count amount of words you want, count messages or get call duration.
    
### If you have any suggestions feel free to write them, right now I am thinking about:
  1. checking how much times specified word/sentence occured in ALL conversations, not only in one
  2. checking how much time specified person used specified word/sentence
  3. doing some graphs with mathplotlib
