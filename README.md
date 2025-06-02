# Documenation Suggestion giver(Task 1)
In this project i implement an ai agent that can scrape any article (under https://help.moengage.com/hc/en-us/articles/...) and provide suggestion. This is the task 1 of the given assignment.
## Table of Content
- [Project demonstraction wxamples](#project-demonstraction)
- [Tech stack](#tech-stack)
- [How to run](#how-to-run)
- [Implementation](#implementation)
- [Challenges Faced](#challenges-faced)

## Project demonstraction
### 1. Example
**link**: https://help.moengage.com/hc/en-us/articles/115002571883-Suggest-a-Feature

```
curl http://localhost:8000/suggestion?url=https://help.moengage.com/hc/en-us/articles/115002571883-Suggest-a-Feature
```

<details>
<summary>Readability(click me)</summary>
Flesch-Kincaid reading ease score: -34.37. 
The score is bad as a higher score indicates easier readability.

Provide score is good or bad: Bad

Give your overall rating of the readability of the article based on given ratings and reviews. 
Readability Rating (as a Non-Technical Marketer): 8/10

List all sentences that you, as a non-technical marketer, find difficult to understand (if any). Organize them under appropriate headings.

## How Does This Help?
* "Each month, the product team and stakeholders at MoEngage review the top5-10 customer requests and respond to them personally." 
  * Suggested rephrase: "Each month, the product team and stakeholders at MoEngage review the top 5-10 customer requests and respond to them personally."
* "To get your requests into these prioritization meetings, provide all the required details on the Submit a request page."
  * Suggested rephrase: "To get your requests into these prioritization meetings, please ensure you provide all required details on the Submit a request page. [screenshot: Submit a request page](file_name.png)"

## Submit a Product Idea
* "6. In the **Current workaround \\& what problems you are facing** field, enter your current workaround (if you have one) and current problems. You can provide any other details that will help build a case for why this is an important request to you. (This is optional.)"
  * Suggested rephrase: "6. In the **Current workaround \\& what problems you are facing** field, enter your current workaround (if you have one) and current problems. You can add any additional details that will help us understand why this feature is important to you. (This is optional.)"

## Feature Status
* "This request was not clear, already exists, or is not in alignment with where we are taking our product."
  * Suggested rephrase: "This request was declined because it was unclear, already exists, or doesn’t align with our product roadmap."

## Your Feedback
* "Only .jpeg, .png files below1MB"
  * Suggested rephrase: "Please upload only .jpeg or .png files, and ensure they are under 1MB in size."

These suggested rephrases aim to make the text more readable and understandable for non-technical marketers. Including screenshots, as mentioned, can also enhance comprehension.
</details>

<br>

<details>

<summary>Completeness(click me)</summary>
**Overview**

The article provides a general overview of the feature request system in MoEngage, but it lacks detailed information on how to suggest a feature, what types of features can be suggested, and how the suggestions are prioritized. Based on the reviews of each section, the overall completeness rating of the article is **6.8/10**.

**Does the article provide enough detail for a user to understand and implement the feature or concept?**

No, the article does not provide enough detail for a user to fully understand and implement the feature or concept. While it provides a general overview of the feature request system, it lacks specific details on how to suggest a feature, what types of features can be suggested, and how the suggestions are prioritized.

**Sections that require examples and what type of example needed**

The following sections require examples:

1. **Suggest a Feature**: An example of a suggested feature, such as "For instance, you can suggest a new feature to enhance user segmentation or improve campaign analytics."
2. **How Does This Help?**: An example of a scenario where a user's feature suggestion was implemented, such as "For example, a customer suggested a feature to integrate MoEngage with a popular CRM platform. Our product team reviewed the request, prioritized it, and eventually implemented the integration, which benefited multiple customers."
3. **Submit a Product Idea**: An example of a well-written product idea submission, including a clear title, detailed description, and relevant product area selection.
4. **Feature Status**: An example of a scenario where a user submits a feature request and it moves through different statuses (e.g., from "Awaiting Feedback" to "Planned" to "Released").
5. **How can we improve this article?**: A screenshot of where the feature status link can be found or an example of how to use it.

These examples would help illustrate the process and make it more relatable to the user, providing a better understanding of the feature request system in MoEngage.

</details>

<br>

<details>
<summary>Structure(click me)</summary>
**Overview**

The article's flow and structure have been reviewed, and the overall rating is 8/10. The reviews suggest that the article is well-structured and easy to follow, but some sections lack detailed information and could benefit from more context.

**Section Suggestions**

* **Suggest a Feature**: The paragraph size is too long and should be broken down into a list format for better clarity.
* **How Does This Help?**: The first paragraph is too short and could be merged with the second paragraph for better flow.
* **Feature Status**: The paragraph size is too short, and more detailed explanations and examples should be provided. A brief introduction or explanation before the list would provide context on why this feature status section is important and how it relates to the overall setup process.

**Headings/Subheadings Review**

* The headings and subheadings seem to enable logical content flow and easy navigation.
* The sequence of sections, from "How Does This Help?" to "Submit a Product Idea" and then "Feature Status", appears logical.

**Answers to Questions**

1. **Does the information flow logically from section to section?**: Yes, the information flows logically from section to section.
2. **Is it easy to navigate and find specific information?**: Yes, it is easy to navigate and find specific information.

However, some improvements can be made:

* Consider adding a brief introduction to the "Suggest a Feature" section to explain how it fits into the overall onboarding and initial setup process.
* Provide more detailed explanations and examples in the "Feature Status" section to improve clarity.

No significant changes are needed in the heading/subheading structure. The current structure appears to support easy navigation and logical content flow.
</details>

<br>

<details>
<summary>Style guide(click me)</summary>
**Overview of the article alignment with style guide:**\n\nThe article \"Suggest a Feature\" has an overall rating of 8/10 in terms of alignment with the style guide. The sections are clear and concise, and they effectively guide the user through the process of suggesting a feature and understanding the feature status. However, there are some areas that can be improved to make the article more customer-focused, clear, and concise.\n\n**Overall Rating:** 8/10\n\n**Sections that are not very aligned to the style guide:**\n\n1. **Suggest a Feature**\n\t* Voice and Tone: 7/10 (It's clear but can be more engaging)\n\t* Clarity and Conciseness: 9/10 (It's concise and to the point)\n\t* Action-oriented language: 6/10 (It's informative but can be more directive)\n\t* Suggestion: Consider adding a brief description of how the feature request system works and what kind of features are being considered. Use a more active voice, e.g., \"Suggest a feature and help shape the future of MoEngage\" instead of \"MoEngage provides you with a feature request system...\"\n\t* Example: \"Suggest a Feature and Help Shape the Future of MoEngage. We want to hear from you! Use our feature request system to share your ideas and help us build a better product. [Suggest a Feature](link to feature request system)\"\n2. **How Does This Help?**\n\t* Suggestion: The first sentence could be more concise. Instead of \"MoEngage values your suggestions and keeps you in the loop when we review or update your ideas or requests,\" consider \"We value your input and keep you updated on your suggestions.\"\n\t* Example: \"We value your input and keep you updated on your suggestions. By suggesting a feature, you can: ... \"\n3. **Feature Statuslink**\n\t* Suggestion: The section can benefit from a brief introduction that explains why understanding feature statuses is important for the user. Simplify some sentences to make the language more concise.\n\t* Example: \"Understanding the status of your feature requests helps you track the progress of your ideas and plan accordingly. ... \"\n\n**Reasonable suggestions:**\n\n* Use a more active voice throughout the article to make it more engaging and customer-focused.\n* Add brief descriptions to explain complex concepts, such as how the feature request system works.\n* Use clear and concise language to make the article easy to understand.\n* Add call-to-action (CTA) buttons or links to make it easy for users to access the feature request system or provide feedback.\n* Consider rephrasing technical terms, such as \"Feature Statuslink\", to make it more customer-friendly.
</details>

<br>
<details>
<summary>Original Response(click me)</summary>

```
{
    "readability": "Flesch-Kincaid reading ease score: -34.37. \nThe score is bad as a higher score indicates easier readability.\n\nProvide score is good or bad: Bad\n\nGive your overall rating of the readability of the article based on given ratings and reviews. \nReadability Rating (as a Non-Technical Marketer): 8/10\n\nList all sentences that you, as a non-technical marketer, find difficult to understand (if any). Organize them under appropriate headings.\n\n## How Does This Help?\n* \"Each month, the product team and stakeholders at MoEngage review the top5-10 customer requests and respond to them personally.\" \n  * Suggested rephrase: \"Each month, the product team and stakeholders at MoEngage review the top 5-10 customer requests and respond to them personally.\"\n* \"To get your requests into these prioritization meetings, provide all the required details on the Submit a request page.\"\n  * Suggested rephrase: \"To get your requests into these prioritization meetings, please ensure you provide all required details on the Submit a request page. [screenshot: Submit a request page](file_name.png)\"\n\n## Submit a Product Idea\n* \"6. In the **Current workaround \\\\& what problems you are facing** field, enter your current workaround (if you have one) and current problems. You can provide any other details that will help build a case for why this is an important request to you. (This is optional.)\"\n  * Suggested rephrase: \"6. In the **Current workaround \\\\& what problems you are facing** field, enter your current workaround (if you have one) and current problems. You can add any additional details that will help us understand why this feature is important to you. (This is optional.)\"\n\n## Feature Status\n* \"This request was not clear, already exists, or is not in alignment with where we are taking our product.\"\n  * Suggested rephrase: \"This request was declined because it was unclear, already exists, or doesn’t align with our product roadmap.\"\n\n## Your Feedback\n* \"Only .jpeg, .png files below1MB\"\n  * Suggested rephrase: \"Please upload only .jpeg or .png files, and ensure they are under 1MB in size.\"\n\nThese suggested rephrases aim to make the text more readable and understandable for non-technical marketers. Including screenshots, as mentioned, can also enhance comprehension.",

    "structure": "**Overview**\n\nThe article's flow and structure have been reviewed, and the overall rating is 8/10. The reviews suggest that the article is well-structured and easy to follow, but some sections lack detailed information and could benefit from more context.\n\n**Section Suggestions**\n\n* **Suggest a Feature**: The paragraph size is too long and should be broken down into a list format for better clarity.\n* **How Does This Help?**: The first paragraph is too short and could be merged with the second paragraph for better flow.\n* **Feature Status**: The paragraph size is too short, and more detailed explanations and examples should be provided. A brief introduction or explanation before the list would provide context on why this feature status section is important and how it relates to the overall setup process.\n\n**Headings/Subheadings Review**\n\n* The headings and subheadings seem to enable logical content flow and easy navigation.\n* The sequence of sections, from \"How Does This Help?\" to \"Submit a Product Idea\" and then \"Feature Status\", appears logical.\n\n**Answers to Questions**\n\n1. **Does the information flow logically from section to section?**: Yes, the information flows logically from section to section.\n2. **Is it easy to navigate and find specific information?**: Yes, it is easy to navigate and find specific information.\n\nHowever, some improvements can be made:\n\n* Consider adding a brief introduction to the \"Suggest a Feature\" section to explain how it fits into the overall onboarding and initial setup process.\n* Provide more detailed explanations and examples in the \"Feature Status\" section to improve clarity.\n\nNo significant changes are needed in the heading/subheading structure. The current structure appears to support easy navigation and logical content flow.",

    "completeness": "**Overview**\n\nThe article provides a general overview of the feature request system in MoEngage, but it lacks detailed information on how to suggest a feature, what types of features can be suggested, and how the suggestions are prioritized. Based on the reviews of each section, the overall completeness rating of the article is **6.8/10**.\n\n**Does the article provide enough detail for a user to understand and implement the feature or concept?**\n\nNo, the article does not provide enough detail for a user to fully understand and implement the feature or concept. While it provides a general overview of the feature request system, it lacks specific details on how to suggest a feature, what types of features can be suggested, and how the suggestions are prioritized.\n\n**Sections that require examples and what type of example needed**\n\nThe following sections require examples:\n\n1. **Suggest a Feature**: An example of a suggested feature, such as \"For instance, you can suggest a new feature to enhance user segmentation or improve campaign analytics.\"\n2. **How Does This Help?**: An example of a scenario where a user's feature suggestion was implemented, such as \"For example, a customer suggested a feature to integrate MoEngage with a popular CRM platform. Our product team reviewed the request, prioritized it, and eventually implemented the integration, which benefited multiple customers.\"\n3. **Submit a Product Idea**: An example of a well-written product idea submission, including a clear title, detailed description, and relevant product area selection.\n4. **Feature Status**: An example of a scenario where a user submits a feature request and it moves through different statuses (e.g., from \"Awaiting Feedback\" to \"Planned\" to \"Released\").\n5. **How can we improve this article?**: A screenshot of where the feature status link can be found or an example of how to use it.\n\nThese examples would help illustrate the process and make it more relatable to the user, providing a better understanding of the feature request system in MoEngage.",

    "style_guide": "**Overview of the article alignment with style guide:**\n\nThe article \"Suggest a Feature\" has an overall rating of 8/10 in terms of alignment with the style guide. The sections are clear and concise, and they effectively guide the user through the process of suggesting a feature and understanding the feature status. However, there are some areas that can be improved to make the article more customer-focused, clear, and concise.\n\n**Overall Rating:** 8/10\n\n**Sections that are not very aligned to the style guide:**\n\n1. **Suggest a Feature**\n\t* Voice and Tone: 7/10 (It's clear but can be more engaging)\n\t* Clarity and Conciseness: 9/10 (It's concise and to the point)\n\t* Action-oriented language: 6/10 (It's informative but can be more directive)\n\t* Suggestion: Consider adding a brief description of how the feature request system works and what kind of features are being considered. Use a more active voice, e.g., \"Suggest a feature and help shape the future of MoEngage\" instead of \"MoEngage provides you with a feature request system...\"\n\t* Example: \"Suggest a Feature and Help Shape the Future of MoEngage. We want to hear from you! Use our feature request system to share your ideas and help us build a better product. [Suggest a Feature](link to feature request system)\"\n2. **How Does This Help?**\n\t* Suggestion: The first sentence could be more concise. Instead of \"MoEngage values your suggestions and keeps you in the loop when we review or update your ideas or requests,\" consider \"We value your input and keep you updated on your suggestions.\"\n\t* Example: \"We value your input and keep you updated on your suggestions. By suggesting a feature, you can: ... \"\n3. **Feature Statuslink**\n\t* Suggestion: The section can benefit from a brief introduction that explains why understanding feature statuses is important for the user. Simplify some sentences to make the language more concise.\n\t* Example: \"Understanding the status of your feature requests helps you track the progress of your ideas and plan accordingly. ... \"\n\n**Reasonable suggestions:**\n\n* Use a more active voice throughout the article to make it more engaging and customer-focused.\n* Add brief descriptions to explain complex concepts, such as how the feature request system works.\n* Use clear and concise language to make the article easy to understand.\n* Add call-to-action (CTA) buttons or links to make it easy for users to access the feature request system or provide feedback.\n* Consider rephrasing technical terms, such as \"Feature Statuslink\", to make it more customer-friendly."
}
```
</details>

### Example 2

**link**: https://help.moengage.com/hc/en-us/articles/360000347066-Tracking-Users-in-Flows%23h_01HV6692KWH361Q3RPX3SQ1RHN
```
curl http://localhost:8000/suggestion?url=https://help.moengage.com/hc/en-us/articles/360000347066-Tracking-Users-in-Flows%23h_01HV6692KWH361Q3RPX3SQ1RHN
```

<details>
<summary>Readablity(click me)</summary>
Flesch-Kincaid reading ease score: -20.91. 
The score indicates that the article's readability is very difficult. This score is bad.

Overall rating of the readability of the article: 7/10

## Tracking Users in Flows

* Difficult to understand sentences:
	+ "Visualize User Trips in Flows" - This sentence is unclear. 
	+ "Conversion Attribution in Flows" - This term may be unfamiliar to non-technical marketers.
* Suggested alternatives:
	+ "Visualize User Trips in Flows: This feature allows you to see the journey of users through your flows, helping you understand their behavior and identify areas for improvement."
	+ Define technical terms like "Conversion Attribution in Flows" to improve readability.

## Tracking Users Who Entered a Flow

* Difficult to understand sentences:
	+ "The event is tracked for each entry done by a user." 
	+ "By filtering using **With control group \\=** **True**, ..."
* Suggested alternatives:
	+ "The event is triggered every time a user enters the flow."
	+ Provide a brief explanation of what "control group" means in this context.

## Tracking Users Who Converted

* Difficult to understand sentences:
	+ "The event is tracked for each conversion, so if a user performs the conversion multiple times during their flow trip, this event will be raised for each recorded conversion and also for each of the defined goals."
	+ "By filtering using **Flow Id**, you can find the list of unique users whose conversion was attributed to this flow."
* Suggested alternatives:
	+ "Every time a user converts, we track it. If a user converts multiple times, we'll track each conversion."
	+ "Use the flow's unique ID to find users who converted because of that specific flow."

## Tracking Users Who Exited a Flow

* Difficult to understand sentences:
	+ "The event is tracked for each exit done by a user."
	+ "By filtering using **Flow Id**, you can find the list of unique users whose conversion was attributed to this flow."
* Suggested alternatives:
	+ "The 'User Exited Flow' event is triggered every time a user exits a flow."
	+ Explain the term "conversion" for non-technical marketers.

## Privacy Preference Center

* Difficult to understand sentences:
	+ "When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies."
	+ "The information does not usually directly identify you, but it can give you a more personalized web experience."
* Suggested alternatives:
	+ "Cookies are small files that help websites remember your preferences. They can help us provide a more tailored experience for you, but you can choose to limit their use."
	+ Provide examples to illustrate how cookies work and how they can personalize the user experience.

## Manage Consent Preferences

* Difficult to understand sentences:
	+ "They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms."
	+ "They help us to know which pages are the most and least popular and see how visitors move around the site."
* Suggested alternatives:
	+ "These cookies are set when you take actions like logging in or submitting forms."
	+ "These cookies help us understand which pages are most visited and how users navigate our site."

## Privacy Preference Centerlink > Cookie List

* Difficult to understand sentences:
	+ The presence of `dialog closed` in the text seems out of place and unclear in its context.
	+ The use of technical terms like "Powered by Onetrust" and "Cookie Consent"
* Suggested alternatives:
	+ Provide a brief explanation of what "Powered by Onetrust" means and its relevance to the platform.
	+ Clarify the purpose of the "Privacy Preference Centerlink" and its connection to the cookie list.
</details>

<br>

<details>
<summary>Completeness(click me)</summary>
**Overview**

The article "Tracking Users in Flows" has been reviewed for completeness, and the overall rating is 6.5/10. The article provides some information on tracking users in flows, but it lacks detailed explanations and practical examples to make it easier for non-technical marketers to understand and implement the features.

**Does the article provide enough detail for a user to understand and implement the feature or concept?**

No, the article does not provide enough detail for a user to understand and implement the feature or concept. The sections lack concrete examples, and some sections appear to be incomplete or unrelated to the topic.

**Sections that require examples and what type of example needed**

The following sections require examples:

1. **Tracking Users in Flows**
	* Type of example needed: A step-by-step guide on how to track users in flows, including screenshots or a real-life scenario.
2. **Tracking Users Who Entered a Flow**
	* Type of example needed: A concrete example of how to use the "Flow Id" or "Flow Name" to segment users who entered a specific flow, including screenshots or a step-by-step guide.
3. **Tracking Users Who Converted**
	* Type of example needed: A concrete example with actual values for the event attributes (e.g., Flow Id, Version Name, Campaign Id), including screenshots or a visual representation of the segmentation process.
4. **Tracking Users Who Exited a Flow**
	* Type of example needed: A concrete example of how to use the filters in a real-world scenario, such as "Find users who exited a flow due to not completing a purchase within a certain time frame".
5. **Manage Consent Preferences**
	* Type of example needed: An example of how user tracking works in a flow, including how cookies are used to identify and track users, and what kind of data is collected.

The following sections are incomplete or unrelated to the topic:

1. **How can we improve this article?** ( appears to be a feedback submission form)
2. **Privacy Preference Center** (unrelated to the topic of tracking users in flows)
3. **Cookie List** (appears to be incomplete and unrelated to the topic)
</details>

<br>

<details>
<summary>Structure(click me)</summary>
**Overview:** 
The article's flow and structure have room for improvement, with a rating of 6/10. The reviews suggest that some sections have long paragraphs that need to be broken down, while others lack relevant content. The use of lists and tables is effective in presenting information, but some sections seem misplaced or incomplete.

**Section Suggestions:**

* **Tracking Users in Flows:** This section seems to be misplaced or incorrectly included, with content related to cookie policies. It needs to be rewritten to focus on tracking users in flows, with a brief paragraph of 1-2 sentences and the use of lists (e.g., bullet points) to improve clarity.
* **Tracking Users Who Entered a Flow:** The first paragraph is a bit long and could be broken up into two paragraphs for easier reading.
* **Tracking Users Who Converted:** The second paragraph is a bit long and contains a table, which might make it harder to read. Consider breaking it up into shorter paragraphs.
* **Tracking Users Who Exited a Flow:** The section seems to be incomplete or misplaced, with content that appears to be a generic feedback form. It needs to be rewritten to focus on the topic, with relevant information and possibly the use of lists or tables to improve clarity.

**Headings/Subheadings Review:**

* The headings and subheadings seem to enable logical content flow, with a clear hierarchy of information: "Tracking Users in Flows" as an introductory section, followed by "Tracking Users Who Entered a Flow," "Tracking Users Who Converted," and "Tracking Users Who Exited a Flow."
* However, the content of "Tracking Users in Flows" seems out of place and should be revised or removed.

**Does the information flow logically from section to section?**
 Mostly, yes. The sections on tracking users who entered, converted, or exited a flow seem to follow a logical sequence. However, the introductory section "Tracking Users in Flows" seems misplaced.

**Is it easy to navigate and find specific information?**
 Mostly, yes. The use of clear headings and subheadings helps navigation. However, the incomplete or misplaced sections might make it harder to find specific information.

**Improvement Suggestions:**

* Revise or remove the "Tracking Users in Flows" section to ensure it provides a clear introduction to the topic.
* Break up long paragraphs in sections like "Tracking Users Who Entered a Flow" and "Tracking Users Who Converted."
* Rewrite the "Tracking Users Who Exited a Flow" section to focus on the topic and include relevant information.
</details>

<br>

<details>
<summary>Style guide(click me)</summary>
**Overview of the article alignment with style guide: 7.2/10**\n\nThe article provides useful information on tracking users in flows, but there are areas that need improvement to align with the style guide. The sections that are not very aligned with the style guide are:\n\n1. **Tracking Users Who Exited a Flowlink > How can we improve this article?**\n\t* Rating: 2/10\n\t* Suggestions:\n\t\t+ Remove the feedback form from this section and place it at the end of the article or provide a separate link for users to provide feedback.\n\t\t+ Add relevant information on how to track users who exited a flow link, such as definition, importance, steps to track, and metrics to analyze.\n\t* Example: Rephrase the section to provide clear instructions on how to track users who exited a flow link.\n\n2. **Privacy Preference Centerlink**\n\t* Rating: 4/10\n\t* Suggestions:\n\t\t+ Rephrase the section to focus on how user privacy preferences and cookie settings might impact the use of the MoEngage platform.\n\t\t+ Simplify complex sentences and technical terms.\n\t* Example: Rewritten section: \"To ensure accurate tracking of users in flows, please note that MoEngage uses cookies to personalize the user experience. You can manage your cookie preferences to allow or block certain types of cookies.\"\n\n3. **Privacy Preference Centerlink > Manage Consent Preferences**\n\t* Rating: 4/10\n\t* Suggestions:\n\t\t+ Use a more customer-focused tone and language.\n\t\t+ Simplify complex sentences and technical terms.\n\t\t+ Break down the text into shorter paragraphs and use bullet points or numbered lists.\n\t* Example: Rewritten text: \"**Manage Your Cookie Preferences**: We use cookies on our website to provide a better experience. Here's what you need to know: ...\"\n\n4. **Privacy Preference Centerlink > Cookie List**\n\t* Rating: 2/10\n\t* Suggestions:\n\t\t+ Rephrase the section heading to be more descriptive and concise.\n\t\t+ Simplify the language used to explain the cookie consent management system.\n\t\t+ Provide clear instructions on how to use the section.\n\t* Example: Rewritten section: \"**Manage Cookie Preferences**: We want to ensure you're comfortable with the cookies we use. Please review and manage your preferences below.\"\n\nThe sections that are well-aligned with the style guide are:\n\n1. **Tracking Users Who Entered a Flow**\n\t* Rating: 8/10\n2. **Tracking Users Who Converted**\n\t* Rating: 8/10\n3. **Tracking Users Who Exited a Flow**\n\t* Rating: 8/10\n\nThese sections provide clear and concise information, and the language is customer-focused. However, there are still some suggestions for improvement, such as adding brief introductions, breaking up long sentences, and using more action-oriented language.
</details>

<br>

<details>
<summary>Original Json Response(click me)</summary>



```
{
    "readability": "Flesch-Kincaid reading ease score: -20.91. \nThe score indicates that the article's readability is very difficult. This score is bad.\n\nOverall rating of the readability of the article: 7/10\n\n## Tracking Users in Flows\n\n* Difficult to understand sentences:\n\t+ \"Visualize User Trips in Flows\" - This sentence is unclear. \n\t+ \"Conversion Attribution in Flows\" - This term may be unfamiliar to non-technical marketers.\n* Suggested alternatives:\n\t+ \"Visualize User Trips in Flows: This feature allows you to see the journey of users through your flows, helping you understand their behavior and identify areas for improvement.\"\n\t+ Define technical terms like \"Conversion Attribution in Flows\" to improve readability.\n\n## Tracking Users Who Entered a Flow\n\n* Difficult to understand sentences:\n\t+ \"The event is tracked for each entry done by a user.\" \n\t+ \"By filtering using **With control group \\\\=** **True**, ...\"\n* Suggested alternatives:\n\t+ \"The event is triggered every time a user enters the flow.\"\n\t+ Provide a brief explanation of what \"control group\" means in this context.\n\n## Tracking Users Who Converted\n\n* Difficult to understand sentences:\n\t+ \"The event is tracked for each conversion, so if a user performs the conversion multiple times during their flow trip, this event will be raised for each recorded conversion and also for each of the defined goals.\"\n\t+ \"By filtering using **Flow Id**, you can find the list of unique users whose conversion was attributed to this flow.\"\n* Suggested alternatives:\n\t+ \"Every time a user converts, we track it. If a user converts multiple times, we'll track each conversion.\"\n\t+ \"Use the flow's unique ID to find users who converted because of that specific flow.\"\n\n## Tracking Users Who Exited a Flow\n\n* Difficult to understand sentences:\n\t+ \"The event is tracked for each exit done by a user.\"\n\t+ \"By filtering using **Flow Id**, you can find the list of unique users whose conversion was attributed to this flow.\"\n* Suggested alternatives:\n\t+ \"The 'User Exited Flow' event is triggered every time a user exits a flow.\"\n\t+ Explain the term \"conversion\" for non-technical marketers.\n\n## Privacy Preference Center\n\n* Difficult to understand sentences:\n\t+ \"When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies.\"\n\t+ \"The information does not usually directly identify you, but it can give you a more personalized web experience.\"\n* Suggested alternatives:\n\t+ \"Cookies are small files that help websites remember your preferences. They can help us provide a more tailored experience for you, but you can choose to limit their use.\"\n\t+ Provide examples to illustrate how cookies work and how they can personalize the user experience.\n\n## Manage Consent Preferences\n\n* Difficult to understand sentences:\n\t+ \"They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms.\"\n\t+ \"They help us to know which pages are the most and least popular and see how visitors move around the site.\"\n* Suggested alternatives:\n\t+ \"These cookies are set when you take actions like logging in or submitting forms.\"\n\t+ \"These cookies help us understand which pages are most visited and how users navigate our site.\"\n\n## Privacy Preference Centerlink > Cookie List\n\n* Difficult to understand sentences:\n\t+ The presence of `dialog closed` in the text seems out of place and unclear in its context.\n\t+ The use of technical terms like \"Powered by Onetrust\" and \"Cookie Consent\"\n* Suggested alternatives:\n\t+ Provide a brief explanation of what \"Powered by Onetrust\" means and its relevance to the platform.\n\t+ Clarify the purpose of the \"Privacy Preference Centerlink\" and its connection to the cookie list.",

    "structure": "**Overview:** \nThe article's flow and structure have room for improvement, with a rating of 6/10. The reviews suggest that some sections have long paragraphs that need to be broken down, while others lack relevant content. The use of lists and tables is effective in presenting information, but some sections seem misplaced or incomplete.\n\n**Section Suggestions:**\n\n* **Tracking Users in Flows:** This section seems to be misplaced or incorrectly included, with content related to cookie policies. It needs to be rewritten to focus on tracking users in flows, with a brief paragraph of 1-2 sentences and the use of lists (e.g., bullet points) to improve clarity.\n* **Tracking Users Who Entered a Flow:** The first paragraph is a bit long and could be broken up into two paragraphs for easier reading.\n* **Tracking Users Who Converted:** The second paragraph is a bit long and contains a table, which might make it harder to read. Consider breaking it up into shorter paragraphs.\n* **Tracking Users Who Exited a Flow:** The section seems to be incomplete or misplaced, with content that appears to be a generic feedback form. It needs to be rewritten to focus on the topic, with relevant information and possibly the use of lists or tables to improve clarity.\n\n**Headings/Subheadings Review:**\n\n* The headings and subheadings seem to enable logical content flow, with a clear hierarchy of information: \"Tracking Users in Flows\" as an introductory section, followed by \"Tracking Users Who Entered a Flow,\" \"Tracking Users Who Converted,\" and \"Tracking Users Who Exited a Flow.\"\n* However, the content of \"Tracking Users in Flows\" seems out of place and should be revised or removed.\n\n**Does the information flow logically from section to section?**\n Mostly, yes. The sections on tracking users who entered, converted, or exited a flow seem to follow a logical sequence. However, the introductory section \"Tracking Users in Flows\" seems misplaced.\n\n**Is it easy to navigate and find specific information?**\n Mostly, yes. The use of clear headings and subheadings helps navigation. However, the incomplete or misplaced sections might make it harder to find specific information.\n\n**Improvement Suggestions:**\n\n* Revise or remove the \"Tracking Users in Flows\" section to ensure it provides a clear introduction to the topic.\n* Break up long paragraphs in sections like \"Tracking Users Who Entered a Flow\" and \"Tracking Users Who Converted.\"\n* Rewrite the \"Tracking Users Who Exited a Flow\" section to focus on the topic and include relevant information.",

    "completeness": "**Overview**\n\nThe article \"Tracking Users in Flows\" has been reviewed for completeness, and the overall rating is 6.5/10. The article provides some information on tracking users in flows, but it lacks detailed explanations and practical examples to make it easier for non-technical marketers to understand and implement the features.\n\n**Does the article provide enough detail for a user to understand and implement the feature or concept?**\n\nNo, the article does not provide enough detail for a user to understand and implement the feature or concept. The sections lack concrete examples, and some sections appear to be incomplete or unrelated to the topic.\n\n**Sections that require examples and what type of example needed**\n\nThe following sections require examples:\n\n1. **Tracking Users in Flows**\n\t* Type of example needed: A step-by-step guide on how to track users in flows, including screenshots or a real-life scenario.\n2. **Tracking Users Who Entered a Flow**\n\t* Type of example needed: A concrete example of how to use the \"Flow Id\" or \"Flow Name\" to segment users who entered a specific flow, including screenshots or a step-by-step guide.\n3. **Tracking Users Who Converted**\n\t* Type of example needed: A concrete example with actual values for the event attributes (e.g., Flow Id, Version Name, Campaign Id), including screenshots or a visual representation of the segmentation process.\n4. **Tracking Users Who Exited a Flow**\n\t* Type of example needed: A concrete example of how to use the filters in a real-world scenario, such as \"Find users who exited a flow due to not completing a purchase within a certain time frame\".\n5. **Manage Consent Preferences**\n\t* Type of example needed: An example of how user tracking works in a flow, including how cookies are used to identify and track users, and what kind of data is collected.\n\nThe following sections are incomplete or unrelated to the topic:\n\n1. **How can we improve this article?** ( appears to be a feedback submission form)\n2. **Privacy Preference Center** (unrelated to the topic of tracking users in flows)\n3. **Cookie List** (appears to be incomplete and unrelated to the topic)",

    "style_guide": "**Overview of the article alignment with style guide: 7.2/10**\n\nThe article provides useful information on tracking users in flows, but there are areas that need improvement to align with the style guide. The sections that are not very aligned with the style guide are:\n\n1. **Tracking Users Who Exited a Flowlink > How can we improve this article?**\n\t* Rating: 2/10\n\t* Suggestions:\n\t\t+ Remove the feedback form from this section and place it at the end of the article or provide a separate link for users to provide feedback.\n\t\t+ Add relevant information on how to track users who exited a flow link, such as definition, importance, steps to track, and metrics to analyze.\n\t* Example: Rephrase the section to provide clear instructions on how to track users who exited a flow link.\n\n2. **Privacy Preference Centerlink**\n\t* Rating: 4/10\n\t* Suggestions:\n\t\t+ Rephrase the section to focus on how user privacy preferences and cookie settings might impact the use of the MoEngage platform.\n\t\t+ Simplify complex sentences and technical terms.\n\t* Example: Rewritten section: \"To ensure accurate tracking of users in flows, please note that MoEngage uses cookies to personalize the user experience. You can manage your cookie preferences to allow or block certain types of cookies.\"\n\n3. **Privacy Preference Centerlink > Manage Consent Preferences**\n\t* Rating: 4/10\n\t* Suggestions:\n\t\t+ Use a more customer-focused tone and language.\n\t\t+ Simplify complex sentences and technical terms.\n\t\t+ Break down the text into shorter paragraphs and use bullet points or numbered lists.\n\t* Example: Rewritten text: \"**Manage Your Cookie Preferences**: We use cookies on our website to provide a better experience. Here's what you need to know: ...\"\n\n4. **Privacy Preference Centerlink > Cookie List**\n\t* Rating: 2/10\n\t* Suggestions:\n\t\t+ Rephrase the section heading to be more descriptive and concise.\n\t\t+ Simplify the language used to explain the cookie consent management system.\n\t\t+ Provide clear instructions on how to use the section.\n\t* Example: Rewritten section: \"**Manage Cookie Preferences**: We want to ensure you're comfortable with the cookies we use. Please review and manage your preferences below.\"\n\nThe sections that are well-aligned with the style guide are:\n\n1. **Tracking Users Who Entered a Flow**\n\t* Rating: 8/10\n2. **Tracking Users Who Converted**\n\t* Rating: 8/10\n3. **Tracking Users Who Exited a Flow**\n\t* Rating: 8/10\n\nThese sections provide clear and concise information, and the language is customer-focused. However, there are still some suggestions for improvement, such as adding brief introductions, breaking up long sentences, and using more action-oriented language."
}
```
</details>

## Tech Stack
I have used python to implement the ai agent.
1. Selenium: To fetch the article html.
2. Beautiful Soup: For extracting article from html
3. Langchain and Langgraph: To Build the Agent.
4. LLM api: Used [groq api](https://console.groq.com/docs/models)
5. Docker: To containerize and run the application in an isolated environment.


## How to Run

System Requirement: **Docker** must be installed on you machine
- With reference of `agent/.env.example` make `agent/.env` file and add groq api key.
- In terminal make you current dir as root of this repo and run following command:
```
$ docker compose up
```

- The agent server will listen at http://localhost:8000/

- Make get request with url
```
curl http://localhost:8000/suggestion?url=https://help.moengage.com/hc/en-us/articles/360042322691-User-Attribute-Profile-Integration-Validation
```
Note: it take about 4-5 min to load the response
## Implementation
1. Visit MoEngage article URL (https://help.moengage.com/hc/en-us/articles/...). It then downloads the article HTML content. 
2. Converts article from html to markdown format.
3. *Ai agent execution*: The same agent is executed interatively for each criterion provided in the assignment, wtih corresponding criterion prompt. Following operation are perform inside the agent:

    a. **Split_article:** Article is split into section based on heading.

    b. **Generate_reviews:** For each section, review based on criterion is generated with use of llm.

    c. **Get readability score:** Calculate Flesch-Kincaid reading ease score on the article.

    d. **Generate final review:** All reviews generate for sections and consolidated and final review generate using llm.

![alt text](graph.png)

## Challenges faced
- Prompt Sensitivity: LLM responses varied based on minor prompt changes, requiring tuning for consistency.

- Rate Limits: LLM API rate limits hit due to multiple api calls, t avoid the rate of api hit is decreased that leads to shower response generation.