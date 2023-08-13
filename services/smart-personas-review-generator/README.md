**Smart Personas Review Generator**  
Review Generator

**Description**  
The Review Generator project automates the creation of website reviews based on given personas, website descriptions, and accessibility assessments. By utilizing language models and chaining different transformers, it can generate contextually relevant reviews.

**Getting Started**

**Installing**
1. Clone the repository:  
   `git clone https://github.com/yourusername/review-generator.git`
2. Navigate to the project directory:  
   `cd review-generator`
3. Install the required packages:  
   `pip install -r requirements.txt`

**Executing program**
1. Initialize the Review Generator:  
   `from review_generator import ReviewGenerator`  
   `generator = ReviewGenerator()`
2. Generate a review by calling the `generate` method with required parameters:  
   `review = generator.generate(website_description, accessibility_assessment, persona, paragraph_limit)`  
   `print(review)`

**Authors**
- Miguel Franken 

---
