# Quiz Question Generator

This project implements a quiz question generator service and a simple web interface to consume the service’s API. It uses the OpenAI API to generate multiple-choice questions based on a single learning objective. Each question includes four answer choices with exactly one correct answer. The service is designed for higher education students and is deployed as an API with a minimal web interface for testing.


## How to Use

1. **Setup:**
   - Clone the repository.
   - Create a virtual environment:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Install the dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Configure the OpenAI API key:
        - Copy `.env.example` and create your own `.env` file:
          ```bash
          cp .env.example .env
          ```
        - Open `.env` and add your OpenAI API key:
          ```
          OPENAI_API_KEY=your_api_key
          ```
        - Alternatively, you can set an environment variable `OPENAI_API_KEY`.
2. **Running the Application:**
   - To run the API and web interface:
     ```bash
     python app.py
     ```
   - Open your browser and navigate to `http://127.0.0.1:PORT` to access the interface.

3. **API Usage:**
   - The API exposes a `/generate` endpoint that accepts a POST request with a JSON payload:
     ```json
     {
       "learning_objective": "Balance chemical equations using the law of conservation of mass"
     }
     ```
   - The endpoint returns a generated quiz question in JSON format.

## Deployment

- **Cloud Deployment:**
  - Platforms like Heroku, AWS Elastic Beanstalk, or Google App Engine can be used.
  - Ensure that the required environment variables (e.g., `OPENAI_API_KEY`, `PORT`) are properly set in the deployment environment.
  - The repository can be easily configured for deployment with a `Procfile` (if using Heroku) or with Docker.

- **Docker Deployment:**
  - Build the Docker image:
    ```bash
    docker build -t quiz-generator .
    ```
  - Run the Docker container:
    ```bash
    docker run -p 5001:5000 --env-file .env quiz-generator
    ```

## Quality and Scientific Correctness Assurance

- **Prompt Engineering:** The prompt is carefully designed to ensure questions are relevant, scientifically accurate, and aligned with higher education standards.
- **Post-Processing:** The response from the OpenAI API is validated to ensure it contains exactly one correct answer and follows the required format.
- **Testing:** Unit tests and manual testing can be implemented to verify that the generator produces high-quality and accurate questions.
- **Expert Review:** Periodic reviews by subject matter experts help improve the prompt design and output quality.

## Development Process

- **Steps Taken:**
  - Designed the project structure.
  - Developed the quiz generation service using the OpenAI API.
  - Implemented the Flask API and web interface.
  - Integrated deployment configurations (Docker).
  - Documented the process and ensured quality through testing.
  
- **Challenges:**
  - Crafting prompts that consistently produce multiple-choice questions with one correct answer.
  - Balancing API usage within a budget of $50.
  
- **Future Improvements:**
  - Extend support to other types of questions.
  - Enhance the web interface with richer user interactions.
  - Add detailed logging and monitoring for production environments.
