import ast

def get_matched_moods(user_mood_list):
    mood_set = set()
    with open('sentiment.txt', 'rt') as f:
        for line in f:
            print ('Getting list')
            inverted_list = line.split(',')
            for element in inverted_list:
                element_dict = ast.literal_eval(element)
                for key, val in element_dict.items():
                    print(key, 'dict', val)
                    if key in user_mood_list:
                        mood_set.add(val)
    return mood_set

#print (get_matched_moods({'anger', 'happy'}))



def get_matched(user_mood_list, filename):
    mood_set = set()
    whip = eval(open(filename, 'r').read())
    for mood in user_mood_list:
        cur_set = set()
        for k, v in whip.items():
            if k.lower() == mood.lower():
                cur_set.update(set(v))
        if len(mood_set) == 0:
            mood_set = cur_set
        else:
            mood_set = set.intersection(cur_set, mood_set)

    return mood_set

def check_similarity(user_moods, user_audience):
    matched_moods = get_matched(user_moods, 'sentiment.txt')
    matched_audience = get_matched(user_audience, 'audience.txt')

    print('Matched moods', matched_moods)
    print('Matched audience', matched_audience)
    overall_set = set.intersection(matched_moods, matched_audience)

    print('Overall mood and audience', overall_set)
    return overall_set
