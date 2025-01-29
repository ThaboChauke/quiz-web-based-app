# Web-Based Quiz Application

This is a dynamic, interactive, and web-based quiz application built with Flask. Users can select a quiz topic, answer questions, and view their scores upon completion.

## Features

- **Dynamic Quiz Selection:** Users can choose from a variety of quiz topics.
- **Randomized Questions:** Questions are randomized for a fresh experience each time.
- **Score Display:** Users can view their scores upon quiz completion.
- **Topic Request Form:** Users can request new quiz topics via a dedicated support page.
- **Data Storage:** Quizzes and their questions are stored in an SQLite database.

## Technologies Used

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Database:** SQLite

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ThaboChauke/quiz-web-based-app.git
   cd quiz-web-based-app
   ```
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database:
   ```bash
   flask shell
   >>> from app import db
   >>> db.create_all()
   ```
5. Run the application:
   ```bash
   flask run
   ```
6. Access the application at `http://127.0.0.1:5000`.

## Usage

1. Navigate to the homepage to view the available quizzes.
2. Click on a quiz to start answering questions.
3. Submit your answers to view your score.
4. Use the "Support" page to request new topics or provide feedback.

## Acknowledgments

This project utilized images from Unsplash. Gratitude to the respective photographers:

- Photo by [Patrick Tomasso](https://unsplash.com/@impatrickt?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/open-book-lot-Oaqk7qqNh_c?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
- Photo by [Hans Reniers](https://unsplash.com/@hansreniers?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/three-clear-beakers-placed-on-tabletop-lQGJCMY5qcM?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
- Photo by [Kyle Glenn](https://unsplash.com/@kylejglenn?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/desk-globe-on-table-nXt5HtLmlgE?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
- Photo by [Tech Daily](https://unsplash.com/@techdailyca?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/a-flat-screen-tv-sitting-on-top-of-a-wooden-table-cF6Le-0viHY?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
- Photo by [Swati Kedia](https://unsplash.com/@phoenix_2022?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/a-group-of-red-shirts-in-a-room-with-benches-CTLuPLp-LDg?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
- Photo by [Antoine Dautry](https://unsplash.com/@antoine1003?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/black-retractable-pen-on-white-printer-paper-_zsL306fDck?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
- Photo by [Mr Cup / Fabien Barral](https://unsplash.com/@iammrcup?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/black-and-white-photo-lot-Fo5dTm6ID1Y?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
- Photo by [Jessica Lewis 🧜‍♀️ thepaintedsquare](https://unsplash.com/@thepaintedsquarejessica?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/person-writing-on-white-paper-zNFT3o8HWks?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)

## License

This project is licensed under the MIT License. See the [LICENSE](/LICENSE) file for details.

