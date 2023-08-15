from chains.review_chain import create_review_chain


class ReviewGenerator:
    """
    A class used to generate reviews based on website description, accessibility assessment, persona, and paragraph limit.

    Attributes
    ----------
    review_chain : function
        The main chain used to generate reviews.

    Methods
    -------
    generate(website_description, accessibility_assessment, persona, paragraph_limit)
        Generates a review based on the given inputs.
    """
    def __init__(self):
        self.review_chain = create_review_chain()  # main chain

    def generate(self, website_description, accessibility_assessment, persona, paragraph_limit):
        """
        Generates a review based on the given inputs.

        Parameters
        ----------
        website_description : str
            A description of the website being reviewed.
        accessibility_assessment : list
            An assessment of the website's accessibility.
        persona : dict
            The persona of the reviewer.
        paragraph_limit : int
            The maximum number of paragraphs in the review.

        Returns
        -------
        str
            The generated review.
        """

        inputs = {
            "website_description": website_description,
            "accessibility_assessment": accessibility_assessment,
            "persona": persona,
            "paragraph_limit": paragraph_limit,
        }

        output = self.review_chain(inputs)

        return output["clean_review_limit"]

