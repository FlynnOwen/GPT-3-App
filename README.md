<h1 align="center"> OpenAI's GPT-3 Messenger </h1>


<img align="right" width="500" height="550" src="img/GPT-3.gif"/>

<h2 align="center"> About: </h2>
This is a Messenger app of Open AI's [GPT-3 API](https://openai.com/blog/openai-api/)

Here is the relevant [Facebook application](https://www.facebook.com/The-All-Knowing-One-103780238591514)

Web hosting is on a [Heroku server](https://www.heroku.com) with CI/CD pipeline of rebuilding upon pushes to 'main' branch.

<h2 align="center"> Usage: </h2>
* Requires a Facebook account
* Requires administrator access to the Facebook Developer Application (request Flynn for this access - info@flynnowen.com)
*  It is coded to be a simple conversation implementation. It will respond to messages one at a time, and can not yet respond to images, links, gifs, or any other type of attachment. This implementation has a 'working memory' of 5 minutes - meaning that if it hasn't received a message within 5 minutes of your previous message, it's memory is wiped. This wiping could be considered as a conversation. 

## Notes:
I've stumbled across the adaptor design pattern (https://en.wikipedia.org/wiki/Adapter_pattern) - which this repository could be considered as (a conversational messenger adaptor for GPT-3)

