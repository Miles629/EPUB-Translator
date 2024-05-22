# python3
# Please install OpenAI SDK first：`pip3 install openai`
from openai import OpenAI


def translate(text,language):
    client = OpenAI(api_key="sk-xxxxx", base_url="https://api.deepseek.com")
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a professional translator who has translated numerous literary works. When it comes to proper nouns, you can choose to translate them faithfully, elegantly, and smoothly, or not translate them at all. Consistency in the translation of names and objects is important. Please translate the given content while maintaining its original format, and you only need to reply with the translated result and keep the paragraph number. Now, please translate the following text into {}.".format(language)},
            {"role": "user", "content": "{}".format(text)},
        ],
        stream=False
    )

    return(response.choices[0].message.content)
# print(translate("资本主义影响了我们生活中的各个方面，我们的生活中充满着来自世界各地的商品。我们生活的时代也是全球化的时代。我们都知道，波音飞机这样的商品涉及多国合作，往往发动机在一国生产，机翼在另一国生产，而控制系统又在另一国生产。但是我们没有意识到的是，即使像衣服这种看似稀松平常的事物，也同样是全球化的产物。就我们所穿着的日常衣服，很可能棉花产自美国、埃及或乌兹别克斯坦，然后在中国和越南纺成纱线，在印度尼西亚织造成衣服，最后再通过一个发达的全球运输系统，出现在世界各地的超市中。这些都是资本主义的奇迹，也是全球化的产物。","English"))
