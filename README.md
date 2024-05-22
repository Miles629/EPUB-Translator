# EPUB-Translator

# 电子书翻译器EPUB-Translator

## 简介

`EPUB-Translator` 是一个旨在通过调用大型语言模型的API来实现电子书翻译的GitHub仓库。我们的目标是提供一种高效、准确的方式来翻译EPUB格式的电子书。

**Introduction**

`EPUB-Translator` is a GitHub repository aimed at translating eBooks by invoking the APIs of large language models. Our goal is to provide an efficient and accurate method for translating eBooks in EPUB format.

## 优缺点

- **逐段翻译**：将翻译结果逐段附加到原文下方，实现“沉浸式翻译”体验。
- **章节翻译**：翻译策略，一次翻译一个完整的章节，减少token消耗(主要是减少多次调用prompt)。存在可能的缺陷，返回段落数和应翻译的段落数不匹配，会导致全部重新翻译。
- **仅翻译文本**: 为了减少token消耗，所有的有格式文本都将以纯文本的形式传入。但这也会导致结果中丢失文本格式。
- **自定义API调用**：用户可以根据自己的需求选择不同的语言模型API。

**Pros and Cons**

- **Segment-by-Segment Translation**: The translation results are appended segment by segment below the original text, providing an "immersive translation" experience.
- **Chapter-by-Chapter Translation**: The translation strategy translates a complete chapter at once, reducing token consumption (mainly by reducing multiple prompt calls). There is a potential flaw where the number of returned paragraphs does not match the number of paragraphs to be translated, which could lead to a complete retranslation.
- **Text-Only Translation**: To reduce token consumption, all formatted text is passed in as plain text. However, this also results in the loss of text formatting in the results.
- **Customizable API Calls**: Users can choose different language model APIs according to their own needs.

## 使用方法Usage

1. **克隆仓库Clone the Repository**：

   ```bash
   git clone https://github.com/yourusername/EPUB-Translator.git
   ```

2. **安装依赖Install Dependencies**：

   ```bash
   cd EPUB-Translator
   pip install -r requirements.txt
   ```

3. **配置APIConfigure API**：
   在 `DeepSeek.py` 文件中配置您的语言模型API密钥。其他大模型请参考官方文档的调用指南。

4. **运行翻译Run Translation**：

   ```bash
   python orderreadwrite.py 
   ------or------
   python app.py
   ```

## 贡献

我们欢迎任何形式的贡献，包括但不限于代码优化、文档编写、问题报告等。

**Contribution**

We welcome any form of contribution, including but not limited to code optimization, documentation writing, and issue reporting.

## 许可证

本项目遵循 [MIT 许可证](LICENSE)。

**License**

This project is licensed under the [MIT License](LICENSE).

## 联系我们

如果您有任何问题或建议，请通过以下方式联系我们：

- GitHub Issues: [https://github.com/Miles629/EPUB-Translator/issues](https://github.com/Miles629/EPUB-Translator/issues)

**Contact Us**

If you have any questions or suggestions, please contact us through the following methods:

- GitHub Issues: [https://github.com/Miles629/EPUB-Translator/issues](https://github.com/Miles629/EPUB-Translator/issues)

---

感谢您对 `EPUB-Translator` 的关注和支持！我们期待与您一起改进电子书翻译体验。

**Thank You**

Thank you for your interest and support in `EPUB-Translator`! We look forward to improving the eBook translation experience together with you.