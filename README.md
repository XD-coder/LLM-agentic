# LLM-agentic
agentic workflow for LLMs (without langchain)

This repository contains code for a multi-agent framework that is specialised for programming purposes.

# MAIN GOAL
Make a framework that can run all long as pausible (logging each iteration) and be independent of user input to make a better program.
It can independently enhance on its knowledge base about documentations , new packages, useful tools.

The framework consists of the following agents:

- Manager agent: This agent is responsible for managing the other agents and for splitting tasks between them.
- Planning agents: These agents are responsible for arguing with each other to make a plan.
- Research agents : These agents are responsible for reading plans and researching important stuff such as documentations for API(s)
- Developer agents: These agents are responsible for working on the tasks that are assigned to them by the manager agent.

The framework works as follows:

- The manager agent reads a complete planning conversation and decides on steps and splits tasks.
- The manager agent sends a list of prompts and the agents to use to the developer agents.
- The developer agents work on the tasks and reply to the manager agent with the program/script they worked on and separately with instructions.
- The manager agent checks if all requirements are met. If not, it repeats the development process again.
- If all requirements are met, the manager agent returns the new program data to the user.

# For contribution , please make a fork or issue
PS: being honest , this is my first project on github , and i havent used it much , im just a first year student .
- if submiting code , please make sure it have comments to describe what it is used for.
