# A Facebook Messenger implementation of OpenAI's GPT-3

This is a Facebook application version of the Open AI's GPT-3 API: https://openai.com/blog/openai-api/

* It is coded to be a simple conversation implementation. It will respond to messages one at a time, and can not yet respond to images, links, gifs, or any other type of attachment. This implementation has a 'working memory' of 5 minutes - meaning that if it hasn't received a message within 5 minutes of your previous message, it's memory is wiped. This wiping could be considered as a 'conversation'. 

* Web hosting is on a Heroku server (https://www.heroku.com). The server has a CI/CD integration with this Github repository, such that any pushes to the 'main' branch result in a rebuilding of the web application.

<p align="center">
<img src="https://github.com/FlynnOwen/GPT-3-App/blob/main/img/GPT-3.gif)", alt="animated"/>
</p>

## Pre-requisites for usage:
* A Facebook account
* Administrator access to the Facebook Developer Application (request Flynn for this access - info@flynnowen.com)


