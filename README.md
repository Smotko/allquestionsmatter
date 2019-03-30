# Rooted

In this project, we are trying to address two challenges from the PixelsCamp partners:
**Hack for Good** from *Fundação Calouste Gulbenkian*, in the category of [*Integration of Refugees and Migrants*](https://pixels.camp/hackathon/hack-for-good_integration-of-refugees-and-migrants) and **Worten's** [*Social Reponsability Mission Market](https://pixels.camp/hackathon/worten_social-responsibility-mission-market).

## Project motivation
This project is about the development of a **community-driven Q&A plattform** to answer FAQs that migrants have in mind but normaly are not able to ask because:
*  They don't speak the local language
*  They don't know whom to ask
*  They feel ashamed for asking because feel judged by the locals
*  They cannot find anyone who speaks their language and can help them
*  They already need to deal with the fact of having to change their lives (voluntarily or, which is worst, unvoluntarily)
*  They are inserted in a different culture and this is already a big barrier

Also, it addresses the problem from another side: **the locals**, who sometimes are not able to answer to these questions because:
*  Procedures for locals and foreigners are different
*  They never did that paperwork, they never had that problem
*  They don't understand why something is a problem for others
*  They sometimes simply don't want to help (personality, discrimnation, etc.)

## Target population
The target of this service are migrants who just moved to Portugal, with access to internet either on a smartphone or a computer.
They don't need to know Portuguese or Enlgish to use the website, and they don't need to download or pay for anything.
The service provided by Rooted will be always free for the migrants.

## Project overview
The platform is a Q&A forum where people will be able to ask the migration-related questions that they always wanted to ask but they didn't dare or weren't able do ask.

This platform has some features that make it unique:
*  It's completely multilingual and has high-quality translations of the content.
*  It's focused on the specific topic of migration FAQs.
*  It's community-created and moderated.

### User stories
We can think about three different user stories:
*  A user can come and look at the questions that someone already asked, those questions can help them understand better their new environment and get things done to solve their problems. After reading the answers., they leave the website.
*  A user comes and looks at the top 5 questions that others wrote. These questions are not very helpful to them and they decide to look for other ones in the searchbox. They find a question that addresses their doubt or issue and leave the website.
*  A user comes and looks at the top 5 questions that others wrote. These questions are not very helpful to them and they decide to look for other ones in the searchbox. There is nothing similar to what he needs, so he decides to ask a new question.

Once questions are created, they get automatically translated into multiple languages and will become ready to be answered by the whole community. When a question is anwswered, it also gets automatically translated into all the languages supported in the website.

*  The user who asked the question will receive a notification saying that their questions was answered, and will be able to read it in their own language.

A special user story involves collaboration with Worten, with an integration between their future platform for social responsibility:
*  Once the users leave their questions, questions are translated, among other languages, into Portuguese. We can integrate out platform with Worten's new one to build a "Five-minutes-a-day partnership", in which they can achieve this social responsibility goal by answering questions from migrants.


### Content moderation
To make the website ready-to-deploy, there will be some curated content by users who already know what are some top questions and concerns from migrants. This content is, by default, moderated.

The new questions, created by the users, will pass through a series of validation, in the case of questions:
*  1. A profanity filter (automatic, such as DeVIL), which will detect curse words and potentially malicious users.
*  2. A data filter, which will prevent people from posting personal data or contact information.
*  3. A relevancy filter (human), where higher-level users will determine if the question is relevant to any of the sections of the website.
*  4. A post-publishing open option for site users to report if a question is irrelevant, outdated or if it violates the code of conduct.


The new answers, on the other hand, will pass through a similar validation process:
*  1. A profanity filter (automatic, such as DeVIL), which will detect curse words and potentially malicious users.
*  2. A data filter, which will prevent people from posting personal data or contact information.
*  3. A relevancy filter (human), where the person who asked will be able to determine if the answer is relevant to the question that he asked.
*  4. A post-publishing open option for site users to report if an answer is irrelevant, outdated or if it violates the code of conduct.


### Gamification strategy
There will be three user types; users, sponsors, admins.

Users and admins will participate in a gamification strategy, in two levels:
*  "Level A", which is the person who reads and asks questions, but doesn't answer the questions.
*  "Level B", which is the person who, additionally to reading and asking, answers the questions from other users.

### Level A break-down with badges
**Just arrived**
A passive user, who reads questions and navigates through the content.

**New in town**
A user who reads questions, navigates and **asks** at least one question.

**Town curious**
A user who asked at least 10 questions.

**Town explorer**
A user who asked at least 50 questions.


### Level B break-down with badges
**Helper**
A user who replied to one question.

**Local guide**
A user who replied to 10 questions.

**Local expert**
A user who replied to 50 questions.

**Local guru**
A user who replied to 100 questions.

**Sponsors**, on the other hand, are always at the "Local guide" level to prevent unfair competition.

## Monetization strategies
The website is an almost 100% text-only site, which results in low maintenance costs and almost very basic needs in terms of engineering power. However, we need to pay the bills, and to get this money we can think about two main sources of income:
*  Donations
*  Paid advertisements from service providers (lawyers, accountants, teachers, etc.) These service providers will pay a subscription that will allow them to answer to questions with the possibility of advertising their services. To give them visibility their answers will always appear in, at least, the second place after other highly-ranked answers from the community.
*  In cases where more than one advertisers compete for a place in the rank for the same question, they can achieve a higher rank by upgrading their subscription. In case they pay the same amount for their subscriptions, the rank will be decided by their level of usefulness.
