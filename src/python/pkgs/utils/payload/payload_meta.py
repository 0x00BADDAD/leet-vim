
OpNames = {
        'question_data': "questionDetail",
        'question_filter_list': "problemsetQuestionListV2"
}

variables_keyed = {
        'question_data': {"titleSlug" : "add-two-numbers"},
        'question_filter_list': {"skip":0,"limit":100,"categorySlug":"all-code-essentials","filters":{"filterCombineType":"ALL","statusFilter":{"questionStatuses":[],"operator":"IS"},"difficultyFilter":{"difficulties":["MEDIUM"],"operator":"IS"},"languageFilter":{"languageSlugs":[],"operator":"IS"},"topicFilter":{"topicSlugs":["dynamic-programming"],"operator":"IS"},"acceptanceFilter":{},"frequencyFilter":{},"lastSubmittedFilter":{},"publishedFilter":{},"companyFilter":{"companySlugs":[],"operator":"IS"},"positionFilter":{"positionSlugs":[],"operator":"IS"},"premiumFilter":{"premiumStatus":[],"operator":"IS"}},"searchKeyword":"","sortBy":{"sortField":"CUSTOM","sortOrder":"ASCENDING"},"filtersV2":{"filterCombineType":"ALL","statusFilter":{"questionStatuses":[],"operator":"IS"},"difficultyFilter":{"difficulties":["MEDIUM"],"operator":"IS"},"languageFilter":{"languageSlugs":[],"operator":"IS"},"topicFilter":{"topicSlugs":["dynamic-programming"],"operator":"IS"},"acceptanceFilter":{},"frequencyFilter":{},"lastSubmittedFilter":{},"publishedFilter":{},"companyFilter":{"companySlugs":[],"operator":"IS"},"positionFilter":{"positionSlugs":[],"operator":"IS"},"premiumFilter":{"premiumStatus":[],"operator":"IS"}}}
}


query_literals = {

        'question_data': '\n    query questionDetail($titleSlug: String!) {\n  languageList {\n    id\n    name\n  }\n  submittableLanguageList {\n    id\n    name\n    verboseName\n  }\n  statusList {\n    id\n    name\n  }\n  questionDiscussionTopic(questionSlug: $titleSlug) {\n    id\n    commentCount\n    topLevelCommentCount\n  }\n  ugcArticleOfficialSolutionArticle(questionSlug: $titleSlug) {\n    uuid\n    chargeType\n    canSee\n    hasVideoArticle\n  }\n  question(titleSlug: $titleSlug) {\n    title\n    titleSlug\n    questionId\n    questionFrontendId\n    questionTitle\n    translatedTitle\n    content\n    translatedContent\n    categoryTitle\n    difficulty\n    stats\n    companyTagStatsV2\n    topicTags {\n      name\n      slug\n      translatedName\n    }\n    similarQuestionList {\n      difficulty\n      titleSlug\n      title\n      translatedTitle\n      isPaidOnly\n    }\n    mysqlSchemas\n    dataSchemas\n    frontendPreviews\n    likes\n    dislikes\n    isPaidOnly\n    status\n    canSeeQuestion\n    enableTestMode\n    metaData\n    enableRunCode\n    enableSubmit\n    enableDebugger\n    envInfo\n    isLiked\n    nextChallenges {\n      difficulty\n      title\n      titleSlug\n      questionFrontendId\n    }\n    libraryUrl\n    adminUrl\n    hints\n    codeSnippets {\n      code\n      lang\n      langSlug\n    }\n    exampleTestcaseList\n    hasFrontendPreview\n  }\n}\n',



        'question_filter_list': '\n    query problemsetQuestionListV2($filters: QuestionFilterInput, $limit: Int, $searchKeyword: String, $skip: Int, $sortBy: QuestionSortByInput, $categorySlug: String) {\n  problemsetQuestionListV2(\n    filters: $filters\n    limit: $limit\n    searchKeyword: $searchKeyword\n    skip: $skip\n    sortBy: $sortBy\n    categorySlug: $categorySlug\n  ) {\n    questions {\n      id\n      titleSlug\n      title\n      translatedTitle\n      questionFrontendId\n      paidOnly\n      difficulty\n      topicTags {\n        name\n        slug\n        nameTranslated\n      }\n      status\n      isInMyFavorites\n      frequency\n      acRate\n    }\n    totalLength\n    finishedLength\n    hasMore\n  }\n}\n    '

                  }
