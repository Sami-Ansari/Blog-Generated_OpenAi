import openai
import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())
openai.api_key =  os.getenv('openai.api_key')

def generate_blog(topic):
    messages = [
        {"role": "system", "content": """You are trained to analyze a topic and generate a blog post.
                                        The blog post must contain 1500 to 3000 words (No less than 1500 words)."""},
        {"role": "user", "content": f"""Analyze the topic and generate a blog post. The topic is {topic}
                                        The blog post should contain the following format.
                                        1) Title (Not more than one line).
                                        2) Introduction (Give introducion about the topic)
                                        3) Add an image url relevent to the topic.
                                        4) Add 2/3 subheadings and explain them.
                                        5) Body (should describe the facts and findings)
                                        6) Add an image url relevent to the topic.
                                        7) Add 2/3 subheadings and explain them.
                                        8) General FAQ regarding the topic.
                                        9) Conclusion of the topic. """}
        ]

    response = openai.ChatCompletion.create(
                      model="gpt-3.5-turbo",
                      messages=messages,
                      max_tokens= 3000,
                      n=1,
                      stop=None,
                      temperature=0.5)

    response_text = response.choices[0].message.content.strip().lower()

    return response_text

user_input ="Data Scientist"
blog = generate_blog(user_input)
print(blog)


# title: the rise of data scientists: unleashing the power of data

# introduction:
# in today's digital age, data has become the new oil, fueling businesses and driving innovation across industries. with the exponential growth of data, organizations are seeking professionals who can extract valuable insights from this vast sea of information. this is where data scientists come into the picture. in this blog post, we will explore the role of data scientists, their skills, and the impact they have on businesses and society as a whole.

# image url: [insert relevant image url here]

# subheading 1: what is a data scientist?
# data scientists are analytical experts who possess a unique blend of technical skills, domain knowledge, and business acumen. they are responsible for collecting, processing, and analyzing large datasets to uncover patterns, trends, and insights that can drive decision-making and strategy. data scientists use a combination of statistical techniques, machine learning algorithms, and programming languages to extract meaningful information from data.

# subheading 2: skills required for data scientists
# 1. strong mathematical and statistical background: data scientists need a solid foundation in mathematics and statistics to understand the underlying principles and techniques used in data analysis. proficiency in areas such as linear algebra, calculus, probability, and statistical modeling is crucial for effective data analysis.

# 2. programming and data manipulation skills: data scientists must be proficient in programming languages such as python or r, as well as sql for data manipulation and querying. they should be able to write efficient code to clean, transform, and preprocess raw data before analysis.

# 3. machine learning and data visualization: familiarity with machine learning algorithms and techniques is essential for data scientists to build predictive models and make data-driven decisions. additionally, they should be skilled in data visualization to effectively communicate insights and findings to stakeholders.

# image url: [insert relevant image url here]

# subheading 3: impact of data scientists on businesses and society
# 1. driving business strategy: data scientists play a crucial role in shaping business strategy by providing insights that drive decision-making. they help organizations understand customer behavior, optimize processes, identify market trends, and develop data-driven products and services. by leveraging the power of data, businesses can gain a competitive edge and make informed decisions.

# 2. enhancing customer experience: data scientists help businesses understand customer preferences, personalize recommendations, and improve overall customer experience. by analyzing customer data, they can identify patterns and trends, enabling organizations to tailor their products and services to meet customer needs effectively.

# 3. solving complex problems: data scientists are problem solvers who tackle complex challenges using data-driven approaches. they can apply their analytical skills to various domains, such as healthcare, finance, cybersecurity, and transportation, to address critical issues and make a positive impact on society.

# general faq regarding data scientists:
# q1. what is the difference between a data scientist and a data analyst?
# a data scientist focuses on extracting insights from data using advanced analytical techniques, while a data analyst primarily focuses on summarizing and visualizing data to support decision-making. data scientists typically have a more extensive skill set and work on complex problems compared to data analysts.

# q2. is coding a necessary skill for data scientists?
# yes, coding is a crucial skill for data scientists. proficiency in programming languages like python or r allows data scientists to manipulate, analyze, and visualize data efficiently. additionally, coding skills enable them to build machine learning models and automate data-related tasks.

# q3. what industries employ data scientists?
# data scientists are in demand across various industries, including finance, healthcare, e-commerce, technology, marketing, and manufacturing. any industry that deals with large volumes of data can benefit from the expertise of data scientists.

# conclusion:
# data scientists are at the forefront of the data revolution, unlocking the power of information and transforming it into actionable insights. their ability to analyze complex datasets and derive meaningful conclusions has a profound impact on businesses, driving innovation and growth. as the volume of data continues to grow exponentially, the demand for skilled data scientists will only increase. by harnessing the skills of these analytical experts, organizations can make data-driven decisions, gain a competitive advantage, and contribute to the betterment of society as a whole.
