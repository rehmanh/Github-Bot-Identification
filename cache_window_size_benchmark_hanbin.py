import re
import pandas as pd
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from rich.progress import track

class bot_identifier():
    ''' For the identifier, the final output is a single int,
        0 means not a bot,
        1 means maybe a bot, 
        2 means definitely a bot,
    '''

    def __init__(self):
        # cache size here is setted as at least 10 prs' total comments
        self.repo_comments_cache = []
        self.CACHE_SIZE = 20
        self.stop_words = set(["thanks", "thank", "lgtm", "you", "the"])
        self.white_list = ["lgtm", "+1", "retest this please"]
        self.bot_df = pd.DataFrame(columns=["bot_name", "repo", "exmaple_pr", "bot_mark", "Template_identify"])
        self.outputpath = './data/results/bot_identification_result_final.csv'
        self.window_rule_count = 0
        self.window_rule_active_count = 0
        self.bot_list = {}

    def match_bot_keyword(self, user_name):
        ''' 
        User Name identifier
        Using the bot keyword to identify the bot
        '''
        if re.search(r'bot',str(user_name), re.IGNORECASE):
            return 1 # one means a bot-like user or a bot
        else:
            return 0           

    def match_repeat_template(self, user_name, repo_name, user_comment, pr_link, way="first and last words"):
        '''
        Using the repeat template to identify the bot
        the repeat tmeplate is only consider the in repo activity,
        And only the repear comment can be detected.
        #TODO: Consider to add the support for activity
        '''

        # record number of repeat_template checker is activated
        self.window_rule_active_count += 1
        if str(user_comment) == "0" or self.bot_command_identify(user_comment) == 0 or self.special_comments_identify(user_comment) == 0:
            return 0

        ## Clean the comment
        # print(f'user_name: {user_name}')
        # print(f'repo_name: {repo_name}')
        # print(f'user_comment: {user_comment}')
        user_comment = self.remove_stopwords(self.remove_emoji(self.remove_url(self.remove_markdown_image(self.remove_user_id(self.markdown_string_process(str(user_comment), pr_link))))))
        if user_comment == "0":
            return 0
        if not re.search(r'^\s*$', user_comment): # if the user_comment is not empty
            self.cache_the_comments(user_name, repo_name, user_comment)
        if len(self.repo_comments_cache) < 2:
            return 0
        else:
            if way == "first and last words":
                for record in self.repo_comments_cache:
                    sentence = record[2]
                    # print(f'match_temp_sentence: {sentence}')
                    # print(f'match_temp_user_comment: {user_comment}')
                    if user_comment in self.white_list:
                        return 0
                    elif re.search(r'^\s*$', user_comment): # if the user_comment is empty
                        return 0
                    elif sentence.split()[0] == user_comment.split()[0] and sentence.split()[-1] == user_comment.split()[-1]:
                        # record number of repeat_template rule is applied
                        self.window_rule_count += 1
                        return 1
                    # elif sentence.split()[1] == user_comment.split()[1] and sentence.split()[-2] == user_comment.split()[-2]:
                    #     return 1
                    else:
                        return 0
            if way == "nltk":
                for record in self.repo_comments_cache:
                    sentence = record[2]
                    if sentence in self.white_list:
                        return 0
                    try: 
                        score = self.compare_sentence_similarity(user_comment, sentence)
                        if score > 0.8:
                            return 1
                        else:
                            return 0
                    except Exception as e:
                        print(e)
                        print("The sentence is: ", sentence)
                        print("The user_comment is: ", user_comment)

                # print("The way parameter is not missing")

    def markdown_string_process(self, string, pr_link):
        '''Remove the reference block and code block in the markdown string'''
        result_list = []
        ## Remove the reference block
        for line in string.splitlines():
            if line.startswith(">") or line == "":
                pass
            else:
                result_list.append(line)

        ## Remove the code block
        code_line_start = []
        code_line_end = []
        for i in range(len(result_list)):
            if result_list[i][:3] == "```" and len(code_line_start)-len(code_line_end) == 0: #code block can start with both ``` and language name or even diff
                code_line_start.append(i)
            elif (result_list[i][-3:] == "```" or result_list[i].split(' ')[0] == "```")and len(code_line_start)-len(code_line_end) == 1:
                code_line_end.append(i)
        
        # print(code_line_start)
        # print(code_line_end)

        if len(code_line_end) != len(code_line_start):
            # print(f'the pr link is : /n {pr_link}')
            # print(f'the string is : /n {string}')
            # print("===The code block is not closed===")
            return "0"

        removed_ref_block_size = 0
        for _ in range(len(code_line_start)):
            
            for __ in range(code_line_start[_], code_line_end[_]+1):
                # print(f'code_line_start[_]: {code_line_start[_]}')
                # print(f'__: {__}')
                result_list.pop(code_line_start[_]-removed_ref_block_size)
        
            removed_ref_block_size += code_line_end[_] - code_line_start[_] +1

        return " ".join(result_list)
    
    def remove_user_id(self, string):
        '''Remove the user id in the string'''
        return re.sub(r'@\w+', '', string)

    def remove_url(self, string):
        '''Remove the url in the string'''
        return re.sub(r'http\S+', '', string)

    def remove_emoji(self, string):
        '''Remove the emoji in the string'''
        return re.sub(r'\\U\S+', '', string)
    
    def remove_markdown_image(self, string):
        '''Remove the markdown image in the string'''
        return re.sub(r'!\[.*\]\(.*\)', '', string)

    def remove_stopwords(self, string):
        '''Remove the stopwords in the string'''
        return " ".join([word for word in string.split() if word not in self.stop_words])

    def bot_command_identify(self, user_comment):
        '''Identify the bot command'''
        if re.search(r'bot',user_comment.split(" ")[0], re.IGNORECASE) and (re.search(r'run', user_comment.split(" ")[1], re.IGNORECASE) or re.search(r'crossbow', user_comment.split(" ")[0], re.IGNORECASE) or re.search(r'rebase', user_comment.split(" ")[0], re.IGNORECASE)):
            return 0
        elif re.search(r'run', user_comment.split(" ")[0], re.IGNORECASE):
            return 0
        else:
            return -1

    def special_comments_identify(self, user_comment):
        '''Identify the special comments'''
        if re.match(r'R:', user_comment): # Beam project use this to request review
            return 0
        elif re.match(r'Cherry-picked', user_comment): # trafficserver project uses this to cherry-pick the commit
            return 0
        elif re.match(r'\[approve ci', user_comment): # trafficserver project uses this to approve the ci
            return 0
        else:
            return -1
    

    def compare_sentence_similarity(self, sentence1, sentence2):
        # Tokenize the sentences
        sentence1_tokens = word_tokenize(sentence1)
        sentence2_tokens = word_tokenize(sentence2)
        
        # Perform lemmatization on the tokens
        lemmatizer = WordNetLemmatizer()
        sentence1_tokens = [lemmatizer.lemmatize(token) for token in sentence1_tokens]
        sentence2_tokens = [lemmatizer.lemmatize(token) for token in sentence2_tokens]
        
        # Compute the wordnet synsets for each token
        sentence1_synsets = [wordnet.synsets(token) for token in sentence1_tokens]
        sentence2_synsets = [wordnet.synsets(token) for token in sentence2_tokens]
        
        # Flatten the synsets lists
        sentence1_synsets = [synset for synsets in sentence1_synsets for synset in synsets]
        sentence2_synsets = [synset for synsets in sentence2_synsets for synset in synsets]
        
        # Compute the average similarity score between all possible synset pairs
        similarity_scores = []
        for synset1 in sentence1_synsets:
            for synset2 in sentence2_synsets:
                similarity = synset1.wup_similarity(synset2)
                if similarity is not None:
                    similarity_scores.append(similarity)
        if len(similarity_scores) == 0:
            return 0
        else:
            return sum(similarity_scores) / len(similarity_scores)


    def match_repo_name(self, repo_name, user_name):
        '''
        The repo name can be used to identify the bot,
        but we must consider the case that the repo name maybe too
        short, and ealsily to be contained in the user name.
        '''
        ###### TODO: Maybe a good idea ######
        name = repo_name[8:]
        if len(name) <= 3:
            return 0
        elif re.search(name, user_name):
            return 1

    def match_bot_tag(self, user_name):
        if str(user_name)[-5:] == "[bot]":
            return 2 # two means exactly a bot
        elif re.search(r'\[bot\]',str(user_name)):
            return 2

    def match_commenter_keyword(self, user_name):
        if re.search(r'codecov-commenter',str(user_name)):
            return 2
        elif re.search(r'commenter',user_name):
            return 1 # one means a bot-like user or a bot

    def call_bot_anti_filter(self):
        '''
        This function will help the preogram to filter the user who call for the bot repeatedly
        The typical action for the 
        '''
        pass
    

    def cache_the_comments(self, user_name, repo_name, user_comment):
        '''
        Cache the comments of the repo,
        but if the cache is full, then we need to pop the oldest one.
        if the repo changes, then we need to clear the cache.
        '''

        if len(self.repo_comments_cache) != 0:
            if self.repo_comments_cache[-1][0] != repo_name: # if the repo name is not the same as the last one
                self.repo_comments_cache = [] # clear the cache

        self.repo_comments_cache.append([repo_name, user_name, user_comment])
        if len(self.repo_comments_cache) > self.CACHE_SIZE: # Cache size is setted in the __init__ function
            self.repo_comments_cache.pop(0) # pop the first one

    def mathcer(self, user_name, user_comment, repo_name, pr_number, step=3):

        pr_link = "https://www.github.com/"+repo_name+"/pull/"+str(pr_number)

        ## 1. match the bot keyword
        if self.match_bot_tag(user_name) == 2:
            self.bot_df.loc[self.bot_df.shape[0]] = dict(zip(self.bot_df.columns, [user_name, repo_name, pr_link, "2", 0]))
            return 2
        elif self.match_commenter_keyword(user_name) == 2:
            self.bot_df.loc[self.bot_df.shape[0]] = dict(zip(self.bot_df.columns, [user_name, repo_name, pr_link, "2", 0]))
            return 2

        elif self.match_bot_keyword(user_name) == 1:
            # temporarily return 2
            self.bot_df.loc[self.bot_df.shape[0]] = dict(zip(self.bot_df.columns, [user_name, repo_name, pr_link, "2", 0]))
            return 2
        elif self.match_commenter_keyword(user_name) == 1:
            # temporarily return 2
            self.bot_df.loc[self.bot_df.shape[0]] = dict(zip(self.bot_df.columns, [user_name, repo_name, pr_link, "2", 0]))
            return 2
        

        ## 2. match the repo name
        elif self.match_repo_name(repo_name, user_name) == 1:
            # temporarily return 2
            self.bot_df.loc[self.bot_df.shape[0]] = dict(zip(self.bot_df.columns, [user_name, repo_name, pr_link, "2", 0]))
            return 2

        ## 3. match the repeat template

        # elif step == 3:
        #     # print(pr_link)
        #     if self.match_repeat_template(user_name, repo_name, user_comment, pr_link) == 1:
        #         self.bot_df.loc[self.bot_df.shape[0]] = dict(zip(self.bot_df.columns, [user_name, repo_name, pr_link, "1", 1]))
        #         return 1

        elif self.match_repeat_template(user_name, repo_name, user_comment, pr_link) == 1:

            self.bot_df.loc[self.bot_df.shape[0]] = dict(zip(self.bot_df.columns, [user_name, repo_name, pr_link, "2", 1]))
            return 2

        ## 4. keep the developer accounts in the final result
        elif step == 4:
            self.bot_df.loc[self.bot_df.shape[0]] = dict(zip(self.bot_df.columns, [user_name, repo_name, pr_link, "0", 0]))
            return 0

        else:
            return 0

    def setOuput(self, outputpath):
        # check if the output path is csv
        if outputpath[-4:] != ".csv":
            raise ValueError("The output path must be a csv file")
        self.outputpath = outputpath

    def precision_score(self, ground_truth, classificaiotn_result):
        '''
        Calculate the precision score
        '''
        TP = 0
        FP = 0
        for i in range(len(ground_truth)):
            if ground_truth[i] == 2 and (classificaiotn_result[i] == 1 or classificaiotn_result[i] == 2):
                TP += 1
            elif (ground_truth[i] == 0 and classificaiotn_result[i] == 1) or (ground_truth[i] == 0 and classificaiotn_result[i] == 2):
            # elif ground_truth[i] == 0 and (classificaiotn_result[i] == 1 or classificaiotn_result[i] == 2):
                FP += 1
        print("current size: " + str(self.CACHE_SIZE))
        print("precision: TP: " + str(TP))
        print("precision: FP: " + str(FP))
        return TP / (TP + FP)
    
    def recall_score(self, ground_truth, classificaiotn_result):
        '''
        Calculate the recall score
        '''
        TP = 0
        FN = 0
        for i in range(len(ground_truth)):
            if ground_truth[i] == 2 and (classificaiotn_result[i] == 1 or classificaiotn_result[i] == 2):
                TP += 1
            elif ground_truth[i] == 2 and classificaiotn_result[i] == 0:
                FN += 1
        print("current size: " + str(self.CACHE_SIZE))
        print("recall: TP: " + str(TP))
        print("recall: FP: " + str(FN))
        return TP / (TP + FN)
    
    def f1_score(self, ground_truth, classificaiotn_result):
        '''
        Calculate the f1 score
        '''
        precision = self.precision_score(ground_truth, classificaiotn_result)
        recall = self.recall_score(ground_truth, classificaiotn_result)
        return 2 * precision * recall / (precision + recall)
    
    def set_cache_size(self, size):
        self.CACHE_SIZE = size

    def run(self, df, step=4, truth="inline"):

        ground_truth = []
        classificaiotn_result = []

        for index, row in track(df.iterrows(), description="Bot identification...", total=df.shape[0]):
            classificaiotn=self.mathcer(row["user"], row["comment_body"].lower(), row["repo_name"], row["pull_number"], step=step)
            classificaiotn_result.append(classificaiotn)
            if truth == "external":
                ground_truth.append(self.get_ground_truth(row["user"]))
            elif truth == "inline":
                ground_truth.append(row["Bot"])

        
        # Calculate the Precision, Recall, F1-score
        print("The precision is: ", self.precision_score(ground_truth, classificaiotn_result))
        print("The recall is: ", self.recall_score(ground_truth, classificaiotn_result))
        print("The f1-score is: ", self.f1_score(ground_truth, classificaiotn_result))
        
        self.bot_df.to_csv(self.outputpath, index=False)

    def set_bot_list(self, bot_list_path):
        bot_list_df = pd.read_csv(bot_list_path)
        self.bot_list = set(bot_list_df.iloc[1:44, 0])

    def get_ground_truth(self, user_name):
        # check if user_name is in bot_list
        if user_name in self.bot_list:
            return 2
        else:
            return 0



if __name__ == "__main__":
    
    WINDOW_SIZE = [5, 10, 15, 20] # the window size for the repeat template

    for window_size in WINDOW_SIZE:
        # Manual Tagged evaluation dataset File
        df = pd.read_csv("/Users/rehmanh/Desktop/Research/Chenhao Bot Study/Evaluation Dataset - Final Evaluation Dataset.csv") # here is the raw dataset file path
        
        # Init the object
        bot_identification = bot_identifier()

        # Set bot list file used for ground truth
        # bot_identification.set_bot_list("./data/bot-account-list-habib.csv")

        # Set Window Size
        bot_identification.set_cache_size(window_size)
        bot_identification.setOuput("/Users/rehmanh/Desktop/Research/Chenhao Bot Study/cache_size_hanbin_%d.csv" % window_size) # here is the output file path
        print("The window size is: ", window_size)

        # reset the counter
        bot_identification.window_rule_count = 0
        bot_identification.window_rule_active_count = 0

        # Run the Script
        bot_identification.run(df, step=4, truth="inline")
        print("number of window size rule activated/applied: " + str(bot_identification.window_rule_active_count) + '/' + str(bot_identification.window_rule_count))

