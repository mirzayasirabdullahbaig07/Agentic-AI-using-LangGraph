"""
========================================================
        Agentic AI using LangGraph
========================================================

Author  : Mirza Yasir Abdullah Baig
Tech Stack:
- Python
- LangChain
- LangGraph
- Groq / OpenAI
- FastAPI
- Streamlit

========================================================
                    Introduction
========================================================

Agentic AI is the next evolution of Artificial Intelligence
where AI systems are capable of making decisions, planning
tasks, using tools, maintaining memory, and performing
multi-step workflows autonomously.

Unlike traditional Generative AI systems that only generate
responses based on prompts, Agentic AI systems can:

- Think step-by-step
- Use external tools and APIs
- Make decisions dynamically
- Perform actions autonomously
- Maintain memory
- Execute workflows
- Interact with humans when needed
- Retry and improve outputs

--------------------------------------------------------
            Generative AI vs Agentic AI
--------------------------------------------------------

Generative AI:
---------------
Traditional Generative AI systems focus mainly on generating
content such as:
- text
- images
- code
- summaries
- translations

Example:
A chatbot answering a question.

These systems are usually:
- reactive
- prompt-based
- single-step systems

--------------------------------------------------------

Agentic AI:
------------
Agentic AI systems go beyond simple response generation.

They can:
- plan tasks
- break problems into steps
- use tools
- call APIs
- search data
- interact with databases
- maintain memory
- execute workflows
- collaborate with humans

Example:
An AI Hiring Agent that:
1. Creates Job Descriptions
2. Posts jobs online
3. Screens resumes
4. Shortlists candidates
5. Schedules interviews

This involves:

- reasoning
- workflows
- memory
- tool usage
- decision making

--------------------------------------------------------
                What is LangGraph?
--------------------------------------------------------

LangGraph is a workflow orchestration framework built on
top of LangChain that helps developers build stateful,
multi-step AI agent systems.

It is specially designed for:
- Agentic AI
- AI workflows
- Human-in-the-loop systems
- Cyclic workflows
- Multi-agent systems
- Long-running AI processes

With LangGraph, developers can create:
- Sequential workflows
- Parallel workflows
- Conditional workflows
- Iterative workflows
- Stateful AI systems

--------------------------------------------------------
                Core Concepts
--------------------------------------------------------

1. State
---------
State stores shared information between nodes.

Example:
- user input
- generated output
- memory
- approval status

--------------------------------------------------------

2. Nodes
---------
Nodes are individual tasks/functions inside a workflow.

Example:
- Generate JD
- Review JD
- Send Email
- Fetch CVs

--------------------------------------------------------

3. Edges
---------
Edges connect nodes together.

They define:
- execution flow
- transitions
- workflow direction

--------------------------------------------------------

4. Conditional Edges
---------------------
Conditional edges help create decision-based systems.

Example:
IF approved:
    proceed forward

ELSE:
    regenerate response

--------------------------------------------------------

5. Human in the Loop (HITL)
----------------------------
Humans can approve, reject, or modify outputs before
the workflow continues.

This is critical for:
- hiring systems
- medical AI
- finance AI
- enterprise workflows

--------------------------------------------------------

6. Memory
----------
AI agents can maintain:
- short-term memory
- long-term memory
- conversational context
- workflow history

--------------------------------------------------------
            Why Learn Agentic AI?
--------------------------------------------------------

Agentic AI is becoming one of the most important fields in AI.

Companies are building:
- AI assistants
- autonomous agents
- workflow automation systems
- AI copilots
- enterprise AI systems

Learning Agentic AI provides skills in:
- AI orchestration
- workflow automation
- LLM engineering
- RAG systems
- tool integration
- AI memory systems
- production AI systems

--------------------------------------------------------
                Learning Objectives
--------------------------------------------------------

After completing this playlist/project, you should be able to:

- Understand Agentic AI systems
- Build workflows using LangGraph
- Create AI agents
- Implement memory systems
- Use tools and APIs
- Build RAG applications
- Add Human-in-the-loop systems
- Create production-ready AI workflows

--------------------------------------------------------
                Recommended Prerequisites
--------------------------------------------------------

Before learning LangGraph, basic knowledge of:

- Python
- APIs
- LangChain
- LLM fundamentals
- Prompt engineering

is recommended.

--------------------------------------------------------
                    Final Note
--------------------------------------------------------

Agentic AI is transforming software development by enabling
AI systems to think, plan, act, and collaborate autonomously.

LangGraph provides a powerful framework to build these
next-generation intelligent systems efficiently.

This repository/documentation is part of the learning
journey toward mastering Agentic AI engineering.

========================================================
"""