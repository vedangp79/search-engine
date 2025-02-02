# GEN AI P5 Chatbot Feedback

### Example: Describe the bot UI Design that we had to use because of Maizey limitations. {: #Q01}
- [ ] Yum
- [x] Yuk

## Background

### How many ULCS courses has group member 1 taken including the current semester? {: #Q02}
2
### How many ULCS courses has group member 2 taken including the current semester? {: #Q03}
1 (0 if only 1 group member)
### How many ULCS courses has group member 3 taken including the current semester? {: #Q04}
1 (0 if only 1-2 group members)

## General
### Approximately how many interactions did you have with the bot on project 5? {: #Q05}
- [ ] 0-3
- [x] 4-10
- [ ] 11-50
- [ ] 51+

### Mark all the topics where the bot was helpful: {: #Q06}
- [ ] Spec questions
- [ ] Design
- [ ] Debugging
- [x] Conceptual questions
- [ ] Explaining test cases
- [ ] Setup / toolchain
- [ ] Implementation / code suggestions

### Would a similar bot be helpful for other projects? {: #Q07}
- [x] Yes
- [ ] No
- [ ] Unsure

### Our group used the bot instead of posting on Piazza {: #Q08}
- [ ] Never
- [ ] Rarely
- [x] Sometimes
- [ ] Often
- [ ] Always

### Our group used the bot instead of going to Office Hours {: #Q09}
- [ ] Never
- [ ] Rarely
- [x] Sometimes
- [ ] Often
- [ ] Always

### Using the bot instead of Piazza or Office Hours saved time {: #Q10}
- [x] Yes
- [ ] No
- [ ] Unsure

### The bot gave more helpful answers than ChatGPT {: #Q11}
#### (Reminder: Course policy permits the use of generative AI for projects (https://eecs485.org/syllabus.html#generative-ai-copilot-chatgpt))
- [ ] Never
- [ ] Rarely
- [x] Sometimes
- [ ] Often
- [ ] Always
- [ ] I did not use ChatGPT

### Given the choice, which bot would you prefer to use for project help? {: #Q12}
- [ ] EECS485 bot (Reducey)
- [ ] ChatGPT
- [x] Both
- [ ] Neither

### Please explain your answer to the previous question. {: #Q13}
ChatGPT is better at explaining general concepts, while the bot
is better with spec related questions

#### (Optional) Overall, do you have any feedback on the bot? {: #Q14}
No

## Interaction 1
### Prompt {: #Q15}
explain me the project

### Response {: #Q16}
Reducey here, to assist you with your understanding of the project!


The project involves writing a MapReduce-like framework. Conceptually, Program this framework follows four main stages to process large data sets:



Segmenting the Input: In this initial phase, large input data is broken up into smaller segments that can be processed in parallel. It prepares the work to be divided among different worker nodes.

### Was this response helpful? {: #Q17}
- [x] Yes
- [ ] No

### To the best of your knowledge, did it answer your question correctly: {: #Q18}
- [x] Yes
- [ ] No
- [ ] Unsure

### (Optional) Anything else you want to tell us about this interaction? {: #Q19}
No

## Interaction 2
### Prompt {: #Q20}
explain the mapping stage

### Response {: #Q21}
Mapping Phase (Map): The mapping stage is a user-provided function. For each segment of input, the map function processes the data and produces intermediate key-value pairs. These key-value pairs are then ready for grouping.

### Was this response helpful? {: #Q22}
- [x] Yes
- [ ] No

### To the best of your knowledge, did it answer your question correctly: {: #Q23}
- [x] Yes
- [ ] No
- [ ] Unsure

### (Optional) Anything else you want to tell us about this interaction? {: #Q24}
No

## Interaction 3
### Prompt {: #Q25}
explain the grouping phase

### Response {: #Q26}
Grouping Phase (Group): The mapping phase's output is assorted so that all intermediate values associated with the same intermediate key are grouped together. Although not explicitly mentioned as a standalone phase in every implementation of MapReduce-like frameworks, this stage prepares the data for the subsequent reducing step.

### Was this response helpful? {: #Q27}
- [x] Yes
- [ ] No

### To the best of your knowledge, did it answer your question correctly: {: #Q28}
- [x] Yes
- [ ] No
- [ ] Unsure

### (Optional) Anything else you want to tell us about this interaction? {: #Q29}
No