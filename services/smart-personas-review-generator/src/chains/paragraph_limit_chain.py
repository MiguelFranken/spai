from langchain import LLMChain
from langchain.chains import SequentialChain, TransformChain
from components.lm_connector_factory import LLMConnectorFactory
from templates.paragraph_limit_prompt_template import generate_paragraph_limit_prompt_template
from templates.website_description_prompt_template import generate_website_description_prompt_template
from transformers.website_context_transformer import transform_website_context


def create_paragraph_limit_chain():
    llm_connector = LLMConnectorFactory.create_connector()

    prompt = generate_paragraph_limit_prompt_template()
    llm_chain = LLMChain(
        llm=llm_connector.get_llm,
        prompt=prompt,
        output_key="clean_review_limit",
        verbose=True
    )

    return SequentialChain(
        chains=[llm_chain],
        input_variables=["clean_review"],
        output_variables=["clean_review_limit"],
        verbose=True
    )
