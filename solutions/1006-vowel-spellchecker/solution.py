class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        # Helper: replace vowels with '*' and lowercase
        def devowel(word):
            vowels = set('aeiou')
            return ''.join('*' if c in vowels else c for c in word.lower())
        
        # Step 1: Prepare data structures
        exact = set(wordlist)  # exact matches
        case_insensitive = {}  # lowercase -> first occurrence
        vowel_errors = {}      # devoweled -> first occurrence
        
        for word in wordlist:
            lower = word.lower()
            if lower not in case_insensitive:
                case_insensitive[lower] = word
            
            devoweled = devowel(word)
            if devoweled not in vowel_errors:
                vowel_errors[devoweled] = word
        
        # Step 2: Process queries
        answer = []
        for query in queries:
            if query in exact:
                answer.append(query)  # exact match
            elif query.lower() in case_insensitive:
                answer.append(case_insensitive[query.lower()])  # case-insensitive
            elif devowel(query) in vowel_errors:
                answer.append(vowel_errors[devowel(query)])  # vowel errors
            else:
                answer.append("")  # no match
        
        return answer

