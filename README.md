# LLM-agentic
agentic workflow for LLMs

This repository contains code for a multi-agent framework that can be used for a variety of purposes, such as planning, finance, and marketing.

The framework consists of the following agents:

Manager agent: This agent is responsible for managing the other agents and for splitting tasks between them.
Planning agents: These agents are responsible for arguing with each other to make a plan.
Developer agents: These agents are responsible for working on the tasks that are assigned to them by the manager agent.
The framework works as follows:

The manager agent reads a complete planning conversation and decides on steps and splits tasks.
The manager agent sends a list of prompts and the agents to use to the developer agents.
The developer agents work on the tasks and reply to the manager agent with the program/script they worked on and separately with instructions.
The manager agent checks if all requirements are met. If not, it repeats the development process again.
If all requirements are met, the manager agent returns the new program data to the user.

# For contribution , please make a fork or issue
being honest , this is my first project on github , and i havent used it much , im just a first year student 
