from textwrap import dedent

from langchain import PromptTemplate


def generate_paragraph_limit_prompt_template():
    template = """
    You wrote the following review:
    {clean_review}

    Your previous review was either too long or too short. Please rewrite the review to be exactly three paragraphs
    in length.

    Review:
    """

    prompt_template = PromptTemplate(
        input_variables=[
            "clean_review"
        ],
        template=dedent(template).strip()
    )

    return prompt_template
