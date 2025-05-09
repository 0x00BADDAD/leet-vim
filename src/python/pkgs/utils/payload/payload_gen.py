from pkgs.utils.payload.payload_meta import OpNames, variables_keyed, query_literals




def payload_gen(OpKey, data):

    """
        This function generates the json payload (or a python dict which is marshalled by aiohttp into a serialized json) with suitable data
    """
    match OpKey:
        case 'question_data':
            name = OpNames[OpKey]               ## get the name of operation
            qname = data[0]
            vars_data = variables_keyed[OpKey]  ## get the variables with some
            vars_data['titleSlug'] = qname
                                               ## sample data that will be updated with
                                               ## the argument passed as data

            gql_query = query_literals[OpKey]   ## get the gql query for the leetcode API

        case 'question_filter_list':
            name = OpNames[OpKey]
            difficulty_list, topic_list, nums = data ## data in tuples

            ## setting the variable according to the data passed
            vars_data = variables_keyed[OpKey] ## copy of the dict (?)
            vars_data['limit'] = nums
            vars_data['filters']['difficultyFilter']['difficulties'] = difficulty_list
            vars_data['filters']['topicFilter']['topicSlugs'] = topic_list

            gql_query = query_literals[OpKey]


    return {
            'operationName': name,
            'query': gql_query,
            'variables': vars_data
            }
