// script.js
document.addEventListener('DOMContentLoaded', () => {
    const analyzeBtn = document.getElementById('analyze-btn');
    analyzeBtn.addEventListener('click', async () => {
        console.log("Analyze button clicked");
        const articleText = document.getElementById('article-text').value;
        const response = await fetch('/api/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: articleText })
        });
        const result = await response.json();
        displayResults(result);
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const analyzeBtn = document.getElementById('question-btn');
    analyzeBtn.addEventListener('click', async () => {
        console.log("Question button clicked");
        const articleText = document.getElementById('article-text').value;
        const askedQuestion = document.getElementById('question').value;
        const response = await fetch('/api/question', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: articleText, question: askedQuestion })
        });
        const result = await response.text();
        answerQuestion(result);
    });
});

function displayResults(result) {
    document.getElementById('summary').innerText = result.summary;

    const peopleAndPlaces = document.getElementById('people-and-places');
    peopleAndPlaces.innerHTML = '';
    for (const item of result.people_and_places) {
        const listItem = document.createElement('li');
        listItem.innerText = item;
        peopleAndPlaces.appendChild(listItem);
    }

    const dataPoints = document.getElementById('data-points');
    dataPoints.innerHTML = '';
    for (const item of result.data_points) {
        const listItem = document.createElement('li');
        listItem.innerText = item;
        dataPoints.appendChild(listItem);
    }
}

function answerQuestion(result) {
    document.getElementById('answer').innerText = result;
}