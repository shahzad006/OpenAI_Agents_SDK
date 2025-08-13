# Swarm

Think of **Swarm** like a team of smart robots (agents) that each have their own special job.
- **Agents** = little smart workers (one good at math, one good at answering questions, one good at drawing).
- **Handoffs** = passing the job from one worker to another when needed.

Example:
If you ask, “How much is my bill and why is the internet slow?”
1. The **billing robot** answers the bill part.
2. Then it **hands you** to the **tech robot** to fix the internet part.

Swarm is **light and simple**, made for practicing and learning how these robot teams work together.


## What is the OpenAI Agents SDK?
The **Agents SDK** is like Swarm’s **big brother** — stronger, faster, and ready for real-world jobs.
It takes Swarm’s ideas and adds more powerful tools so big companies can use them.

### Design Patterns (fancy word for “ways to organize the team”)
These are like **teamwork strategies:**
1. **Prompt Chaining** – One robot does step 1, then gives the result to another robot for step 2, then step 3, etc. (like a relay race).
2. **Routing** – Send the question to the robot best suited for it.
3. **Parallelization** – Many robots work at the same time to finish faster.
4. **Orchestrator-Workers** – One “boss” robot gives tasks to other “worker” robots.
5. **Evaluator-Optimizer** – One robot checks the others’ work and tells them how to improve.

### 💡 Simple way to remember:
Swarm = training wheels for robot teamwork.  <br>

Agents SDK = the full racing bike with gears, brakes, and speed.




# Anthropic Design Patterns


OpenAI’s Agents SDK is a toolkit for building and managing AI agents that can work together to do complicated jobs. It matches well with ideas from Anthropic about how to design effective AI agents.

## 1. Prompt Chaining (Step-by-Step Workflow)
Break a big job into smaller, easier steps. Each step uses the result from the step before it. With the Agents SDK, you can set up agents that follow this step-by-step plan.

## 2. Routing
Send each task to the agent best suited to handle it. The SDK’s “handoff” feature lets one agent pass the job to another when needed.

## 3. Parallelization
Do several tasks at the same time to be faster. The SDK can run multiple agents in parallel and manage them all.

## 4. Orchestrator-Workers
Have one “boss” agent (the orchestrator) break a big task into smaller parts and give each part to “worker” agents. The orchestrator keeps track of progress and makes sure everything works together.

## 5. Evaluator-Optimizer
Have an “evaluator” agent check how well other agents are doing, then suggest ways to improve. The SDK’s guardrails feature helps create this feedback loop so the agents keep getting better.


By using these patterns, developers can make AI agents that are more **organized**, **efficient**, and **smart**.
