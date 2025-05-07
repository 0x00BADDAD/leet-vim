import asyncio
import aiohttp
import json

operationName= "questionDetail"
variables = {"titleSlug" : "add-two-numbers"}
query= "\n    query questionDetail($titleSlug: String!) {\n  languageList {\n    id\n    name\n  }\n  submittableLanguageList {\n    id\n    name\n    verboseName\n  }\n  statusList {\n    id\n    name\n  }\n  questionDiscussionTopic(questionSlug: $titleSlug) {\n    id\n    commentCount\n    topLevelCommentCount\n  }\n  ugcArticleOfficialSolutionArticle(questionSlug: $titleSlug) {\n    uuid\n    chargeType\n    canSee\n    hasVideoArticle\n  }\n  question(titleSlug: $titleSlug) {\n    title\n    titleSlug\n    questionId\n    questionFrontendId\n    questionTitle\n    translatedTitle\n    content\n    translatedContent\n    categoryTitle\n    difficulty\n    stats\n    companyTagStatsV2\n    topicTags {\n      name\n      slug\n      translatedName\n    }\n    similarQuestionList {\n      difficulty\n      titleSlug\n      title\n      translatedTitle\n      isPaidOnly\n    }\n    mysqlSchemas\n    dataSchemas\n    frontendPreviews\n    likes\n    dislikes\n    isPaidOnly\n    status\n    canSeeQuestion\n    enableTestMode\n    metaData\n    enableRunCode\n    enableSubmit\n    enableDebugger\n    envInfo\n    isLiked\n    nextChallenges {\n      difficulty\n      title\n      titleSlug\n      questionFrontendId\n    }\n    libraryUrl\n    adminUrl\n    hints\n    codeSnippets {\n      code\n      lang\n      langSlug\n    }\n    exampleTestcaseList\n    hasFrontendPreview\n  }\n}\n"



def make_url():
    question_url= 'https://leetcode.com/graphql/'
    return question_url


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.post(make_url(), json={'operationName': operationName, 'query': query, 'variables':variables}) as resp:
            print(resp.status)
            resp_text = await resp.json()
            resp_text = resp_text['data']['question']

            print(f'Type of resp_test is: {type(resp_text)}\n')
            for k in resp_text.keys():
                print(f'key-> {k}\n')

            ##with open('question.json', 'w') as resp_file:
            ##    json.dump(resp_text, resp_file)
            resp_text = '<html><head></head><body>' + resp_text['content'] + '</body></html>'
            with open('question.html', 'w') as q_html:
                q_html.write(resp_text)

if __name__ == '__main__':
    asyncio.run(main())



