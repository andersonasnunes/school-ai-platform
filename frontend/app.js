async function generateLesson() {

  const data = {
    subject: document.getElementById("subject").value,
    grade: document.getElementById("grade").value,
    level: document.getElementById("level").value,
    topic: document.getElementById("topic").value,
    subtopics: document.getElementById("subtopics").value
  };

  const response = await fetch("http://127.0.0.1:8000/ai/lesson", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  });

  const result = await response.json();

  document.getElementById("result").innerText = result.lesson;
}