# map funtion map(func, *iterables)
def square(x):         # 计算平方数
    return x ** 2


map(square, [1, 2, 3, 4, 5])    # 计算列表各个元素的平方
list(map(square, [1, 2, 3, 4, 5]))   # 使用 list() 转换为列表
[1, 4, 9, 16, 25]
list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))   # 使用 lambda 匿名函数
[1, 4, 9, 16, 25]

L1 = [
    ('Bread', 10),
    ('BUtter', 20),
    ('Cake', 19)
]
L2 = list(map(lambda item: item[1], L1))
print(L2)
L3 = list(map(lambda item: (item[0], item[1]*1.2), L1))
print(L3)
'''----------'''


def get_item_1(item):
    return item[1]


'''---------- exercise 20'''
num = [1, 2, 3, 4, 5]
num1 = list(map(lambda item: (item**3), num))
print(num1)
'''---------- exericse 30'''
text = '''
Artificial Intelligence (AI) is a rapidly evolving field that involves the development of computer systems capable of performing tasks that typically require human intelligence such as 
visual perception, speech recognition, and decision-making. AI systems can be trained using large amounts of data to recognize patterns and make predictions. Machine learning is a 
subfield of AI that focuses on the development of algorithms that can learn from and make predictions based on data. The use of AI is becoming widespread across various industries, 
including healthcare, finance, transportation, and retail. While AI has the potential to bring about significant positive change in our society, it also raises ethical and social issues. 
For example, the use of AI in decision-making could perpetuate existing biases and lead to unfair outcomes. There are also concerns about job displacement as AI systems become more capable 
of performing tasks that were previously done by humans. To address these challenges, there is a growing need for responsible and ethical AI development and deployment. 
This involves creating systems that are transparent, explainable, and accountable, as well as investing in education and training to ensure that individuals have the skills and knowledge 
to participate in the AI-driven economy. In conclusion, AI is a rapidly evolving field that has the potential to bring about significant positive change, but it is important that we approach 
its development and deployment with caution and responsibility.
'''
text1 = text.split()


def map_longest(text1: str) -> tuple:
    '''
    Function returns the longest word in the text and it's length

    Parameters:
        text: any text

    Returns:
        tuple: a tuple containing the longest word and it's length

    '''
    '''the_longest_word = max(text1, key=lambda word: len(word))
    return the_longest_word, len(the_longest_word)'''
    the_longest_word = list(map(lambda item: (len(item), item), text1))
    sorted_text = sorted(the_longest_word, reverse=True)
    print(
        f"The longest word in the text is '{sorted_text[0][1]}' with the length of {sorted_text[0][0]} characters.")
    # sorting order from the word length
    '''
    my_text = text.split()
    result = list(map(lambda item: (len(item), item), my_text))
    sorted_text = sorted(result, reverse=True)
    longest = sorted_text[0]
    text = (
        f'The longest word in the text is {longest[1]} with the length of {longest[0]} characters')
    return text'''


map_longest(text1)

'''-------------------------------'''
